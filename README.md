# Supervisiones CABA

Visualizador geográfico estático y portable de establecimientos educativos y territorios de supervisión de la Ciudad Autónoma de Buenos Aires.

**Desarrollado por MAPA - UEICEE - 2026**

**Repositorio:** https://github.com/XtnPaez/supervisiones_caba

## Uso

Abrir `distribucion/index.html` en un navegador actualizado. No requiere servidor local, PostgreSQL ni compilación. Requiere conexión a Internet para Leaflet (CDN) y el mapa base oficial de CABA.

Permite seleccionar nivel educativo, buscar establecimientos, filtrar por comuna y supervisión cuando corresponda, activar capas territoriales y seleccionar polígonos para filtrar espacialmente. Los puntos se pueden seleccionar para abrir una ficha, que se cierra con **Cerrar ficha** o la tecla `Esc`.

La tabla inferior muestra **todas las columnas** del CSV correspondiente, con desplazamiento horizontal y vertical, ordenamiento y paginación. El botón **Descargar listado CSV** exporta **todos los registros filtrados**, no solo los visibles en la página actual. También está disponible **Exportar filtrados · CSV** en el encabezado.

## Datos

- **9 CSV de establecimientos:** Adultos Primaria (82), Adultos Secundaria (112), Artística (12), Especial (54), Inicial (364), Media (108), Normales (18), Primaria (452), Técnica (39). Total: **1.241 registros** en los archivos de origen.
- **7 GeoJSON:** barrios, comunas y supervisiones de Adultos, Especial, Inicial/Primaria, Media y Técnica.
- Campos comunes: `cueanexo`, `nombre`, `direccion`, `lat`, `lon`, `comuna`, `supervision`.
- Artística y Normales se filtran territorialmente por comuna, sin supervisión administrativa propia definida en estos datos.

## Estructura del repositorio

```text
supervisiones_caba/
├── README.md
├── docs/
│   ├── arquitectura.md
│   ├── catalogo_capas.md
│   ├── modelo_datos.md
│   ├── interfaz_y_filtros.md
│   ├── actualizacion_datos.md
│   ├── validacion.md
│   ├── hoja_de_ruta.md
│   └── historial_cambios.md
├── fuentes/
│   ├── csv/
│   └── geojson/
├── scripts/
│   └── preparar_datos.py
└── distribucion/
    ├── index.html
    ├── css/estilos.css
    ├── js/app.js
    ├── js/catalogo.js
    └── data/
        ├── establecimientos/
        └── territorios/
```

## Mapa base

Se utiliza el mapa oficial del Gobierno de la Ciudad de Buenos Aires, servido mediante GeoServer/GeoWebCache (TMS):

```text
https://geoserver.buenosaires.gob.ar/geoserver/gwc/service/tms/1.0.0/catalogo_mapa_base:mapa_base_v2@EPSG:900913@png/{z}/{x}/{-y}.png
```

Se configura en `distribucion/js/app.js` mediante `L.tileLayer(...)`. La plantilla `{-y}` atiende a la numeración TMS.

## Actualización de datos

1. Reemplazar los CSV y GeoJSON originales dentro de `fuentes/`, conservando los nombres esperados.
2. Ejecutar `python scripts/preparar_datos.py` desde la raíz del repositorio.
3. Verificar los nueve niveles, filtros, polígonos, fichas y descarga CSV en `distribucion/index.html`.
4. Publicar o comprimir **el contenido de `distribucion/`** para distribuir el visor sin el resto del repositorio.

Los archivos de `distribucion/data/` son JavaScript generado, para permitir abrir el visor desde `file://`. No editar esos archivos a mano.

## Alcance y limitaciones

La versión documentada es **v1.2**. Se realizaron correcciones de interfaz en v1.1 y cambios de identidad institucional en v1.2. Las comprobaciones estructurales de fuentes no equivalen a una auditoría topológica ni a pruebas automatizadas completas en navegador. Los datos corresponden a las exportaciones incorporadas al repositorio, no a consultas en tiempo real.

Consultar [`docs/`](docs/) para detalles de arquitectura, datos, operación y cambios.
