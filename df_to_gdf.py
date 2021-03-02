# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:13:01 2020

@author: fneira
"""

import pandas as pd
import geopandas as gpd
import os

os.chdir('D:/Users/fneira/OneDrive - ciren.cl/2020_FIA_MAGALLANES/DATOS_CLIMA/FINAL/')

archivo = 'D:/Users/fneira/OneDrive - ciren.cl/2020_FIA_MAGALLANES/DATOS_CLIMA/FINAL/BBDD_CLIMA.xlsx'

df = pd.read_excel(archivo, sheet_name='MIXTO', na_values='-9999')

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df._LON, df._LAT),
                       crs="EPSG:4326")

gdf.to_file('bbdd_clima.shp')

gdf.plot()
