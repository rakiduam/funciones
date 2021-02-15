#!/usr/bin/python
import pandas as pd
from datetime import datetime


def fecha_cercana(fecha_buscar, lista_donde):
    """
    fecha_buscar: fecha en formato YYYYmmdd , cualquier otra cosa es necesario preprocesar
    lista_donde: listado de fechas en el mismo formato YYYYmmdd ej: 20201231
    devuelve el valor mas cercano de la fecha que se esta buscando
    """
    fecha_buscar = datetime(int(fecha_buscar[:4]), int(fecha_buscar[4:6]), int(fecha_buscar[6:]))
    lista_donde.sort()
    # b = lista_donde.copy()
    b = lista_donde[:]
    b = pd.DataFrame(b, columns=['col1'], index=pd.to_datetime(b, format='%Y%m%d'))
    idx = b.index.get_loc(fecha_buscar, method='nearest')
    return(lista_donde[idx])

