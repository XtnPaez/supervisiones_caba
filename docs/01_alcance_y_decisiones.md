# Alcance y decisiones de arquitectura

## Alcance confirmado

- Cobertura geográfica exclusiva: **Ciudad Autónoma de Buenos Aires (CABA)**.
- Nueve capas de establecimientos: Adultos Primaria, Adultos Secundaria, Artística, Especial, Inicial, Media, Normales, Primaria y Técnica.
- Cada nivel tiene su **propio CSV**, con atributos particulares que **no deben eliminarse ni homogeneizarse artificialmente**.
- Los CSV pueden compartir campos requeridos por el visualizador, en particular `supervision` y `comuna`.
- Los establecimientos se dibujan como puntos a partir de las coordenadas del CSV.
- Los polígonos GeoJSON representan límites territoriales; no son GeoJSON de puntos.
- Algunos niveles utilizan comunas en lugar de polígonos específicos de supervisión.
- Un mismo GeoJSON de polígonos puede ser utilizado por más de un nivel.
- Se conservan todas las columnas de cada CSV en su tabla correspondiente.
- La tabla debe disponer de **scroll horizontal y vertical**.
- El visor se distribuye como carpeta portable y se abre desde `index.html` con Internet para dependencias externas.
- Los datos cambian como máximo una vez por año; se exportan desde PostgreSQL/PostGIS.
- La nueva arquitectura se documentará en un repositorio.

## Decisiones de implementación propuestas

- Un motor genérico más un catálogo de niveles y territorios.
- Una capa de puntos activa por vez en la interfaz inicial, como el MVP; diseño interno ampliable.
- Transformar las exportaciones a archivos `.js` de datos para permitir `file://`.
- Resolver asociaciones de supervisión y comuna antes de publicar, preferentemente en PostGIS.
- No crear un backend, API o actualizador automático.

## Aún no acordado

- Nombres finales de columnas de coordenadas, clave única y convenciones de valores nulos.
- Qué GeoJSON corresponde a cada nivel y qué identificadores tienen los polígonos.
- Si el clic sobre un polígono activará el filtro territorial correspondiente en todos los casos.
- Cómo manejar valores vacíos de `supervision` cuando un nivel solo use comunas.
- Política de publicación de datos, licencia y repositorio.

Estas cuestiones deben resolverse con las exportaciones nuevas, sin inventar relaciones.
