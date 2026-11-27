# Planetarium — organização do código-fonte

Este documento é um plano. Ele não muda nenhum código: descreve como sair do arquivo único `index.html` para uma estrutura de pastas, sem perder nenhuma função e sem parar o app no ar.

## 1. Como está hoje

Tudo o que o app faz está dentro de `index.html` (cerca de 310 KB e 1.800 linhas muito longas):

| Parte | Tamanho aproximado |
|---|---|
| Estilos (CSS) | 20 KB |
| Estrutura da tela (HTML: topo, menu, fichas, cartões) | 27 KB |
| Código (JavaScript) | 262 KB |

Fora dele ficam apenas os dados (`sky.json`, `art.json`, `cidades-*.json`, `terra/`, `art/`), a biblioteca `lib/satellite.min.js`, o `sw.js` (funcionamento offline), o `manifest.webmanifest` e os scripts Python de `tools/` que geram os dados.

### Por que começou assim

Um arquivo único publica em qualquer lugar sem etapa de construção, funciona offline com um service worker simples e foi rápido para iterar. Para um protótipo, foi a escolha certa.

### Por que agora atrapalha

- **Tudo enxerga tudo.** Há dezenas de variáveis globais compartilhadas (`st`, `dv`, `SV`, `CV`, `FL`, `ET`, `G3`, `WX`, `WG`, `REC`…). Uma mudança no disco pode quebrar o globo sem aviso.
- **A ordem do arquivo importa.** Já houve erros de "variável usada antes de existir" por causa da ordem de declaração.
- **Difícil de revisar.** Linhas com milhares de caracteres impedem ver o que mudou num commit.
- **Sem testes automáticos.** A verificação hoje é manual, com capturas de tela.
- **Nomes curtos e enigmáticos** (`svEarthGL`, `etSelectDisc`, `g3Tex`, `drawDisc0`) que só fazem sentido para quem escreveu.
- **Cache inteiro a cada versão.** Qualquer ajuste muda os 310 KB do `index.html`, e o celular baixa tudo de novo.

## 2. Direção recomendada

**JavaScript moderno em módulos, sem framework, com o Vite para montar a versão publicada.**

- **Sem framework (React, Vue etc.):** o app é quase todo desenho em Canvas 2D e WebGL. Um framework de interface não ajuda nisso e acrescentaria peso.
- **Módulos ES** (`import`/`export`): cada arquivo declara do que precisa. Acaba o "tudo enxerga tudo" e a dependência da ordem.
- **Vite:** em desenvolvimento serve os módulos direto; para publicar, junta e reduz tudo em poucos arquivos com nomes únicos por versão. Assim o celular só baixa de novo o que mudou.
- **TypeScript: depois, opcional.** Dá para começar em JavaScript e adotar TypeScript aos poucos, começando pelos cálculos astronômicos, onde ele mais ajuda a evitar erros de unidade (graus × radianos, km × raio da Terra).
- **Publicação:** um GitHub Actions roda `vite build` e publica a pasta `dist/` no GitHub Pages. O artefato do Claude passa a receber o conteúdo de `dist/`.

Alternativa mais simples, se preferir não ter etapa de construção: os mesmos módulos ES carregados direto pelo navegador (`<script type="module">`). Funciona no GitHub Pages e nos celulares atuais, mas são mais arquivos para baixar e o cache fica mais trabalhoso. A recomendação continua sendo o Vite.

## 3. Estrutura de pastas proposta

