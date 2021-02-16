from osgeo import gdal

def hdf2array(hdf, banda):
    """
    hdf : nombre del archivo HDF
    banda: banda de la cual extraer el dato
    devuelve un array de numpy
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