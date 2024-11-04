from nombres import *

def test_leer_frecuencias_nombres(fichero):
    registros = leer_frecuencias_nombres(fichero)
    print(f"Se ha leido {len(registros)} registros")
    print("Se leen los tres primero")
    print(registros[0])
    print(registros[1])
    print(registros[2])
    print("Se leen los tres ultimos")
    print(registros[-1])
    print(registros[-2])
    print(registros[-3])

def test_filtrar_por_genero(nombres, genero):
    registros = filtrar_por_genero(nombres, genero)
    print(f"Numero de registros para {genero}: {len(registros)}")


def test_calcular_nombres(nombres, genero=None):
    registros= calcular_nombres(nombres, genero)
    if genero == None:
        print(f"Ambos generos{registros[:10]}")
    else:
        print(f"Genero {genero}{registros[:10]}")





if __name__ == "__main__":
    Nombres = leer_frecuencias_nombres("./data/frecuencias_nombres.csv")
    #test_leer_frecuencias_nombres()
    #test_filtrar_por_genero(Nombres, "Hombre")
    #test_filtrar_por_genero(Nombres, "Mujer")
    test_calcular_nombres(Nombres)
    test_calcular_nombres(Nombres, "Hombre")
    test_calcular_nombres(Nombres, "Mujer")