```
planetarium/
├─ index.html                 só a casca: marcação da tela + <script type="module" src="/src/main.js">
├─ public/                    copiado como está para a publicação
│  ├─ manifest.webmanifest
│  ├─ icons/                  icon-192.png, icon-512.png
│  ├─ data/                   sky.json, art.json, cidades-br.json, cidades-mundo.json
│  ├─ terra/                  dia.jpg, noite.jpg, mapa.jpg, gleason.jpg, lua.webp
│  ├─ art/                    desenhos das constelações
│  └─ lib/                    satellite.min.js
├─ src/
│  ├─ main.js                 inicialização: carrega dados, monta a interface, inicia o laço
│  ├─ app/
│  │  ├─ state.js             estado central (hoje `st`) e camadas ligadas/desligadas
│  │  ├─ prefs.js             tudo que é salvo no aparelho (chaves "planetarium-*")
│  │  ├─ modes.js             Imersivo / Disco / Globo / mergulho e as viagens entre eles
│  │  ├─ layout.js            tela dividida, lado a lado, paisagem/retrato
│  │  └─ loop.js              laço de quadros, relógio da simulação, velocidade
│  ├─ astro/                  cálculo puro, sem desenho (testável)
│  │  ├─ time.js              data juliana, tempo sideral (GMST)
│  │  ├─ sun.js               Sol (NOAA)
│  │  ├─ moon.js              Lua (Schlyter), fases
│  │  ├─ planets.js           elementos orbitais do JPL, posição heliocêntrica
│  │  ├─ coords.js            equatorial ↔ eclíptica ↔ horizonte, projeção do disco (toDisc/fromDisc)
│  │  ├─ eclipses.js
│  │  ├─ tides.js
│  │  └─ geomag.js            declinação magnética (WMM2025)
│  ├─ data/
│  │  ├─ catalog.js           estrelas, constelações, Via Láctea, distâncias (STARLY)
│  │  ├─ cities.js            cidades do mundo e do Brasil, busca
│  │  └─ art.js               desenhos das constelações
│  ├─ render/
│  │  ├─ labels.js            fila de rótulos sem sobreposição (LBQ)
│  │  ├─ sky/                 Imersivo: céu, Sol e Lua, paisagem, zodíaco, rastros, nuvens do céu
│  │  ├─ disc2d/              disco 2D clássico
│  │  ├─ gl/
│  │  │  ├─ context.js        criação, perda e recuperação do WebGL
│  │  │  ├─ camera.js         projeção usada também pelos rótulos (vproj)
│  │  │  └─ shaders/          cada shader no seu arquivo (terra, nuvens, chão, pontos, linhas)
│  │  ├─ disc3d/              disco 3D, muralha, anel de horas, mergulho, chão do Imersivo
│  │  ├─ globe/               sistema solar, Terra, planetas e Lua nítidos, céu de fundo
│  │  └─ tiles/               blocos de satélite: cache, seleção (globo e disco), fontes e créditos
│  ├─ weather/                previsão local, grade global de nuvens, cobertura para o WebGL
│  ├─ live/                   satélites (TLE + SGP4) e aviões (ADS-B)
│  ├─ sensors/                GPS, giroscópio, bússola, calibração, câmera AR
│  ├─ ui/
│  │  ├─ dom.js               atalhos de acesso à página
│  │  ├─ gestures.js          toque, pinça, roda do mouse (por área: céu, disco, globo, mergulho)
│  │  ├─ menu.js, panels.js, sim-sheet.js, mini-player.js, info-card.js, toast.js
│  │  ├─ model-switch.js      Disco | Globo, Lado a lado, Centro, Nuvens
│  │  └─ recording.js         gravação de vídeo com áudio
│  ├─ i18n/pt-BR.js           todos os textos da interface num só lugar
│  └─ styles/                 base.css, topo.css, menu.css, fichas.css, cartoes.css
├─ sw/                        service worker (gerado na publicação, com a lista de arquivos da versão)
├─ tools/                     scripts Python que geram os dados (como hoje)
├─ tests/
│  ├─ unit/                   cálculos astronômicos (Vitest)
│  └─ e2e/                    navegação e capturas de tela (Playwright)
├─ docs/                      este documento e as decisões de arquitetura
└─ .github/workflows/         construir, testar e publicar
```

### De onde vem cada parte (seções atuais do `index.html`)

