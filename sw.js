const VERSION = "2026.11.27-8";
const CACHE = "planetarium-" + VERSION;
const CORE = ["./", "index.html", "manifest.webmanifest", "icon-192.png", "icon-512.png", "sky.json", "art.json", "cidades-br.json", "terra/mapa.jpg", "terra/gleason.jpg", "terra/dia.jpg", "terra/noite.jpg", "terra/lua.webp", "lib/satellite.min.js"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE.map(u => new Request(u, { cache: "reload" }))))); self.skipWaiting(); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
// Página e dados: sempre a versão mais nova da rede (ignorando cópias antigas), cache só sem internet.
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  const url = new URL(e.request.url);
  const same = url.origin === location.origin, fonts = /fonts\.(googleapis|gstatic)\.com$/.test(url.hostname);
  if (!same && !fonts) return;
  const put = res => { if (res.ok || res.type === "opaque") { const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); } return res; };
  const isImage = /\.(webp|png|jpg)$/.test(url.pathname) || fonts;
  e.respondWith(isImage
    ? caches.match(e.request).then(hit => hit || fetch(e.request).then(put))
    : fetch(e.request, { cache: "no-cache" }).then(put).catch(() => caches.match(e.request)));
});
