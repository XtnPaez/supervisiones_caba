# Atlas Educativo CABA

![Estado](https://img.shields.io/badge/estado-diseño_de_arquitectura-blue) ![Cobertura](https://img.shields.io/badge/cobertura-CABA-informational) ![Actualización](https://img.shields.io/badge/actualización-anual-lightgrey) ![Tecnología](https://img.shields.io/badge/visor-Leaflet-green)

Visualizador geográfico **estático y portable** de establecimientos educativos de la Ciudad Autónoma de Buenos Aires. Integra un mapa de puntos, límites territoriales, filtros y una tabla de atributos vinculada al mapa.

> **Estado del proyecto:** planificación de la nueva arquitectura. Los datos definitivos se exportarán nuevamente desde PostgreSQL/PostGIS. El MVP anterior es una referencia funcional y visual, no la fuente de datos de la nueva versión.

## Objetivo

Distribuir una carpeta autocontenida que se pueda abrir mediante `index.html` en un navegador, **sin instalar software ni iniciar un servidor local**. Se requiere Internet para las bibliotecas cargadas por CDN y los mapas base. Los datos de establecimientos y polígonos se distribuyen localmente.

## Capas de establecimientos

| ID | Nivel o modalidad | Geometría |
|---|---|---|
| `adultos_primaria` | Adultos Primaria | Punto |
| `adultos_secundaria` | Adultos Secundaria | Punto |
| `artistica` | Artística | Punto |
| `especial` | Especial | Punto |
| `inicial` | Inicial | Punto |
| `media` | Media | Punto |
| `normales` | Normales | Punto |
| `primaria` | Primaria | Punto |
| `tecnica` | Técnica | Punto |

Los puntos se construirán en el navegador a partir de coordenadas incluidas en los CSV de cada nivel. **No se requieren GeoJSON de puntos**.

## Capas territoriales

GeoJSON de polígonos de supervisiones y/o comunas. No todos los niveles poseen límites de supervisión propios; **varios niveles pueden compartir una misma capa de polígonos**. Las relaciones exactas se definirán cuando estén disponibles las nuevas exportaciones.

## Funciones previstas

- Selección de nivel/modalidad educativa.
- Visualización de puntos y de la división territorial asignada.
- Filtros por `supervision` y `comuna` en todos los niveles.
- Búsqueda de establecimientos y selección sincronizada entre mapa, tabla y ficha.
- **Tabla con todas las columnas del CSV seleccionado**, sin lista fija de columnas ni eliminación de atributos.
- Desplazamiento horizontal y vertical dentro del área de tabla, manteniendo accesibles el mapa y los controles.
- Exportación de registros filtrados, conservando todas las columnas.
- Datos locales portables y bibliotecas cartográficas externas vía Internet.

## Decisiones de diseño

1. **CSV diferentes por nivel:** solamente se exige un conjunto mínimo de campos comunes para el motor. Los demás atributos permanecen específicos de cada CSV.
2. **Una sola fuente para puntos y tabla:** los marcadores se derivan de los registros CSV.
3. **Polígonos independientes y reutilizables:** un GeoJSON territorial puede asociarse a múltiples niveles.
4. **Filtros por atributos:** `supervision` y `comuna` vienen resueltos desde PostGIS; el navegador no necesita ejecutar cruces espaciales.
5. **Actualización infrecuente:** como máximo una vez por año, mediante una nueva exportación validada y una nueva publicación estática.
6. **Portabilidad real:** para apertura mediante `file://`, la distribución usará archivos JavaScript de datos generados desde los CSV/GeoJSON, evitando depender de `fetch()` local.

## Organización propuesta

```text
atlas-educativo/
├── README.md
├── docs/                         # Decisiones, contratos y procedimientos
├── fuentes/                       # Exportaciones originales (a incorporar)
│   ├── establecimientos/          # Nueve CSV
│   └── territorios/               # GeoJSON únicos
├── scripts/                       # Conversión y validación (a desarrollar)
└── visor/                         # Carpeta portable que se distribuye
    ├── index.html
    ├── css/
    ├── js/
    └── data/
        ├── establecimientos/      # Archivos JS derivados de CSV
        └── territorios/           # Archivos JS derivados de GeoJSON
```

**Nota:** este paquete contiene la documentación inicial, no la implementación de la versión nueva ni las exportaciones definitivas.

## Documentación

- [Alcance y decisiones](docs/01_alcance_y_decisiones.md)
- [Arquitectura y portabilidad](docs/02_arquitectura.md)
- [Contrato de datos](docs/03_modelo_de_datos.md)
- [Capas y territorios](docs/04_catalogo_de_capas.md)
- [Interfaz y comportamiento](docs/05_interfaz_y_filtros.md)
- [Actualización y control de calidad](docs/06_actualizacion_y_validacion.md)
- [Pendientes y hoja de ruta](docs/07_hoja_de_ruta.md)

## Origen

El proyecto toma como referencia un MVP previo de supervisiones educativas de Inicial y Primaria, implementado con HTML, CSS, JavaScript y Leaflet. Su lógica original utilizaba puntos GeoJSON y, para Primaria, una tabla CSV asociada por `cueanexo`. La nueva versión **no replica obligatoriamente esa estructura**.

## Licencia y publicación

Pendiente definir la licencia del código, las condiciones de reutilización de los datos y el repositorio remoto. No se presume una licencia para los datos institucionales.
