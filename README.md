# Planetarium

O céu ao vivo em duas visões:

- **Céu (imersivo):** o céu visto do chão, guiado pelo GPS, pelo giroscópio e pela bússola do celular. Mostra cerca de 5.000 estrelas visíveis a olho nu, as 88 constelações com nomes em português e desenhos, a Via Láctea, o Sol, a Lua com a fase e os planetas, sobre uma paisagem com colinas e árvores.
- **Disco 3D (de fora):** o disco com o Polo Norte no centro e o sul na borda, com foto de satélite real, dia e noite projetados com as luzes das cidades, o Sol, a Lua, os planetas, os satélites e o firmamento girando no domo. Câmera livre: girar, inclinar, aproximar e mover.

Nas duas visões aparecem juntos o **céu observado** (posições calculadas por efemérides) e o **modelo do disco** (onde um Sol e uma Lua locais, na altura escolhida, apareceriam do ponto do observador), para comparar no campo.

## Simulação

Toque no relógio para abrir a barra de simulação: tocar/pausar, régua das 24 horas, velocidades, atalhos (nascer e pôr do Sol, meio-dia, meia-noite), simulações prontas (um dia, uma noite, um ano no mesmo horário), rastros do Sol, da Lua e das estrelas, e tela dividida com o Disco 3D e o Imersivo ao mesmo tempo, sincronizados.

## Eclipses, Estrela Polar e anel de horas

- **Eclipses:** o app procura os próximos eclipses do Sol e da Lua a partir das posições calculadas (conferido com o catálogo da NASA para 2026–2027), diz se cada um é visível do seu local e permite simular daqui ou do centro da sombra. Durante a simulação, a Lua cobre o Sol no Imersivo, o céu escurece conforme a cobertura e a sombra aparece no Disco 3D; no eclipse da Lua, ela fica avermelhada.
- **Estrela Polar:** marcada no centro do domo do Disco 3D e no céu do Imersivo; abaixo do horizonte, o app mostra quantos graus.
- **Anel de horas (inspirado no mapa de Gleason, 1892):** horas solares em algarismos romanos em volta do disco, girando com o Sol (XII dourado = meio-dia); graus de latitude e longitude na grade e escala de distância ao longo dos meridianos. Estilo de mapa “Gleason 1892” gerado por `tools/gleason.py`.

## Mergulho: do disco ao chão

- **Ícone do canto superior direito:** troca entre o Imersivo e o Disco 3D com a viagem animada (subida ou descida, cerca de 5 s). Tocando de novo durante a viagem, ela inverte o sentido.
- **Pinça no disco** além do zoom máximo (ou **Descer até meu local**, no menu do disco): a câmera desce pelo domo até o seu local, em 3D (WebGL). Acima do domo você vê o disco e as constelações; sob o domo, o mapa em perspectiva embaixo, o domo com as estrelas em cima e o Sol e a Lua do modelo a 5.000 km.
- Perto do chão, as estrelas, o Sol e a Lua deslizam das posições do domo (modelo) para as posições observadas; o painel lateral mostra a altitude e qual céu está sendo mostrado.
- A descida é um movimento único: a câmera 3D começa exatamente na vista do disco e, perto do chão, a imagem já se torna a do Imersivo, sem corte.
- Abaixo de 2 m você pousa no Imersivo; pinça para fora no Imersivo (ou **Subir até o disco**) faz o caminho inverso. Botões ▲ ▼, **Pousar** e **Disco** no painel lateral.
- Com as nuvens ligadas, a camada de nuvens prevista aparece vista de cima e você atravessa a neblina por volta de 2 km.

## Cidades no mapa

- **Cidades no mapa** (menu, Disco 3D): como num mapa on-line, os nomes aparecem conforme o zoom; primeiro as grandes cidades e capitais do mundo, depois as regionais, com a distância até você quando perto. Funciona no disco e no mergulho, sem nomes sobrepostos.
- Dados: Natural Earth (domínio público), gerados por `tools/cidades-mundo.py`.

## Chão do Imersivo

- **Chão com o mapa** (menu, Céu): o chão usa o mesmo mapa do disco, em perspectiva, com dia e noite, e uma rosa dos ventos pintada no chão. No horizonte aparecem cidades próximas na direção certa, com a distância real.

## Disco seguindo você

