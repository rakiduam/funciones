# python 3.x
# pensado en arrays verticales inicialmente...
from osgeo import gdal

def escribe_geotif(nombre_salida, array_escribir, metadata_diccionario, nodataval):
    """

    :param nombre_salida:
    :param array_escribir:
    :param metadata_geotrans:
    :param metadata_proyeccion:
    :param metadata_noval:
    :param metadata_xsize:
    :param metadata_ysize:
    :return:
    """
    xsize = metadata_diccionario.size_x
    ysize = metadata_diccionario.size_y
    'geotransform': dst.GetGeoTransform(),  # geotransform
    'nodata': img.GetNoDataValue(),  # nodata value
    proyeccion = metadata_diccionario.proj4
    'res_x': xres,  # resolucion en x
    'res_y': yres,  # resolucion en y
    'size_x': dst.RasterYSize,  # numero pixeles en x
    'size_y': dst.RasterYSize,  # numero pixeles en y
    # 'dtype': dst.NumericTypeCodeToGDALTypeCode()

    imagen = (lista_nombres_salida)
    rstARR = array_numpy_a_escribir.reshape(xsize, ysize)
    nombre = (carpeta_sal + '/' + imagen)
    out_ds = gdal.GetDriverByName('GTiff').Create(nombre,
                                                  xsize,
                                                  ysize, 1,
                                                  gdal.GDT_Int16,
                                                  ['COMPRESS=LZW',
                                                   'TILED=YES'])
    out_ds.SetGeoTransform(geotrans)
    out_ds.SetProjection(proyeccion)
    out_ds.GetRasterBand(1).WriteArray(rstARR)
    out_ds.GetRasterBand(1).SetNoDataValue(nodataval)
    out_ds = None

#
#
# def escribe_tif(lista_nombres_salida, array_numpy_a_escribir, carpeta_sal,
#                 geotrans, proyeccion, nodataval, xsize, ysize):
#     count = 0  # contador recurrente
#     if len(array_numpy_a_escribir.shape) >= 2:
#         print('no pasa na guacho')
#         for imagen in (lista_nombres_salida):
#             rstARR = array_numpy_a_escribir[:, count].reshape(xsize, ysize)
#             nombre = (carpeta_sal + '/' + imagen)
#             out_ds = gdal.GetDriverByName('GTiff').Create(nombre,
#                                                           xsize,
#                                                           ysize, 1,
#                                                           gdal.GDT_Int16,
#                                                           ['COMPRESS=LZW',
#                                                            'TILED=YES'])
#             out_ds.SetGeoTransform(geotrans)
#             out_ds.SetProjection(proyeccion)
#             out_ds.GetRasterBand(1).WriteArray(rstARR)
#             out_ds.GetRasterBand(1).SetNoDataValue(nodataval)
#             out_ds = None
#             count += 1
#     elif len(array_numpy_a_escribir.shape) < 2:
#         imagen = (lista_nombres_salida)
#         rstARR = array_numpy_a_escribir.reshape(xsize, ysize)
#         nombre = (carpeta_sal + '/' + imagen)
#         out_ds = gdal.GetDriverByName('GTiff').Create(nombre,
#                                                       xsize,
#                                                       ysize, 1,
#                                                       gdal.GDT_Int16,
#                                                       ['COMPRESS=LZW',
#                                                        'TILED=YES'])
#         out_ds.SetGeoTransform(geotrans)
#         out_ds.SetProjection(proyeccion)
#         out_ds.GetRasterBand(1).WriteArray(rstARR)
#         out_ds.GetRasterBand(1).SetNoDataValue(nodataval)
#         out_ds = None