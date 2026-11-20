# Hoja de ruta y decisiones pendientes

## Fase 0 — Diseño (actual)

- [x] Cobertura: CABA.
- [x] Nueve niveles/modalidades de puntos.
- [x] CSV distintos con campos particulares conservados.
- [x] Campos `supervision` y `comuna` compartidos para visualizar y filtrar.
- [x] Puntos generados desde CSV.
- [x] GeoJSON solo para límites territoriales.
- [x] Polígonos reutilizables entre niveles.
- [x] Tabla con **todas** las columnas y scroll horizontal/vertical.
- [x] Actualización como máximo anual.
- [x] Distribución portable mediante `index.html`.
- [x] Documentación inicial del repositorio.

## Fase 1 — Datos definitivos

- [ ] Exportar los nueve CSV desde PostGIS.
- [ ] Identificar divisiones territoriales únicas y exportar sus GeoJSON.
- [ ] Confirmar nombres y tipos de campos comunes.
- [ ] Verificar identificador único por fila.
- [ ] Definir relación de cada nivel con cada división territorial.
- [ ] Documentar campos, origen, corte y conteos.

## Fase 2 — Motor nuevo

- [ ] Implementar catálogo declarativo.
- [ ] Implementar conversión CSV/GeoJSON a JS local.
- [ ] Generar marcadores desde CSV.
- [ ] Implementar filtros por supervisión y comuna.
- [ ] Implementar tabla dinámica con todas las columnas.
- [ ] Implementar scroll horizontal y vertical.
- [ ] Vincular mapa, tabla y ficha.
- [ ] Exportar CSV filtrado sin pérdida de columnas.

## Fase 3 — Verificación y publicación

- [ ] Validar los datos y documentar incidencias.
- [ ] Probar los nueve niveles.
- [ ] Probar apertura con doble clic en `index.html`.
- [ ] Probar navegadores y resoluciones objetivo.
- [ ] Preparar ZIP portable y versión de publicación.
- [ ] Registrar fecha de corte y cambios.

## Decisiones por resolver cuando lleguen los datos

1. Clave única real de cada fila y nombres definitivos de coordenadas.
2. Inventario de polígonos y asociación nivel → territorio.
3. Comportamiento del filtro de supervisión en niveles sin límites propios.
4. Relación entre clic en polígonos y filtros por atributo.
5. Cantidad de registros y estrategia de paginación/virtualización.
6. Licencias, visibilidad del repositorio y publicación de fuentes.

## Criterio de cierre

La versión está lista cuando cada uno de los nueve niveles se puede seleccionar, filtrar, consultar y exportar sin pérdida de columnas; los polígonos correctos se muestran y la carpeta del visor funciona al abrir `index.html` sin servidor.
