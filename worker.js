// Cloudflare Worker: proxy CORS mínimo para la API de Spansh.
// Solo acepta peticiones desde los orígenes permitidos y solo reenvía
// las rutas de búsqueda de sistemas/estaciones y lectura de sistemas.
const ALLOWED_ORIGINS = [
  "https://adderloops.github.io",
  "http://localhost:8765",
];
const ALLOWED_PATHS = [/^\/api\/systems\/search$/, /^\/api\/stations\/search$/, /^\/api\/system\/\d+$/];

export default {
  async fetch(req) {
    const origin = req.headers.get("Origin") || "";
    if (!ALLOWED_ORIGINS.includes(origin)) {
      return new Response("Forbidden", { status: 403 });
    }
    const cors = {
      "Access-Control-Allow-Origin": origin,
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Vary": "Origin",
    };
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });

    const url = new URL(req.url);
    if (!ALLOWED_PATHS.some((re) => re.test(url.pathname))) {
      return new Response("Not found", { status: 404, headers: cors });
    }
    const upstream = await fetch("https://spansh.co.uk" + url.pathname + url.search, {
      method: req.method,
      headers: { "Content-Type": "application/json", "User-Agent": "AtlasColonizacionPersonal/1.0" },
      body: req.method === "POST" ? await req.text() : undefined,
    });
    return new Response(upstream.body, {
      status: upstream.status,
      headers: { ...cors, "Content-Type": upstream.headers.get("Content-Type") || "application/json" },
    });
  },
};