- **Seguir minha posição e direção** (menu, Disco 3D, ligado por padrão): ao abrir o disco, ele se aproxima do seu local e gira para que a frente seja para onde você olha no Imersivo; com os sensores ligados, gira junto com o celular. Um leque dourado mostra o seu campo de visão sobre o mapa.
- Arrastar para os lados libera o disco (modo livre); inclinar e aproximar continuam seguindo. Centralizar também desliga o seguir.

## Alinhamento com o céu real

- **Norte verdadeiro:** a bússola do celular aponta para o norte magnético. O app corrige a declinação magnética do seu local com o modelo WMM2025 da NOAA (em Muriaé, cerca de 23° para oeste).
- **Modo alinhado:** com os sensores ligados, o centro da tela é exatamente para onde o celular aponta, com campo de visão próximo ao da câmera.
- **Calibrar pelo céu** (menu, modo Imersivo): abre a câmera com o céu desenhado por cima. Ponha o Sol, a Lua, Vênus ou uma estrela brilhante no centro e toque em Alinhar; com o Sol e a Lua, o app tenta encontrá-los sozinho na imagem. A correção fica salva e pode ser desfeita.
- **Câmera ao fundo:** mostra a imagem da câmera atrás do céu desenhado.

## Observação com a câmera, zodíaco e gravação

- **Câmera ao fundo:** a imagem real da câmera fica atrás do céu desenhado, e as constelações, os desenhos, as estrelas e os nomes aparecem mesmo de dia, como um "raio X" do céu.
- **Zodíaco e eclíptica:** o caminho do Sol entre as estrelas, com os 12 signos (setores de 30° a partir do equinócio). As fichas do Sol, da Lua e dos planetas mostram o signo em que estão.
- **Caminho do Sol e da Lua:** a trajetória do dia no céu, com as horas marcadas.
- **Gravar vídeo** (menu, seção Tela): grava a câmera, o céu e a simulação sem os menus, com local, data e hora no canto; no fim, salve ou compartilhe (MP4 no iPhone).

## Tempo e nuvens

- **Nuvens do tempo real:** no Imersivo, nuvens desenhadas conforme a cobertura prevista para o local e a hora simulada, andando com o vento (dados Open-Meteo, CC BY 4.0). O formato das nuvens é ilustrativo; a quantidade, a altura (baixas, médias, altas) e o vento vêm da previsão.
- **Previsão do tempo:** condições na hora simulada, nuvens das próximas 48 horas e as próximas noites boas para observar.

## Teste da curvatura

- **Teste da curvatura** (menu, nos dois modos): um controle de curvatura do disco, começando no valor medido (1° a cada 111,2 km, das medições de Eratóstenes, al-Biruni, das expedições do século XVIII e do Arco de Struve até o GPS) e ajustável de 0% (plano) a 150%.
- Mostra o perfil norte–sul em corte e, para várias cidades (de Reykjavík a Ushuaia, mais o seu local), a altura observada dos polos celestes comparada com a prevista; escolha entre estrelas muito distantes ou no domo. **Melhor ajuste** procura a curvatura que mais se aproxima do observado.

## Disco em 3D

- **Disco em 3D (forma e muralha)** (menu, Disco 3D) ou **Ver esta forma no Disco 3D** (no Teste da curvatura): o disco passa a ser desenhado em 3D de verdade, com espessura de rocha, muralha de gelo na borda e a forma escolhida no Teste da curvatura: plano (0%), convexo (centro mais alto, até fechar numa esfera em 100%) ou côncavo (bordas mais altas, valores negativos). A forma muda ao vivo ao mexer no controle.
- Com estrelas "muito distantes" o céu fica ao fundo; com "no domo", as estrelas ficam no domo do modelo. Espessura e muralha são ilustrativas.
- Ao descer para o seu local a partir de um disco curvado, ele volta a ficar plano antes do mergulho.

## Marés

- **Marés** (menu, nos dois modos): calcula a maré astronômica de equilíbrio pelas posições reais da Lua e do Sol. No Disco 3D, o oceano fica azul onde a água se acumula (maré alta) e cor de areia onde baixa, com as duas regiões de maré alta marcadas: sob a Lua e do lado oposto.
- **Tábua de marés:** curva das 24 horas no seu local, horários de maré alta e baixa, aviso de sizígia (marés vivas) e quadratura (marés mortas) e o botão Simular o dia.
- É o ritmo teórico; no litoral real a altura é maior e os horários atrasam algumas horas conforme o porto.

## Menu e tela

