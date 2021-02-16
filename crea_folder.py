import os
import errno

def crea_folder(ruta_carpeta):
    """ comprueba existencia directorio, sino lo crea """
    try:
        os.makedirs(ruta_carpeta)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
