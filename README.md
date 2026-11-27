# Planetarium

O céu ao vivo em duas visões:

- **Céu (imersivo):** o céu visto do chão, guiado pelo GPS, pelo giroscópio e pela bússola do celular. Mostra cerca de 5.000 estrelas visíveis a olho nu, as 88 constelações com nomes em português e desenhos, a Via Láctea, o Sol, a Lua com a fase e os planetas, sobre uma paisagem com colinas e árvores.
- **Disco 3D (de fora):** o disco com o Polo Norte no centro e o sul na borda, com foto de satélite real, dia e noite projetados com as luzes das cidades, o Sol, a Lua, os planetas, os satélites e o firmamento girando no domo. Câmera livre: girar, inclinar, aproximar e mover.

Nas duas visões aparecem juntos o **céu observado** (posições calculadas por efemérides) e o **modelo do disco** (onde um Sol e uma Lua locais, na altura escolhida, apareceriam do ponto do observador), para comparar no campo.

## Satélites e aviões

- **Satélites:** órbitas do CelesTrak (estações espaciais, os mais brilhantes e, opcionalmente, Starlink), calculadas no próprio aparelho com SGP4. O app busca os dados direto no CelesTrak (ou em `dados/tle-<grupo>.txt`, se existir no site).
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
- Foto da Terra e luzes noturnas: NASA Blue Marble e Black Marble (domínio público), reprojetadas para o disco (`terra/`). Arquivos de origem obtidos do repositório [three-globe](https://github.com/vasturiano/three-globe).
- Cálculo de órbitas: [satellite.js](https://github.com/shashwatak/satellite-js) (MIT), em `lib/`. Dados orbitais: [CelesTrak](https://celestrak.org).
- Aviões: [adsb.fi](https://adsb.fi), [adsb.lol](https://adsb.lol), [airplanes.live](https://airplanes.live) e [OpenSky Network](https://opensky-network.org).
- Desenhos das constelações: ilustrações de Johan Meuris, do projeto [Stellarium sky cultures](https://github.com/Stellarium/stellarium-skycultures) (cultura ocidental), sob a [Free Art License](https://artlibre.org/licence/lal/en/). Os dados de âncoras são CC BY-SA.
- Municípios do Brasil: [kelvins/municipios-brasileiros](https://github.com/kelvins/municipios-brasileiros) (MIT).
- Sol: algoritmo da NOAA. Lua: método simplificado de Paul Schlyter.
- `sky.json` é gerado a partir de `d3-celestial/data` (estrelas até magnitude 6).