| Seção atual | Tamanho | Destino |
|---|---|---|
| Efemérides, Estrelas principais, Cálculo dos objetos | ~4 KB | `astro/` |
| Catálogo (d3-celestial / Hipparcos) e planetas | ~5 KB | `data/catalog.js` + `astro/planets.js` |
| Estado, Canvas, Câmera | ~5 KB | `app/state.js`, `render/sky/camera.js` |
| Eclipses, Próximas fases, Marés | ~9 KB | `astro/eclipses.js`, `astro/moon.js`, `astro/tides.js` |
| Cores do céu, Desenho, Paisagem, Sol e Lua com realismo | ~29 KB | `render/sky/` |
| Arte das constelações | ~1 KB | `data/art.js` + `render/sky/art.js` |
| Vista do disco (de fora) | ~16 KB | `render/disc2d/` |
| Satélites e aviões | ~12 KB | `live/` |
| Rastros | ~1 KB | `render/sky/trails.js` |
| Textos (fichas de informação) | ~9 KB | `ui/info-card.js` + `i18n/` |
| Sensores e GPS; Câmera e calibração pelo céu | ~22 KB | `sensors/` |
| Cidades: busca e nome do local; Cidades por zoom | ~3 KB | `data/cities.js` + `render/labels-cities.js` |
| Controles | ~12 KB | `ui/` (menu, fichas, gestos) |
| Disco seguindo o observador | ~2 KB | `render/disc2d/follow.js` |
| Motor 3D, Chão do Imersivo, Mergulho | ~26 KB | `render/gl/` + `render/disc3d/` |
| Forma da Terra, Disco em 3D | ~22 KB | `render/disc3d/` + `ui/model-switch.js` |
| Nuvens do mundo todo; Tempo e nuvens | ~8 KB | `weather/` |
| Modelo Globo, Terra detalhada, Satélite no disco | ~38 KB | `render/globe/` + `render/tiles/` |
| Zodíaco e caminhos do dia | ~2 KB | `render/sky/zodiac.js` |
| Gravação de vídeo | ~4 KB | `ui/recording.js` |
| Laço | ~4 KB | `app/loop.js` + `main.js` |

## 4. Regras da nova estrutura

1. **`astro/` não desenha nada.** Recebe data e lugar e devolve números. É a parte mais valiosa e a mais fácil de testar.
2. **Estado em um lugar só** (`app/state.js`). Os módulos leem e alteram o estado por funções com nome claro, por exemplo `setMode("sky")` e `setLayer("wx", true)`, e não por variáveis soltas.
3. **Desenho não decide regra.** Os módulos de `render/` só desenham o que o estado diz. As decisões (qual modo, qual zoom, qual camada) ficam em `app/` e `ui/`.
4. **Nada de texto solto no código.** Toda frase da interface fica em `i18n/pt-BR.js`. Isso facilita revisar a escrita e, um dia, traduzir.
5. **Nomes que se explicam.** Por exemplo, `svEarthGL` vira `drawEarthGlobe` e `etSelectDisc` vira `selectDiscTiles`. A troca acontece no momento em que cada parte é mudada de lugar.
6. **As chaves salvas no aparelho não mudam** (`planetarium-cal`, `-curva`, `-disco3d`, `-escala-real`, `-estilo`, `-follow`, `-proxy`, `-simhint`, `-wx`). Assim ninguém perde calibração nem preferências.
7. **Créditos e licenças junto da fonte.** O módulo das imagens de satélite contém as URLs e a atribuição; os dados continuam com seus arquivos `LICENSE-*`.

## 5. Como migrar sem quebrar nada

A migração acontece em fases curtas. Cada fase vai num branch próprio, é testada e só depois entra no `main`. O app publicado continua funcionando o tempo todo.

