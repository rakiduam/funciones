# https://www.geeksforgeeks.org/how-to-uncompress-a-tar-gz-file-using-python/
import tarfile
import zipfile

def descomprimir_todo(comprimido, directorio_salida):
    """
    archivo: descomprime archivos tipo tar.gz
    """
    file = tarfile.open(comprimido)
    file.extractall(directorio_salida)
    file.close()


# def descomprimir_todo(comprimido, directorio_salida):
#     """
#     """
#