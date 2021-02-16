# python 3.x
from osgeo import gdal

def metadata(archivo_imagen):
    """
    obtiene geo metadata desde archivos raster o hdf.
    """
    if str(archivo_imagen)[-3:] == 'hdf':
        #
        #lee_hdf = gdal.Open(archivo_imagen, gdal.GA_ReadOnly)
        lee_hdf = gdal.Open(archivo_imagen, gdal.GA_ReadOnly)
        # ojo, no todas los datasets son iguales dentro de MODIS
        #dst = gdal.Open(lee_hdf.GetSubDatasets()[0][0], gdal.GA_ReadOnly)
        dst = gdal.Open(lee_hdf.GetSubDatasets()[0][0], gdal.GA_ReadOnly)
        img = dst.GetRasterBand(1)
        #
    elif str(archivo_imagen)[-3:] != 'hdf':
        #
        dst = gdal.Open(archivo_imagen, gdal.GA_ReadOnly)
        img = dst.GetRasterBand(1)
        #
    ulx, xres, xskew, uly, yskew, yres = dst.GetGeoTransform()
    #
    metadata_diccionario = ({
    # geo_transform = (x top left, x cell size, x rotation, y top left,
    # y rotation, negative y cell size)
           'geotransform': dst.GetGeoTransform(),  # geotransform
           'nodata': img.GetNoDataValue(),  # nodata value
           'proj4': dst.GetProjection(),  # proyeccion imagen
           'res_x': xres,  # resolucion en x
           'res_y': yres,  # resolucion en y
           'size_x': dst.RasterYSize, # numero pixeles en x
           'size_y': dst.RasterYSize, # numero pixeles en y
           #'dtype': dst.NumericTypeCodeToGDALTypeCode()
           })
    lee_hdf = None
    dst = None
    img = None
    return(metadata_diccionario)
