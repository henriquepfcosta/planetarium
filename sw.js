const CACHE = "planetarium-v11";
const CORE = ["./", "index.html", "manifest.webmanifest", "icon-192.png", "icon-512.png", "sky.json", "art.json", "cidades-br.json", "terra/dia.jpg", "terra/noite.jpg", "lib/satellite.min.js"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE))); self.skipWaiting(); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
// Rede primeiro para a página e os dados (sempre a versão mais nova), cache como reserva offline.
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  const url = new URL(e.request.url);
  const same = url.origin === location.origin, fonts = /fonts\.(googleapis|gstatic)\.com$/.test(url.hostname);
  if (!same && !fonts) return;
  const put = res => { if (res.ok || res.type === "opaque") { const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); } return res; };
  const isImage = /\.(webp|png|jpg)$/.test(url.pathname) || fonts;
  e.respondWith(isImage
    ? caches.match(e.request).then(hit => hit || fetch(e.request).then(put))
    : fetch(e.request).then(put).catch(() => caches.match(e.request)));
});
