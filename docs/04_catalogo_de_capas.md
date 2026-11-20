# Catálogo de capas y territorios

## Nueve capas de puntos

| ID de nivel | Etiqueta | CSV de origen | Territorio asociado |
|---|---|---|---|
| `adultos_primaria` | Adultos Primaria | `adultos_primaria.csv` | Por definir |
| `adultos_secundaria` | Adultos Secundaria | `adultos_secundaria.csv` | Por definir |
| `artistica` | Artística | `artistica.csv` | Por definir |
| `especial` | Especial | `especial.csv` | Por definir |
| `inicial` | Inicial | `inicial.csv` | Por definir |
| `media` | Media | `media.csv` | Por definir |
| `normales` | Normales | `normales.csv` | Por definir |
| `primaria` | Primaria | `primaria.csv` | Por definir |
| `tecnica` | Técnica | `tecnica.csv` | Por definir |

Los nombres de archivo son una **convención propuesta**, no nombres observados en las nuevas exportaciones.

## Catálogo territorial

No se crearán automáticamente nueve archivos de polígonos. Solo se almacenarán las divisiones territoriales **realmente distintas** que se reciban desde PostGIS, incluyendo comunas y supervisiones específicas.

| ID territorial | Tipo | Archivo | Niveles usuarios |
|---|---|---|---|
| `comunas` | Comuna | Por definir | Por definir |
| Otros IDs | Supervisión | Por definir | Por definir |

Un mismo ID territorial puede aparecer asociado a múltiples niveles.

## Esquema conceptual de configuración

```javascript
// Ejemplo de diseño: NO representa asignaciones reales
const catalogo = {
  niveles: {
    primaria: {
      etiqueta: 'Primaria',
      datos: 'data/establecimientos/primaria.js',
      territorio: 'territorio_por_definir'
    }
  },
  territorios: {
    territorio_por_definir: {
      datos: 'data/territorios/territorio_por_definir.js',
      campoId: 'campo_por_definir'
    }
  }
};
```

La configuración final deberá indicar cómo se llaman los campos de identificación y selección territorial. La tabla no necesita una lista de columnas porque debe mostrar todas las del CSV.

## Comportamiento territorial

- La selección de nivel determina qué puntos y qué polígonos se muestran.
- `supervision` y `comuna` filtran por atributos del CSV.
- Los límites se dibujan a partir del GeoJSON seleccionado.
- Un clic sobre un polígono solo puede aplicar un filtro si la correspondencia está definida y validada.
- Si un nivel usa comunas como división territorial, no se inventan supervisiones geométricas.
