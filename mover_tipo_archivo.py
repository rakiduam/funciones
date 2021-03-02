from os.path import join as juntar
from shutil import move
from glob import glob

def mover_archivos(tipos, origen, destino):
    """
    :param tipos: lista en cadena de archivos a mover
    :param origen: directorio de origen
    :param destino: directorio de salida
    :return:
    """
    for tipo in tipos:
        listado_origen = glob(juntar(origen, '**/*.' + tipo))
        [move(juntar(archivo), juntar(destino, archivo.split('/')[-1])) for archivo in listado_origen]

# mover_archivos(['tif', 'hdr', 'tfw'], '/home/fanr/SIG/DEM/SRTM/', '/home/fanr/SIG/DEM/SRTM/todos/')
