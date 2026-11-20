# Actualización anual y control de calidad

## Frecuencia

El conjunto de datos se actualiza **como máximo una vez al año**. No se requiere sincronización en tiempo real, backend ni base de datos en el equipo del usuario.

## Flujo de publicación

1. Registrar fecha de corte, origen y versión de datos.
2. Exportar desde PostgreSQL/PostGIS los nueve CSV de establecimientos.
3. Exportar solo los GeoJSON territoriales únicos necesarios.
4. Ejecutar controles de calidad y revisar excepciones.
5. Convertir las fuentes a archivos JavaScript locales consumibles desde `file://`.
6. Actualizar el catálogo con nombres y relaciones reales.
7. Ejecutar pruebas funcionales y visuales en navegadores objetivo.
8. Publicar una nueva carpeta `visor/` y documentar cambios.

## Controles de CSV

- Archivo presente, legible y UTF-8.
- Encabezados válidos y sin duplicados.
- Presencia de campos comunes acordados.
- Identificador de fila no nulo y único (según clave definida).
- Coordenadas numéricas, en orden lat/lon, dentro del ámbito esperado de CABA.
- Valores de `supervision` y `comuna` consistentes con el dominio de cada nivel.
- Conservación de todas las columnas y filas entre exportación y empaquetado.
- Conteo de filas, filas sin coordenadas y duplicados reportados por nivel.

## Controles de GeoJSON

- GeoJSON válido y geometrías Polygon/MultiPolygon.
- CRS de exportación WGS84 (EPSG:4326), como exige GeoJSON moderno.
- Identificadores territoriales válidos y no duplicados dentro de la división.
- Geometrías válidas, límites esperados y ausencia de errores relevantes.
- Correspondencia documentada entre campos territoriales y filtros de CSV, si se habilita clic para filtrar.

## Controles de aplicación

- Abrir `visor/index.html` directamente sin servidor.
- Verificar nueve niveles y sus tablas completas.
- Verificar polígonos compartidos sin duplicación de archivos.
- Verificar scroll horizontal/vertical, filtros, selección, búsqueda y exportación.
- Verificar dependencia de Internet y mensajes de error cuando fallen los CDN o el mapa base.

## Registro de publicación (plantilla)

| Dato | Valor |
|---|---|
| Fecha de corte | Pendiente |
| Fecha de exportación | Pendiente |
| Responsable | Pendiente |
| Versión del visor | Pendiente |
| Versión del conjunto de datos | Pendiente |
| Total de registros por nivel | Pendiente |
| Total de polígonos por división | Pendiente |
| Incidencias conocidas | Pendiente |

## Reproducibilidad

Guardar las consultas SQL, parámetros de extracción, scripts de conversión y reportes de validación dentro del repositorio cuando se implementen. No guardar credenciales ni cadenas de conexión sensibles.
