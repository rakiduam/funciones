from glob import glob
import os

def listar_todos_los_archivos(tipo, carpeta_raiz):
    """
    :param tipo:
    :param carpeta_raiz:
    :return:
    """
    os.chdir(carpeta_raiz)
    sub_carpetas = [(os.path.join(os.getcwd(), carpeta)) for carpeta in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), carpeta)) == True]
    listado = []
    for carpeta in sub_carpetas:
        listado = listado + glob(os.path.join(os.getcwd(), carpeta, '***' + tipo))
    return(listado)

# carpeta_raiz = 'E:/cnr/espa-fneira@ciren.cl-12182020-192057-758/temporadas/'
# tipo = '.gz'
# listar_todos_los_archivos('*gz', raiz)