import os
from shutil import move
from glob import glob

def mover_archivos(tipo, origen_carpeta, destino_carpeta):
    """

    :param tipo:
    :param origen_carpeta:
    :param destino_carpeta:
    :return:
    """
    listado_origen = glob('*' + tipo)

