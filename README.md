# Atlas educativo CABA — Supervisiones

Visualizador geográfico **estático y portable** de establecimientos educativos y divisiones territoriales de la Ciudad Autónoma de Buenos Aires.

## Inicio rápido

1. Abrir **`distribucion/index.html`** con un navegador actualizado.
2. Seleccionar nivel, comuna y supervisión (si corresponde).
3. Explorar el mapa, seleccionar polígonos o puntos, consultar la ficha y la tabla, ordenar columnas y exportar CSV filtrados.

**No requiere PostgreSQL, servidor local ni compilación.** Leaflet y OpenStreetMap se cargan desde Internet; por tanto, se necesita conexión para el mapa interactivo y el fondo cartográfico. Los datos locales se cargan mediante archivos JavaScript para admitir `file://`.

## Estructura

```text
supervisiones_caba/
├── README.md
├── docs/                 Documentación y validaciones
├── fuentes/
│   ├── csv/              Nueve CSV originales
│   └── geojson/          Siete GeoJSON originales
├── scripts/
│   └── preparar_datos.py Generación de los archivos JS
└── distribucion/         Visualizador ejecutable autónomo
    ├── index.html
    ├── css/estilos.css
    ├── js/app.js
    ├── js/catalogo.js
    └── data/
        ├── establecimientos/
        └── territorios/
```

## Capas

Nueve niveles: Adultos Primaria, Adultos Secundaria, Artística, Especial, Inicial, Media, Normales, Primaria y Técnica. Territorios: barrios, comunas y cinco familias de polígonos de supervisión. Inicial y Primaria comparten polígonos; Adultos Primaria y Secundaria también.

## Actualizar datos

Reemplazar los CSV/GeoJSON dentro de `fuentes/` conservando nombres y campos comunes, ejecutar:

```bash
python scripts/preparar_datos.py
```

Después abrir `distribucion/index.html` y comprobar filtros y puntos. Para compartir solamente el visor, comprimir el **contenido** de `distribucion/`.

## Consideraciones

- La tabla conserva todas las columnas específicas de cada CSV, con desplazamiento horizontal y vertical.
- La selección de polígonos aplica un filtro espacial sobre las coordenadas del establecimiento; no depende de que el nombre de supervisión del CSV coincida exactamente con el nombre del polígono.
- Normales y Artística no tienen supervisión administrativa propia definida en este conjunto: se filtran por comuna. En el CSV original de Artística el valor `supervision` repite la comuna.
- Los polígonos se muestran como referencia cartográfica y la pertenencia se determina con un algoritmo de punto-en-polígono; revisar casos sobre límites y geometrías inválidas antes de utilizar el resultado como fuente administrativa oficial.
- Los datos corresponden a los archivos entregados, no a una actualización en tiempo real.

Repositorio: https://github.com/XtnPaez/supervisiones_caba
