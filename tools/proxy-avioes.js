// Proxy opcional para o radar de aviões do Planetarium (Cloudflare Workers, plano gratuito).
// Uso: crie um Worker em dash.cloudflare.com, cole este código, publique e cole o endereço
// (https://<nome>.<conta>.workers.dev) no app em Local e modelo > Radar de aviões.
export default {
  async fetch(req) {
    const cors = { "access-control-allow-origin": "*", "content-type": "application/json", "cache-control": "max-age=5" };
    const u = new URL(req.url);
    const lat = Number(u.searchParams.get("lat")), lon = Number(u.searchParams.get("lon"));
    const dist = Math.min(250, Math.max(1, Number(u.searchParams.get("dist")) || 250));
    if (!Number.isFinite(lat) || !Number.isFinite(lon) || Math.abs(lat) > 90 || Math.abs(lon) > 180)
      return new Response('{"erro":"lat/lon inválidos"}', { status: 400, headers: cors });
    const fontes = [
      `https://opendata.adsb.fi/api/v3/lat/${lat}/lon/${lon}/dist/${dist}`,
      `https://api.adsb.lol/v2/point/${lat}/${lon}/${dist}`,
      `https://api.airplanes.live/v2/point/${lat}/${lon}/${dist}`,
    ];
    for (const f of fontes) {
      try {
        const r = await fetch(f, { headers: { "user-agent": "Planetarium (proxy pessoal)" } });
        if (r.ok) return new Response(await r.text(), { headers: cors });
      } catch (e) {}
    }
    return new Response('{"ac":[]}', { status: 502, headers: cors });
  },
};
