#!/usr/bin/env python3
"""Reconstruye los archivos JS portables a partir de fuentes/csv y fuentes/geojson.
Uso: python scripts/preparar_datos.py (desde cualquier directorio)
"""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'distribucion'
manifest=json.loads((DEST/'js/catalogo.js').read_text(encoding='utf8').split('=',1)[1].rstrip().rstrip(';'))
for level,meta in manifest.items():
    f=ROOT/'fuentes/csv'/f'{level}.csv'
    with f.open(encoding='utf-8-sig',newline='') as h:
        reader=csv.DictReader(h);rows=list(reader);meta['columns']=reader.fieldnames
    out=[]
    for row in rows:
        try:
            row['lat']=float(row['lat'].replace(',','.'));row['lon']=float(row['lon'].replace(',','.'))
            if not(-35.2<row['lat']<-34.2 and -59.1<row['lon']<-57.8):raise ValueError('fuera de rango')
        except (ValueError,KeyError):
            print(f'AVISO: coordenadas inválidas en {level}: {row.get("cueanexo")}');continue
        row={k:(None if isinstance(v,str) and v.strip().upper() in ('','NULL') else v) for k,v in row.items()}
        if level=='artistica':row['supervision']=None
        out.append(row)
    meta['count']=len(out)
    (DEST/'data/establecimientos'/f'{level}.js').write_text('window.ATLAS_DATA=window.ATLAS_DATA||{};window.ATLAS_DATA['+json.dumps(level)+']='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8')
    print(level,len(out))
for f in sorted((ROOT/'fuentes/geojson').glob('poligonos_*.geojson')):
    key=f.stem.removeprefix('poligonos_');data=json.loads(f.read_text(encoding='utf-8-sig'))
    (DEST/'data/territorios'/f'{key}.js').write_text('window.ATLAS_TERR=window.ATLAS_TERR||{};window.ATLAS_TERR['+json.dumps(key)+']='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8')
(DEST/'js/catalogo.js').write_text('window.ATLAS_MANIFEST='+json.dumps(manifest,ensure_ascii=False,indent=2)+';\n',encoding='utf8')
print('Datos regenerados correctamente.')
