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
