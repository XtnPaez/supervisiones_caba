# Arquitectura

- **Interfaz:** HTML5, CSS3, JavaScript sin framework de compilación.
- **Cartografía:** Leaflet 1.9.4 vía CDN, teselas de OpenStreetMap.
- **Fuentes:** CSV y GeoJSON originales en `fuentes/`.
- **Distribución:** los archivos fuente se convierten en asignaciones JS globales `window.ATLAS_DATA` y `window.ATLAS_TERR` para evitar restricciones CORS al abrir `file://`.
- **Estado:** filtros combinados de nivel, texto, comuna, supervisión y polígono seleccionado; tabla, puntos y exportación reflejan el mismo subconjunto.
- **Tabla:** paginación, ordenamiento por columna, scroll vertical y horizontal.
- **Ficha:** presenta todos los atributos del registro, sin esquema rígido.
- **Sin backend:** no se envían consultas a un servidor propio. El CDN y el mapa base sí necesitan conexión.
