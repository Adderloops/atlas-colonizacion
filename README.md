# Atlas de Colonización

Personal Elite Dangerous colonisation search tool, powered by the [Spansh](https://spansh.co.uk) API.

Herramienta personal para buscar sistemas candidatos de colonización.

- **Sistemas:** sin colonizar, cerca de tu sistema ancla, ordenados con pesos ajustables (ELW, mundos acuáticos, anillos, señales bio/geo…). Favoritos y exportación a CSV.
- **Cuerpos y recursos:** filtros por tipo de cuerpo, anillos, señales y distancia de llegada.
- **Logística:** proveedores de mercancías de construcción en el radio de búsqueda.

## Uso

- Abre `index.html` (o la página de GitHub Pages) y escribe tu sistema de referencia.
- Si el navegador bloquea la conexión con Spansh (CORS), ejecuta `python server.py` y abre http://localhost:8765. El servidor reenvía las peticiones a Spansh.
- «Datos de ejemplo» muestra la interfaz con datos inventados.
- El bloque «Diagnóstico» del estado muestra la petición enviada y los campos que devuelve Spansh.

## Proxy gratuito para GitHub Pages (Cloudflare Worker)

Spansh no permite peticiones directas desde otros dominios, así que la página publicada necesita un proxy.

1. Entra en [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers & Pages** → **Create** → **Create Worker**.
2. Ponle un nombre (por ejemplo `atlas-spansh`), pulsa **Deploy**, luego **Edit code**, pega el contenido de `worker.js` y despliega.
3. Copia la URL del worker (`https://atlas-spansh.<tu-subdominio>.workers.dev`).
4. En la página, en **Conexión → URL base de la API**, escribe esa URL con `/api` al final: `https://atlas-spansh.<tu-subdominio>.workers.dev/api`. Se queda guardada en el navegador.

El worker solo acepta peticiones desde `https://adderloops.github.io` y `http://localhost:8765`, y solo reenvía las rutas de búsqueda de sistemas.
