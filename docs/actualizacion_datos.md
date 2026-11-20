# Actualización y publicación

1. Exportar las nueve consultas desde PostgreSQL/PostGIS en CSV UTF-8, con encabezados y coordenadas WGS84.
2. Exportar las siete capas GeoJSON; conservar sus nombres de archivo.
3. Sustituir los archivos de `fuentes/csv/` y `fuentes/geojson/`.
4. Ejecutar `python scripts/preparar_datos.py` desde la raíz o desde otra ubicación.
5. Abrir `distribucion/index.html`, comprobar cada nivel, filtros, tabla, polígonos, fichas y exportación.
6. Publicar la carpeta `distribucion/` y, si se desea, generar un ZIP de su contenido.

Controles recomendados: unicidad de CUE por archivo, lat/lon válidas, comunas 1–15, supervisiones coincidentes, geometrías válidas, puntos fuera de polígonos y valores nulos. El script avisa coordenadas inválidas y las omite; no sustituye una validación geoespacial formal.
