# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:13:01 2020

@author: fneira
"""

from pathlib import Path

import geopandas
import pandas as pd


def df2gdf(ubicacion_archivo_xls, col_x, col_y, sheet=None, na_values=None, crs_salida=None):
    """
    :param ubicacion_archivo_xls:
    :param col_x:
    :param col_y:
    :param sheet:
    :param na_values: default -9999
    :param crs_salida: default 32719
    :return:
    """
    if sheet is None:
        sheet = 0
    if na_values is None:
        na_values = '-9999'
    if crs_salida is None:
        crs_salida = 'EPSG:32719'

    df = pd.read_excel(ubicacion_archivo_xls,
                       header=0,
                       sheet_name=sheet,
                       na_values=str(na_values))

    gdf = geopandas.GeoDataFrame(df,
                                 geometry=geopandas.points_from_xy(df[col_x], df[col_y]),
                                 crs=crs_salida)

    largo = len(Path(ubicacion_archivo_xls).suffix)

    gdf.to_file(ubicacion_archivo_xls[:-largo] + '.shp')

# ubicacion_archivo_xls = '/home/fanr/Downloads/PET_MODIS/pet_modis.xlsx'
# df2gdf('/home/fanr/Downloads/PET_MODIS/pet_modis.xlsx', 'lon', 'lat', sheet=None, na_values=None, crs_salida=None):

# os.chdir('D:/Users/fneira/OneDrive - ciren.cl/2020_FIA_MAGALLANES/DATOS_CLIMA/FINAL/')
#
# archivo = 'D:/Users/fneira/OneDrive - ciren.cl/2020_FIA_MAGALLANES/DATOS_CLIMA/FINAL/BBDD_CLIMA.xlsx'
#
# df = pd.read_excel(archivo, sheet_name='MIXTO', na_values='-9999')
#
# gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df._LON, df._LAT),
#                        crs="EPSG:4326")
#
# gdf.to_file('bbdd_clima.shp')
#
# gdf.plot()
