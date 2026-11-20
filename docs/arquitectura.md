# Arquitectura

## Componentes

- HTML5, CSS3 y JavaScript sin framework de compilación.
- Leaflet 1.9.4 cargado desde CDN.
- Mapa base oficial de CABA, servido desde GeoServer/GeoWebCache mediante TMS, con URL `{z}/{x}/{-y}`.
- CSV y GeoJSON originales almacenados en `fuentes/`.
- Archivos JavaScript generados en `distribucion/data/`, asignados a variables globales para admitir apertura por `file://`.
- No requiere backend propio, base de datos ni servidor local; sí conexión para Leaflet y teselas.

## Estructura de la aplicación

- `distribucion/index.html`: estructura de la interfaz, título **Supervisiones CABA** y pie institucional.
- `distribucion/css/estilos.css`: estilos, disposición del mapa, tabla inferior y ficha.
- `distribucion/js/catalogo.js`: catálogo de niveles y capas.
- `distribucion/js/app.js`: inicialización del mapa, filtros, tabla, ficha, exportación y capa base.
- `distribucion/data/`: establecimientos y territorios precargados en JavaScript.

## Comportamiento

Los filtros por nivel, texto, comuna, supervisión y polígono seleccionado determinan el subconjunto mostrado en mapa y tabla. La exportación CSV utiliza ese mismo subconjunto. La ficha de un establecimiento se abre desde el punto o la fila y puede cerrarse mediante botón o `Esc`.

La tabla tiene desplazamiento horizontal y vertical, encabezados ordenables y paginación. La exportación CSV incluye todas las filas filtradas y todas las columnas del nivel.

La selección de polígonos se resuelve espacialmente con las geometrías, no mediante igualdad de nombres.
