import os
from osgeo import gdal
import numpy as np
from cloud_values import cloud_values
from gdal_metadata import metadata
from glob import glob
from escribe_geotif import escribir_geotif

entdir = ''
outdir = ''

archivo = (r'/home/fanr/Descargas/LC082330842021011201RT-SC20210204115857/LC08_L1TP_233084_20210112_20210112_01_RT_pixel_qa.tif')
archivob2 = (r'/home/fanr/Descargas/LC082330842021011201RT-SC20210204115857/LC08_L1TP_233084_20210112_20210112_01_RT_sr_band2.tif')
raster = gdal.Open(archivo).ReadAsArray()

#raster_masked = np.where((x in np.array(cloud_values(archivo))), 1, 0)
raster_masked = np.where(np.isin(raster, cloud_values(archivo)), 1, 0)
rb2 = gdal.Open(archivob2).ReadAsArray()

escribir_geotif(nombre_salida='/home/fanr/Descargas/b2.tif', raster_array=rb2*raster_masked,
                geotransform=metadata(archivo)['geotransform'], proyeccion=metadata(archivo)['proj4'],
                xsize=metadata(archivo)['size_x'], ysize=metadata(archivo)['size_y'],
                nodata=metadata(archivo)['nodata'])


# escribe_geotif(nombre_salida='/home/fanr/Descargas/aa.tif', raster_masked, metadata(archivo), -999)

raster_masked.max()
raster_masked.min()

aa = raster * raster_masked
np.unique(aa.ravel())
aa.max()
aa.min()

escribir_geotif(nombre_salida='/home/fanr/Descargas/aa.tif', raster_array=raster_masked,
                geotransform=metadata(archivo)['geotransform'], proyeccion=metadata(archivo)['proj4'],
                xsize=metadata(archivo)['size_x'], ysize=metadata(archivo)['size_y'],
                nodata=metadata(archivo)['nodata'])

cloud_values(archivo)

meta = metadata(archivo)
meta.keys()

raster.ReadAsArray()