- O Sol e a Lua do modelo aparecem como marcas coral discretas no imersivo; toque no Sol ou na Lua para ver a linha até a marca e a diferença em graus.
- O menu de camadas abre como uma lista na lateral esquerda, com uma chave liga/desliga em cada item; no Disco 3D o disco se desloca para a direita enquanto o menu está aberto.
- **Tela deitada:** a barra de simulação e as fichas (eclipses, marés, data, local) passam para uma coluna à direita e o disco se desloca para o lado, sem cobrir o mapa.
- **Lua no topo:** ícone maior com a fase escrita ao lado (por exemplo, "Lua cheia · 100%"); toque para ver as próximas fases.
- **Tela deitada:** gire o celular (ou use o item do menu) para ver em paisagem. No Android o app trava a tela deitada em tela cheia; no iPhone basta girar com o bloqueio de rotação desligado.

## Satélites e aviões

- **Satélites:** começam desligados; os dados só são baixados quando você liga a camada. Órbitas do CelesTrak (estações espaciais, os mais brilhantes e, opcionalmente, Starlink), calculadas no próprio aparelho com SGP4. O app busca os dados direto no CelesTrak (ou em `dados/tle-<grupo>.txt`, se existir no site).
- **Aviões:** posições ao vivo de radar ADS-B num raio de cerca de 460 km do observador, tentando adsb.fi, adsb.lol, airplanes.live e OpenSky, nesta ordem. Se todos bloquearem o acesso pelo navegador, publique `tools/proxy-avioes.js` como Cloudflare Worker (gratuito) e cole o endereço no app em Local e modelo > Radar de aviões.

## Local

Ao abrir, o app usa o GPS (se a permissão já foi dada) e mostra o nome da cidade. A busca encontra qualquer cidade: os 5.570 municípios do Brasil funcionam offline, e o resto do mundo vem do serviço gratuito de geocodificação do Open-Meteo. O nome do local fora do Brasil vem do OpenStreetMap (Nominatim).

## Rodar

É um site estático, sem build. Sirva a pasta por HTTPS (exigido para GPS e sensores):

- **GitHub Pages:** Settings → Pages → Branch `main` / pasta raiz.
- **Vercel / Netlify:** importe o repositório, sem configuração.
- **Local:** `python3 -m http.server` e abra `http://localhost:8000`.

No celular, use "Adicionar à tela inicial" para abrir como app (PWA, funciona offline depois da primeira visita).

## Dados e créditos

- Estrelas, constelações, Via Láctea e elementos orbitais: [d3-celestial](https://github.com/ofrohn/d3-celestial) de Olaf Frohn (licença BSD-3), com base no catálogo Hipparcos e nos elementos keplerianos aproximados do JPL.
- Mapa estilizado (`terra/mapa.jpg`): gerado por `tools/mapa.py` a partir da NASA Blue Marble, da máscara de água e do relevo (topografia) do repositório three-globe, com sombreamento de relevo, oceano limpo e borda de gelo.
- Foto da Terra e luzes noturnas: NASA Blue Marble e Black Marble (domínio público), reprojetadas para o disco (`terra/`). Arquivos de origem obtidos do repositório [three-globe](https://github.com/vasturiano/three-globe).
- Foto da Lua: textura lunar dos exemplos do [three.js](https://github.com/mrdoob/three.js) (MIT), reprojetada para a face visível (`terra/lua.webp`).
- Cálculo de órbitas: [satellite.js](https://github.com/shashwatak/satellite-js) (MIT), em `lib/`. Dados orbitais: [CelesTrak](https://celestrak.org).
- Aviões: [adsb.fi](https://adsb.fi), [adsb.lol](https://adsb.lol), [airplanes.live](https://airplanes.live) e [OpenSky Network](https://opensky-network.org).
- Desenhos das constelações: ilustrações de Johan Meuris, do projeto [Stellarium sky cultures](https://github.com/Stellarium/stellarium-skycultures) (cultura ocidental), sob a [Free Art License](https://artlibre.org/licence/lal/en/). Os dados de âncoras são CC BY-SA.
- Municípios do Brasil: [kelvins/municipios-brasileiros](https://github.com/kelvins/municipios-brasileiros) (MIT).
- Sol: algoritmo da NOAA. Lua: método simplificado de Paul Schlyter.
- `sky.json` é gerado a partir de `d3-celestial/data` (estrelas até magnitude 6).
