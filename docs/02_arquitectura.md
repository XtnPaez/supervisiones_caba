# Arquitectura y portabilidad

## Arquitectura lógica

```text
PostgreSQL / PostGIS (fuente de origen)
             |
             v
  CSV por nivel + GeoJSON por territorio
             |
             v
  Validación + empaquetado reproducible
             |
             v
 visor/data/*.js  +  visor/js/catalogo.js
             |
             v
 index.html -> Leaflet + filtros + tabla + inspector
```

## Capas independientes

1. **Fuentes:** exportaciones originales, conservadas sin reescritura silenciosa.
2. **Preparación:** validaciones, reporte de calidad y generación de JavaScript local.
3. **Catálogo:** relaciona nivel, archivo de establecimientos y territorio; declara la semántica de los campos comunes.
4. **Motor:** dibuja puntos, límites, filtros, tabla y ficha sin conocer atributos particulares de un nivel.
5. **Interfaz:** presentación adaptable a muchas columnas y pantallas distintas.

## Apertura sin servidor

En navegadores, `fetch('data/archivo.csv')` desde `file://` puede estar bloqueado. Por ello el paquete portable se construirá con scripts cargados mediante etiquetas `<script src="...">` y datos declarados en un espacio de nombres conocido, o con una alternativa equivalente probada en los navegadores objetivo.

**No basta con renombrar `.csv` a `.js`:** el proceso de preparación debe generar JavaScript válido, preservar tipos/identificadores y escapar correctamente cadenas. Los CSV originales seguirán siendo los datos fuente.

Las bibliotecas Leaflet y de estilos podrán cargarse desde CDN. Los mapas base requieren Internet y están sujetos a la disponibilidad y condiciones de sus proveedores. La aplicación deberá mostrar un error claro si una dependencia externa no carga.

## Principio de no duplicación

- Cada establecimiento proviene de una fila del CSV del nivel.
- Un único conjunto de registros alimenta mapa, tabla, filtros, búsqueda y ficha.
- Los GeoJSON de polígonos se almacenan una sola vez por división territorial única.
- Una capa puede referenciar un territorio compartido mediante su ID en el catálogo.

## Diseño de carpetas

El repositorio puede contener herramientas y fuentes; **solo `visor/`** debe ser necesario para ejecutar la aplicación. Todos los enlaces internos deben ser relativos a `visor/index.html`.

## Compatibilidad a verificar

- Apertura directa en navegadores objetivo bajo `file://`.
- Disponibilidad de Leaflet y mapas base con Internet.
- Rendimiento al cargar tablas anchas y miles de registros.
- Correcta visualización en distintas resoluciones.
