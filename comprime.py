# https://www.thepythoncode.com/article/compress-decompress-files-tarfile-python
# carga de modulos
import zipfile, os, glob

# directorio entrada, comprimira todo lo que hay dentro de dicho directorio
# bastaría cambiar este directorio
entDIR = 'E:/CURSOS_AGUA/ENVIAR/'

# chequeo de cambio de directorio entrada
os.chdir(entDIR)
print(os.getcwd())

# obtener el listado unico{} de los archivos, independiente de extension
# en este caso esta seteado para que sea de forma recursiva y directorios
# de ahi ** y el recursive=True
lista = set([str(i).split('.')[0] for i in glob.glob('**/*.*', recursive=True)])

# obtener todas las extensiones{} de los archivos
# existe la opcion del endswith, pero implica saber largo del texto
tipos = set([str(i).split('.')[-1] for i in glob.glob('*.*')])

# aquellos archivos que no se agregaran, en este caso son los comprimidos.
no_tipos = (['zip', 'tar', 'gz', 'rar', '7z', 'bz2'])

# es muy probable que pandas tenga una funcion que haga un mix entre ambas variables
# en este instante estan seteadas como "set{}" y no listas[], son iterables
# pero no se puede realizar slice. eventualmente se puede cambiar la forma
# https://docs.python.org/3.7/library/stdtypes.html#set-types-set-frozenset
print(lista, tipos)

# comprimir en archivos zip, separados.
for imagen in lista:
    # script para compresión, sin tener que abrir / cerrar archivo.
    # no es que comprima mucho, aprox 20-30%, pero agrupa.
    with zipfile.ZipFile(imagen+'.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        for ext in tipos:
            # chequea archivo existe, sino lo salta.
            archivo = ('').join(glob.glob(imagen + '*' + ext))
            print(archivo)
            # si existe archivo y no es un comprimido.
            if os.path.exists(archivo) and not ext in no_tipos:
                my_zip.write(archivo)
from glob import glob
import os
from zipfile import Zipfile
from numpy import arange

import tarfile
from tqdm import tqdm  # pip3 install tqdm

entDIR = '/home/disco2/version01_MOD13Q1/MOD13Q1/ENMASCARADO/'

os.chdir(entDIR)


def compress(tar_file, members):
    """
    Adds files (`members`) to a tar_file and compress it
    """
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:gz")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()


# obtener el listado unico{} de los archivos, independiente de extension
listado_tif = glob('**/*h12v12*.tif')

fechas = arange(1, 32, 16).tolist() + arange(305, 367, 16).tolist()
agnos = arange(2005, 2021)

listado2 = []
for fecha in fechas:
    listado2 = listado2 + [dia for dia in listado_tif if str(fecha).zfill(3) in dia]

listado3 = []
for agno in agnos:
    listado3 = listado3 + [img for img in listado2 if str(agno).zfill(4) in img]

listado3.sort()

for i in listado3:
    print('\n')
    print(i)

compress('/mnt/SEAGATE6TB/mod13Q1.tar', listado3)

for archivo listado_tif:
    with ZipFile('/mnt/SEAGATE6TB/mod13q1.zip') as myzip:
        with myzip.open(archivo) as myfile:
            print(myfile.read())

# obtener todas las extensiones{} de los archivos
# existe la opcion del endswith, pero implica saber largo del texto
# tipos = set([str(i).split('.')[-1] for i in glob.glob('*.*')])
tipos = ['tif']

# aquellos archivos que no se agregaran, en este caso son los comprimidos.
# no_tipos = (['zip', 'tar', 'gz', 'rar', '7z', 'bz2'])

# es muy probable que pandas tenga una funcion que haga un mix entre ambas variables
# en este instante estan seteadas como "set{}" y no listas[], son iterables
# pero no se puede realizar slice. eventualmente se puede cambiar la forma
# https://docs.python.org/3.7/library/stdtypes.html#set-types-set-frozenset
print(listado_tif, tipos)

with ZipFile(listado_tif, 'w') as myzip:
    myzip.write('eggs.txt')

