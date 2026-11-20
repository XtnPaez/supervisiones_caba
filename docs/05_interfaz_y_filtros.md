# Interfaz, tabla y filtros

## Diseño general

Se toma como referencia funcional y visual el MVP: panel de capas y filtros, mapa principal, tabla vinculada e inspector de establecimiento.

## Flujo principal

1. Seleccionar uno de los nueve niveles.
2. Cargar los registros del CSV correspondiente y su territorio asociado.
3. Generar marcadores desde `lat`/`lon`.
4. Filtrar por `supervision`, `comuna` y búsqueda textual.
5. Actualizar **el mismo subconjunto** de registros en mapa, tabla y contador.
6. Seleccionar un punto o una fila para abrir la ficha correspondiente.

## Tabla: requisito obligatorio

- Mostrar **todas las columnas del CSV** seleccionado, incluidas las específicas de ese nivel.
- Mantener el **orden de columnas** del archivo fuente.
- No ocultar ni eliminar columnas por una configuración predeterminada.
- Permitir **desplazamiento horizontal** cuando el ancho exceda el panel.
- Permitir **desplazamiento vertical** cuando existan muchas filas.
- Mantener accesibles el mapa, los filtros y los controles de navegación.
- Considerar encabezado fijo durante el desplazamiento vertical, si las pruebas de usabilidad lo confirman.
- Paginación o virtualización: decisión técnica a evaluar según volumen y rendimiento; ninguna puede eliminar columnas.
- La exportación CSV debe preservar todas las columnas de los registros filtrados.

## Filtros

- `supervision`: valores del CSV del nivel activo.
- `comuna`: valores del CSV del nivel activo.
- Búsqueda textual: alcance exacto por definir; se recomienda poder buscar en todas las columnas convertidas a texto.
- Filtros combinables por intersección lógica (AND).
- Opción de limpiar filtros y recuperar la extensión total.
- Si un nivel carece de valores útiles de supervisión, no inventar categorías: mostrar estado sin datos/no aplica según se acuerde.

## Selección

- Clic en punto: resaltar marcador y seleccionar registro.
- Clic en fila: seleccionar el mismo registro y centrarlo si tiene coordenadas válidas.
- Ficha: mostrar los atributos disponibles del registro, sin asumir campos propios de otros niveles.
- Cambiar de nivel limpia la selección y los filtros incompatibles.

## Pruebas de interfaz

- CSV con 5, 15, 30 o más columnas.
- Textos largos y celdas vacías.
- Scroll horizontal y vertical simultáneos.
- Filtros y selección sincronizados.
- Filas sin coordenadas.
- Navegador abierto con `file://`.
