# Contrato de datos

## Regla central

**Los CSV no comparten un esquema completo.** Cada nivel exporta sus atributos educativos propios. Solo se estandarizan los campos necesarios para que el motor funcione.

## Campos comunes propuestos

| Campo lógico | Necesidad | Uso |
|---|---|---|
| `id` o clave equivalente | Obligatorio; nombre por definir | Identificar cada fila sin ambigüedad |
| `nombre` | Obligatorio | Etiqueta, búsqueda, ficha |
| `direccion` | Recomendado | Tabla, búsqueda, ficha |
| `lat` | Obligatorio para dibujar | Latitud WGS84, EPSG:4326 |
| `lon` | Obligatorio para dibujar | Longitud WGS84, EPSG:4326 |
| `supervision` | Columna común acordada | Visualización y filtro; puede no aplicar territorialmente a algunos niveles |
| `comuna` | Columna común acordada | Visualización y filtro |

**Importante:** `id`, `lat` y `lon` son nombres propuestos. La clave efectiva podría ser `cueanexo` **solo si identifica unívocamente cada fila en cada nivel**. Se decidirá después de inspeccionar las fuentes.

## Atributos específicos

Todos los campos adicionales del CSV se conservan, sin exigir columnas vacías a otros niveles. La tabla mostrará **todos los encabezados y todas las columnas** en el orden exportado. No se hará una selección de columnas visibles.

## Ejemplo ilustrativo, no esquema definitivo

```csv
cueanexo,nombre,direccion,lat,lon,supervision,comuna,atributo_propio
20000000,Establecimiento de ejemplo,Calle de ejemplo,-34.61,-58.44,Supervision X,4,Valor
```

## Coordenadas

PostGIS puede generar coordenadas con:

```sql
ST_Y(ST_Transform(geom, 4326)) AS lat,
ST_X(ST_Transform(geom, 4326)) AS lon
```

Se debe verificar que `geom` tenga asignado el SRID correcto antes de transformar. Si el origen ya está en EPSG:4326, puede utilizarse directamente. Latitud/longitud se exportan como valores decimales; no como geometrías WKT.

## Identificadores y tipos

- Preservar identificadores como **texto** para no perder ceros iniciales.
- Evitar que el parser convierta automáticamente códigos en números.
- Conservar encabezados y orden original de columnas.
- Documentar nulos y codificación UTF-8.
- Evitar inferir una clave única a partir de `nombre` o `direccion`.

## GeoJSON territoriales

Cada archivo corresponde a una división territorial única (comunas o supervisiones). Se recomienda disponer de identificador, nombre y geometría `Polygon`/`MultiPolygon`. Los nombres concretos de propiedades se definirán al recibir las exportaciones.

## Relación CSV / territorio

El CSV contiene `supervision` y `comuna`. El catálogo define qué división territorial se muestra para cada nivel. **La coincidencia de valores de CSV con propiedades de polígonos debe verificarse** antes de habilitar selección de polígonos como filtro; no se debe suponer equivalencia por nombre.

## Casos especiales

- Sin coordenadas o coordenadas inválidas: el registro puede permanecer en la tabla y marcarse en el reporte; no se dibuja un punto incorrecto.
- Sin supervisión: se conserva el valor vacío y se define comportamiento del filtro.
- Valores de comuna inconsistentes: se normalizan en origen o se reportan.
- Claves duplicadas: se detectan antes de publicar.
