# -*- coding: utf-8 -*-
"""
    Listado de funciones recurrentes en los scripts de procesamiento.
    Más fácil mantener un archivo que varios.
    Buscar la forma de que se importe siempre y que busque si esta.
"""

###############################################################################
#### LIBRERIAS ################################################################
###############################################################################
from osgeo import gdal, gdal_array
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.interpolate import InterpolatedUnivariateSpline as spline
import errno
import glob
import numpy as np
import os
import time
import tqdm


###############################################################################
#### FUNCIONES ################################################################
###############################################################################

######################################################################
## TEXTO
def crea_dir(x):
    try:
        os.makedirs(x)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def slash(texto):
    """
    reemplaza slash windows o doble slash
    """
    texto = texto.replace('\\', '/').replace('///', '/').replace('//', '/')
    return(texto)


def get_dia(lista_tif):
    """
    extrae el dia de adquisición desde el nombre MODIS. Siempre que se
    mantenga, la estructura MOD13A2.A2017225.h11v10.xxxxxxx.*
    """
    dias = [int((y.replace('\\', '/').replace('///', '/').replace('//', '/').split('.')[-4])[-3:]) for y in lista_tif]
    #dias = [i. for i in lista_tif]
    return(dias)

def nombres_relleno(lista_original_nombres):
    """
    Crea 365 estructura nombre para relleno, bajo la estructura:
    ejemplo :  MODXXXX.DIA###.
    """
    #
    nombre_original = lista_original_nombres[0]
    nombre_original = (nombre_original.split("/"))[-1]
    split_en_puntos = str(nombre_original).split(".")
    split_en_puntos[1] = split_en_puntos[1][:-3]
    #
    lista_temp = []
    #
    for dia in range(1, 366):
        split_en_puntos[1] = ("").join([split_en_puntos[1], str(dia).zfill(3)])
        #
        dia_temp = ('.').join(split_en_puntos)
        #
        split_en_puntos[1] = split_en_puntos[1][:-3]
        #
        lista_temp.append(dia_temp)
    #
    return(lista_temp)



######################################################################
## MANEJO DE RASTERS
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


def hdf2array(hdf, banda):
    """
    hdf_2_arr: transforma lista de ubicaciones de archivos HDF,
    y extrae el dataset seleccionado (sd)
    agrupa datos ordenados en formato array:
    columna imagen, fila pixel
    """
    lista = []
    for i in tqdm(hdf):
        hdf_ds = gdal.Open(i, gdal.GA_ReadOnly)
        img_ds = gdal.Open(hdf_ds.GetSubDatasets()[banda][0], gdal.GA_ReadOnly)
        bnd_ds = (img_ds.GetRasterBand(1)).ReadAsArray()
        lista.append(bnd_ds)
        hdf_ds = None
        img_ds = None
        bnd_ds = None
    return(np.array(lista))


def rst2array(tif_lista):
    """
    rst_2_arr: transforma una lista de imagenes, en un numpyarray.
    ordenado, donde columna es la imagen, y fila el pixel (serie tiempo)
    """
    #
    lista = np.empty([])
    for count, rst_img in enumerate(tif_lista):
        img_dst = gdal.Open(rst_img, gdal.GA_ReadOnly)
        bnd_dst = (img_dst.GetRasterBand(1)).ReadAsArray()
        img_vec = bnd_dst.flatten(order='C')
        img_dst = None
        bnd_dst = None
        lista = lista.append(img_vec)
        if count !=0:
            lista = np.vstack((lista, img_vec))
        else:
            lista.astype(img_vec.dtype)
            lista = img_vec
    return(lista)

def img2array(tif_lista):
    for count, rst_img in enumerate(tif_lista):
        img_dst = gdal.Open(rst_img, gdal.GA_ReadOnly)
        bnd_dst = (img_dst.GetRasterBand(1)).ReadAsArray()
        img_vec = bnd_dst.flatten(order='C')
        if count !=0:
            lista[:, count] = img_vec
        else:
            lista = np.zeros((np.size(img_vec), len(tif_lista)), order='C')
            lista[:,count] = img_vec
        img_dst = None
        bnd_dst = None
    return(lista)




######################################################################
## FUNCIONES RASTER
def spline_ts(SerieTiempo, No_Data_Value):
    """
    genera relleno datos faltantes, usando spline.
    """
    #
    num_datos = np.size(SerieTiempo)
    mit_num_datos = num_datos/2
    indice = np.equal(SerieTiempo, No_Data_Value)
    suma_nodata = sum(indice)
    tipo = SerieTiempo.dtype
    #
    if suma_nodata == 0:
        SerieTiempo_relleno = SerieTiempo
    elif suma_nodata >= (mit_num_datos) :
        SerieTiempo_relleno = np.full(num_datos, No_Data_Value)
    elif suma_nodata < (mit_num_datos) :
        # busca los indices para reemplazar los valores dentro de la serie
        idx = np.argwhere(indice)
        ordinales = np.array(np.arange(0, num_datos, dtype=tipo))
        #
        ordX = np.column_stack((ordinales, SerieTiempo))
        #
        spl = InterpolatedUnivariateSpline(
                ordX[np.logical_not(indice)][:, 0],
                (ordX[np.logical_not(indice)][:, 1]),
                k=1, ext = 0)
        # genera datos interpolados por spline
        n2 = np.asarray((spl(ordinales)), dtype=tipo)
        # reemplaza solo aquellos valores no existentes en la serie original
        ordX[idx, 1] = n2[idx]
        # salida final de datos
        SerieTiempo_relleno = ordX[:, 1]
    return(SerieTiempo_relleno)



def spline_array(array, nodata):
    """
    """
    z, x, y = array.shape
    salida = np.zeros((array.shape), dtype=array.dtype)
    array = array.reshape((z, x*y), order='C')
    lista = []
    for i in tqdm(np.arange(0, y*x)):
        lista.append(spline_ts(array[:, i], nodata))
    salida=(np.stack(lista, axis=1)).reshape((z,x,y), order='C')
    return(salida)

# esta funcion se encuentra optimizada en python y puede ser aplicada
# en ejes al parecer a una velocidad mayor
# def sav_gol_array(array):
#     #
#     z, x, y = array.shape
#     salida = np.zeros((array.shape), dtype=array.dtype)
#     array = array.reshape((z, x*y), order='C')
#     #
#     lista = []
#     tipo = array.dtype
#     #
#     for i in (np.arange(array.shape[1])):
#         filled = savgol_filter(array[i, :], 11, 2, mode='wrap')
#         filled = np.array(filled, dtype = tipo)
#         lista.append(filled)
#     lista = np.stack(lista, axis=1)
#     return()


def escribe_tif(lista_nombres_salida, array_numpy_a_escribir, carpeta_sal,
                geotrans, proyeccion, nodataval, xsize, ysize):
    count = 0  # contador recurrente
    if len(array_numpy_a_escribir.shape) >= 2:
        print('no pasa na guacho')
        for imagen in (lista_nombres_salida):
            rstARR = array_numpy_a_escribir[:, count].reshape(xsize, ysize)
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
            count += 1
    elif len(array_numpy_a_escribir.shape) < 2:
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
