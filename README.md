# Planetarium

O céu ao vivo em duas visões:

- **Céu (imersivo):** o céu visto do chão, guiado pelo GPS, pelo giroscópio e pela bússola do celular. Mostra cerca de 5.000 estrelas visíveis a olho nu, as 88 constelações com nomes em português, a Via Láctea, o Sol, a Lua com a fase e os planetas.
- **Disco (de fora):** o mapa com o Polo Norte no centro e o sul na borda, com o dia e a noite projetados e o Sol, a Lua e os planetas sobre os pontos onde estão a pino.

Nas duas visões aparecem juntos o **céu observado** (posições calculadas por efemérides) e o **modelo do disco** (onde um Sol e uma Lua locais, na altura escolhida, apareceriam do ponto do observador), para comparar no campo.

## Rodar

É um site estático, sem build. Sirva a pasta por HTTPS (exigido para GPS e sensores):

- **GitHub Pages:** Settings → Pages → Branch `main` / pasta raiz.
- **Vercel / Netlify:** importe o repositório, sem configuração.
- **Local:** `python3 -m http.server` e abra `http://localhost:8000`.

No celular, use "Adicionar à tela inicial" para abrir como app (PWA, funciona offline depois da primeira visita).

## Dados e créditos

- Estrelas, constelações, Via Láctea e elementos orbitais: [d3-celestial](https://github.com/ofrohn/d3-celestial) de Olaf Frohn (licença BSD-3), com base no catálogo Hipparcos e nos elementos keplerianos aproximados do JPL.
- Sol: algoritmo da NOAA. Lua: método simplificado de Paul Schlyter.
- `sky.json` é gerado a partir de `d3-celestial/data` (estrelas até magnitude 6).
