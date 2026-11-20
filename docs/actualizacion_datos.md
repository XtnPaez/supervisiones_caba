# Actualización y publicación

1. Exportar las nueve consultas desde PostgreSQL/PostGIS en CSV UTF-8, con encabezados y coordenadas WGS84.
2. Exportar las siete capas GeoJSON; conservar sus nombres de archivo.
3. Sustituir los archivos de `fuentes/csv/` y `fuentes/geojson/`.
4. Ejecutar `python scripts/preparar_datos.py` desde la raíz o desde otra ubicación.
5. Abrir `distribucion/index.html`, comprobar cada nivel, filtros, tabla, polígonos, fichas y exportación.
6. Publicar la carpeta `distribucion/` y, si se desea, generar un ZIP de su contenido.

Controles recomendados: unicidad de CUE por archivo, lat/lon válidas, comunas 1–15, supervisiones coincidentes, geometrías válidas, puntos fuera de polígonos y valores nulos. El script avisa coordenadas inválidas y las omite; no sustituye una validación geoespacial formal.

## Publicación y control de versión

La versión de interfaz documentada es **v1.2**. El nombre visible y el pie institucional están en `distribucion/index.html`; el mapa base oficial CABA se configura en `distribucion/js/app.js`. Después de regenerar datos, comprobar que el listado inferior se vea, que la ficha cierre y que el CSV exporte todos los resultados filtrados.
