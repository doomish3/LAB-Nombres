from collections import namedtuple

import csv

from datetime import datetime

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(fichero):
    res =[]
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=",")
        next(lector)
        for año,nombre,frecuencia,genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            res.append(FrecuenciaNombre(año,nombre,frecuencia,genero))
        return res
    

def filtrar_por_genero(nombres, genero):
    res = []
    for nombre in nombres:
        if nombre.genero == genero:
            res.append(nombre)
    return res


def calcular_nombres(nombres, genero = None):
    res = set()
    for n in nombres:
        if n.genero == genero:
            res.add(n.nombre)
        elif genero == None:
            res.add(n.nombre)
    return sorted(res)
