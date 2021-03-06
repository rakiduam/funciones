import geopandas
from pathlib import Path
from os.path import split as separa


def gdf2df(ubicacion_archivo):
    gdf = geopandas.read_file(ubicacion_archivo)
    largo = len(Path(ubicacion_archivo).suffix)
    gdf['centroide'] = gdf.centroid
    gdf.insert(1, 'x', gdf.centroid.x)
    gdf.insert(1, 'y', gdf.centroid.y)
    gdf.to_excel(ubicacion_archivo[:-largo] + '.xlsx',
                 freeze_panes=[1, 4],
                 sheet_name=(separa(ubicacion_archivo)[-1])[:-largo])

# gdf2df('/home/fanr/SIG/PROCESANDO/datos_entrada/sampled_krig.shp')
# gdf2df('/home/fanr/SIG/PROCESANDO/datos_entrada/sampled_krig_300.shp')

# ubicacion_archivo = '/home/fanr/SIG/PROCESANDO/datos_entrada/sampled_krig.shp'
# pathlib.Path(ubicacion_archivo).suffix