**Fase 0 — Rede de segurança** (antes de mover qualquer código)
- Transformar os testes manuais de hoje em testes automáticos: abrir cada modo, tocar nos botões principais e comparar capturas de tela. Usar hora fixa, imagens de satélite simuladas e tempo simulado, para o resultado não variar.
- Testes de números para o Sol, a Lua, os planetas, a declinação magnética e os eclipses, usando os valores já conferidos (por exemplo, os do WMM e a declinação de Muriaé).
- Montar a lista de verificação da seção 6.

**Fase 1 — Separar sem mudar**
- Copiar o CSS para `src/styles/` e o JavaScript para `src/legacy.js` (ainda um arquivo só) e ligar o Vite.
- Mover os dados para `public/`, gerar o service worker na publicação e configurar o GitHub Actions.
- Critério para seguir: o app publicado é idêntico, e todos os testes da Fase 0 passam.

**Fase 2 — Tirar os cálculos (`astro/`, `data/`)**
- São as partes mais independentes. Saem primeiro e já ganham testes próprios.

**Fase 3 — Estado e preferências (`app/`)**
- Criar `state.js` e `prefs.js` e trocar o acesso direto às variáveis globais por funções.

**Fase 4 — Interface (`ui/`, `i18n/`)**
- Menu, fichas, mini player, cartões, gestos e gravação.

**Fase 5 — Desenho (`render/`)**
- Uma área por vez: céu, disco 2D, motor 3D, disco 3D e mergulho, globo, blocos de satélite.
- Fazer o globo e os blocos de satélite por último: são as partes mais novas e com mais ligações.

**Fase 6 — Limpeza**
- Remover o `legacy.js` vazio, padronizar nomes e, se fizer sentido, começar o TypeScript por `astro/`.

Cada fase deve sair em uma versão publicada (por exemplo, 2026.12.x) e ficar um ou dois dias em uso antes da próxima.

## 6. Lista de verificação (nada pode se perder)

Céu e Imersivo: GPS, giroscópio e bússola; calibração e declinação magnética; câmera AR; constelações, desenhos e zodíaco; caminho do Sol e da Lua; paisagem e chão de satélite com olhar para baixo; Estrela Polar; nuvens do tempo real; gravação com áudio.

Disco: 2D e 3D; estilos mapa, Gleason, foto e pontos; satélite com zoom até as cidades; nomes e ruas; nuvens flutuando com sombra; anel de horas; cidades por zoom; seguir posição e direção; mergulho até o chão e volta; muralha de gelo; domo com estrelas.

Globo: sistema solar com escala didática e real; centro Terra, Sol, Lua e planeta tocado; Terra de satélite até 1,5 km; câmera presa à Terra; nuvens em camada; céu de fundo com distâncias; movimento na galáxia; planetas e Lua nítidos.

Nos dois modos: Disco | Globo; lado a lado e as três telas divididas; simulação (velocidades, ir para, um dia, um ano, fases, eclipses, comparar); marés e tábua; eclipses; previsão do tempo; atalho Nuvens.

Ao vivo e tela: satélites, Starlink e aviões; tela deitada; funcionamento offline; preferências salvas.

## 7. Cuidados

- **Service worker:** com nomes de arquivo por versão, a lista de cache passa a ser gerada na publicação. Manter a regra atual: página e dados vêm primeiro da rede; o cache é usado só sem internet.
- **Endereço no GitHub Pages:** configurar o `base` do Vite para o caminho do repositório, senão imagens e dados não carregam.
- **Artefato do Claude:** passa a receber os arquivos de `dist/`, não mais o `index.html` da raiz.
- **WebGL no celular:** manter o limite de imagens e a recuperação de contexto. Num módulo próprio isso fica mais fácil de testar.
- **Desempenho:** a divisão não pode criar trabalho a mais por quadro. O laço continua único, e os módulos só exportam funções.

## 8. Próximo passo

Começar pela **Fase 0** (testes automáticos e lista de verificação), num branch próprio. Ela não muda nada para quem usa o app e é o que permite mover o código com segurança depois.
