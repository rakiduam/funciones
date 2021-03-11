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
