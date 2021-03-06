import geopandas
from pathlib import Path
from os.path import split as separa


def gdf2df(ubicacion_archivo):
    gdf = geopandas.read_file(ubicacion_archivo)
    largo = len(Path(ubicacion_archivo).suffix)
    # if (gdf.geometry.unique())=='POLYGON':
    #     gdf['centroide'] = gdf.centroid
    #     gdf.insert(1, 'x', gdf.centroid.x)
    #     gdf.insert(1, 'y', gdf.centroid.y)
    # else:
    #     print('nada')
    gdf.to_excel(ubicacion_archivo[:-largo] + '.xlsx',
                 freeze_panes=[1, 4],
                 sheet_name=(separa(ubicacion_archivo)[-1])[:-largo])

# gdf2df('/home/fanr/SIG/PROCESANDO/datos_entrada/sampled_krig.shp')
# gdf2df('/home/fanr/SIG/PROCESANDO/datos_entrada/sampled_krig_300.shp')
# gdf2df(r'C:\Users\fneira\OneDrive - ciren.cl\AGROCLIMA_COMPARTIDO\FICHA17\CLIMA_RASTER_ATLAS\salida_tablas\05_suelo-clima_2020.shp')

# ubicacion_archivo = '/home/fanr/SIG/PROCESANDO/datos_entrada/sampled_krig.shp'
# pathlib.Path(ubicacion_archivo).suffix