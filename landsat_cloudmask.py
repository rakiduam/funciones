# https://www.usgs.gov/core-science-systems/nli/landsat/landsat-sr-derived-spectral-indices-pixel-quality-band
# https://numpy.org/doc/stable/reference/generated/numpy.bitwise_and.html
from osgeo import gdal
import numpy as np

def cloud_values(ubicacion_qa_landsat):
    """
    se ingresa la ubicacion del raster de quality assesment de landsat,
    el que se abre, con gdal y se tranforma a array de numpy
    :return:
    valores que son usados para la mascara.
    se puede usar en arcpy u otro
    """
    qa = gdal.Open(ubicacion_qa_landsat)
    unicos = np.unique(qa.ReadAsArray())
    # los valores corresponden a nubes, sombras de nube ver url
    out = [True if((np.bitwise_and(unico, 5) and np.bitwise_and(unico,7)) or np.bitwise_and(unico,3)) else False for unico in unicos]
    return(out)
