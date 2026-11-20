# Modelo de datos

Campos comunes obligatorios: `cueanexo`, `nombre`, `direccion`, `lat`, `lon`, `comuna`, `supervision`.

Los nueve archivos conservan columnas adicionales según nivel. `lat` y `lon` representan grados decimales WGS84. `cueanexo` se trata como identificador textual; `comuna` se normaliza como texto para el filtro.

`supervision` puede ser nulo si no existe una supervisión territorial propia en los archivos. En Normales, el literal `NULL` se transforma en nulo. En Artística, el CSV de origen usa el número de comuna como `supervision`; la distribución lo interpreta como nulo para no confundir jurisdicción comunal con supervisión administrativa.

Los GeoJSON tienen geometrías MultiPolygon, con coordenadas longitud-latitud. La selección de un polígono usa geometría real, no igualdad de nombres.
