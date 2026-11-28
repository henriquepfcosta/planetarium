# Criação · Gênesis 1

Experiência separada do Planetarium que desmonta o Disco 3D do app (o mesmo mapa, domo, estrelas, luminares e anel de horas) e o monta de novo, passo a passo, conforme Gênesis 1:1–2:3: as águas, a luz, o firmamento com as águas acima dele, a terra seca, os luminares, a vida e o descanso. No fim, abre o Disco 3D ao vivo, que é a estrutura completa do app.

## Onde fica

- Tela inicial: botão **Criação · Gênesis 1**, abaixo de "Explorar arrastando".
- Menu: seção **Experiências** → **Criação · Gênesis 1**.
- Ela usa o próprio Disco 3D: esconde os painéis do app, guarda as suas configurações e as devolve ao fechar. O estilo de mapa escolhido (mapa, foto, Gleason) é o que aparece montado.

## Controles

- Dias **1 a 7** no topo: pulam para o início de cada dia.
- **◀ ❚❚ ▶** no cartão: passo anterior, pausar/continuar a reprodução automática, próximo passo.
- Arrastar a cena gira o disco.
- No sétimo dia, **Ver a terra completa no disco, agora** fecha a experiência e abre o Disco 3D com o Sol, a Lua e as estrelas na posição de hoje.

## Roteiro (o que aparece em cada passo)

| Dia | Texto | O que é montado |
|---|---|---|
| 1 | 1:1 | O disco surge, ainda em trevas, coberto pelas águas |
| 1 | 1:2 | Abismo (*tehom*) e a névoa do Espírito pairando sobre as águas (sem figura) |
| 1 | 1:3 | Luz sem fonte, antes dos luminares |
| 1 | 1:4–5 | Luz e trevas separadas, girando: tarde e manhã |
| 2 | 1:6–8 | O firmamento (*raqia*) sobe do meio das águas e leva as águas de cima; ficam as águas de baixo; o firmamento é chamado Céu |
| 3 | 1:9–10 | As águas se ajuntam, aparece a porção seca; Terra e Mares; borda de gelo |
| 3 | 1:11–13 | A terra seca ganha vegetação (do tom seco ao verde) |
| 4 | 1:14–19 | Os luminares descem do alto do firmamento aos seus caminhos; as estrelas acendem no domo; a luz passa a seguir o luminar maior; aparecem os sinais: anel de horas (dias), trópicos (estações) |
| 5 | 1:20–23 | Seres das águas e aves pela face do firmamento |
| 6 | 1:24–31 | Animais da terra; homem e mulher, em silhuetas simples |
| 7 | 2:1–3 | Descanso; botão para o disco ao vivo |

## Como editar o texto ou o roteiro

Tudo fica em `criacao.json`, sem precisar mexer no código:

- `texto`: o versículo exibido. O texto atual é uma tradução livre a partir do hebraico, feita para esta simulação; pode ser trocado pela tradução de sua preferência (respeitando a licença dela). Escolha de tradução: "os céus" (plural) em 1:1 e 2:1, para a criação inteira; "Céu" (singular) para o firmamento em 1:8 e nas expressões ligadas a ele (1:9, 1:14, 1:17, 1:20), deixando claro que o firmamento é um céu dentro dos céus criados. No hebraico as duas formas são a mesma palavra, *shamayim*.
- `ref`: a referência mostrada no cartão.
- `cena`: o que é montado no passo. Cada chave vai de 0 (ausente) a 1 (completo) e vale dali em diante: `forma`, `escuro`, `abismo`, `espirito`, `luz`, `separa`, `ciclo`, `firmamento`, `acima`, `terra`, `gelo`, `verde`, `luminares`, `estrelas`, `sol`, `sinais`, `peixes`, `aves`, `animais`, `pessoas`, `descanso`.
- `rotulos`: etiquetas mostradas na cena (por exemplo `firmamento`, `acima`, `debaixo`, `maior`, `menor`).
- `fim: true` no último passo mostra o botão que abre o disco ao vivo.

## Águas acima do firmamento no Disco 3D

Além da experiência, o Disco 3D ganhou a camada opcional **Águas acima do firmamento** (menu, seção do Disco): uma casca de água translúcida por cima do domo, com movimento lento, que deixa ver as estrelas, o Sol e a Lua através dela.

## Para a reorganização das pastas

Quando o código for dividido (ver `docs/ARQUITETURA.md`), esta experiência vira um módulo próprio, por exemplo `src/experiences/criacao/`, com o roteiro em `public/data/criacao.json`.
