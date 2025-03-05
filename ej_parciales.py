def posicion(l: list[str], nombre: str) -> int:
    longitud: int = len(l)
    for i in range(longitud):
        if l[i] == nombre:
            return i

def frecuencia_posiciones_caballos(caballos:list[str], carreras:dict[str, list[str]]) -> dict[str, list[int]]:
    res: dict[str, list[int]] = dict()
    longitud: int = len(caballos)
   
    for caballo in caballos:
        posicion_caballo = [0] * longitud
      
        for posiciones in carreras.values():
            indice = posicion(posiciones, caballo)
            posicion_caballo[indice] += 1
        res[caballo] = posicion_caballo
    
    return res

caballos = ["pepe", "diego", "franco"]
carreras = {
    "primera": ["pepe", "franco", "diego"],
    "segunda": ["franco", "diego", "pepe"],
    "tercera": ["diego", "pepe", "franco"],
    "cuarta": ["franco", "diego", "pepe"]
}
x = frecuencia_posiciones_caballos(caballos, carreras)
#print(x.items())

def matriz_capicua(m: list[list[int]]) -> bool:
    res:bool = True
    for fila in m:
        for i in range (len(fila)):
            if fila[i] != fila[len(fila)-i-1]:
                res = False
    return res

matriz = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
#print(matriz_capicua(matriz))


def encontrar_max_min(l: list[tuple[int, float]]) -> tuple[float, float]:
    min: float = 0
    max: float = 0
    for tupla in l:
        if tupla[1] > max:
            max = tupla[1]
    min = (l[0])[1]
    for tupla in l:
        if tupla[1] < min:
            min = tupla[1]
    res = tuple[min, max]
    return res
#print(encontrar_max_min([(3, 30), (4, 500), (4, 9000), (1, 15)]))

def valores_extremos(cotizaciones_diarias: dict[str, list[tuple[int, float]]]) -> dict[str, tuple[float, float]]:
    resultado: dict[str, tuple[float, float]] = dict()
    for clave in cotizaciones_diarias.keys():
        max_min: tuple[float, float] = encontrar_max_min(cotizaciones_diarias[clave]) 
        resultado[clave] = max_min
    return resultado

cotizaciones = {
    "mercadolibre": [[3, 5000], [5, 1000], [8, 10000]],
    "amazon": [[1, 10987], [13, 131313], [17, 100]],
    "netflix": [[1, 100], [2, 200], [3, 8000]]
}
resultado = valores_extremos(cotizaciones)
#print(resultado.values())

def hay_num_repetidos(l: list[int]) -> bool:
    res = False
    list_aux: list[int] = []
    for num in l:
        if not num in list_aux:
            list_aux.append(num)
        else:
            res = True
    return res
    
def es_sudoku_valido(m: list[list[int]]) -> bool:
    res = True
    # FILAS
    for linea in m:     
        list_aux: list[int] = []
        for num in linea:
            if num != 0:
                list_aux.append(num)
        if hay_num_repetidos(list_aux):
                res = False
        list_aux.clear()
    # COLUMNAS
    for indice in range(9):
        lista_aux: list[int] = []
        for linea in m:
            if linea[indice] != 0:
               lista_aux.append(linea[indice])
        if hay_num_repetidos(lista_aux):
            res = False
        lista_aux.clear()
    
    return res

m = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
]
#print(es_sudoku_valido(m))

def cuenta_posiciones_por_nacion(naciones: list[str], torneos:dict[int, list[str]]) -> dict[str, list[int]]:
    res: dict[str, list[int]] = dict()
    for nacion in naciones:
        conteo: list[int] = [0]*len(naciones)
        for valor in torneos.values():
            posicion_nacion:int = posicion(valor, nacion)
            conteo[posicion_nacion] += 1
        res[nacion] = conteo
    return res

naciones= ["arg", "aus", "nz", "sud"]
torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
x = cuenta_posiciones_por_nacion(naciones, torneos)
#print(x.items())

def alguno_posicion_par(l: list[int], elem: int) -> bool:
    for indice in range (len(l)):
        if l[indice] == elem:
            if indice%2 == 0:
                return True
    return False

def elem_en_posiciones_pares(m: list[list[int]], elem: int) -> list[bool]:
    list_bool: list[bool] = []
    for fila in m:
        if alguno_posicion_par(fila, elem):
            list_bool.append(True)
        else:
            list_bool.append(False)
    return list_bool

elem= 1; M = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 1, 0, 0, 6, 0, 0, 1, 0],
]
#print(elem_en_posiciones_pares(M, elem))

def contador_lista(l: list[list[str]], elem: str) -> int:
    contador: int = 0
    for lista in l:
        for nombre in lista:
            if elem == nombre:
               contador += 1
    return contador

def dias_viajados(viajes_diarios: dict[int, list[str]], usuarios:list[str]) -> dict[str,int]:
    res: dict[str, int] = dict()
    valores: list[list[str]] = viajes_diarios.values()
    for usuario in usuarios:
           contador: int = contador_lista(valores, usuario)
           res[usuario] = contador
    return res

viajes_diarios = {1 : ["Juan", "Maria"], 2 : ["Marcela","Juan"]}
usuarios = ["Juan", "Maria", "Marcela"]

x = dias_viajados(viajes_diarios, usuarios)
#print(x.items())

from queue import Queue as Cola

def duplicar_cola(c: Cola) -> Cola:
    duplicado = Cola()
    while not cola.empty():
        n = c.get()
        c.put(n)
        duplicado.put(n)
    return duplicado

def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str, str]]) -> Cola[str]:
    res: Cola[str] = Cola()
    duplicado: Cola[str, str] = duplicar_cola(filaClientes)
    while not duplicado.empty():
        elem: tuple[str, str] = duplicado.get()
        if elem[1] == "vip":
            res.put(elem[0])
    duplicado_v2 = duplicar_cola(filaClientes)
    while not duplicado_v2.empty():
        elem_v2: tuple[str, str] = duplicado_v2.get()
        if elem_v2[1] == "comun":
            res.put(elem_v2[0])
    return res

cola = Cola()
cola.put(["pepe", "vip"])
cola.put(["jose", "comun"])
cola.put(["fernando", "vip"])    
x = reordenar_cola_priorizando_vips(cola)
print(x.queue)

#def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
 #   res: dict[str, int] = dict()

def columna(indice: int, m: list[list[str]]) -> list[str]:
    res: list[str] = []
    for fila in m:
        res.append(fila[indice])
    return res

def hay_3_en_forma_consecutiva (l: list[str], simbolo: str) -> bool:
    list_de_simbolo: list[str] = []
    for elem in l:
        if elem == simbolo:
            list_de_simbolo.append(elem)
        else:
            list_de_simbolo.clear()
        if len(list_de_simbolo) == 3:
            return True
    return False

def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    res: list[int] = []
    indices_de_column: int = len(tablero)
    for i in range (indices_de_column):
        colum: list[str] = columna(i, tablero)
        if hay_3_en_forma_consecutiva(colum, "X") and hay_3_en_forma_consecutiva(colum, "O"):
            return 3
        elif hay_3_en_forma_consecutiva(colum, "x"):
            res.append(1)
        elif hay_3_en_forma_consecutiva(colum, "O"):
            res.append(2)
    if 1 in res and 2 in res:
        return 3
    elif 1 in res:
        return 1
    elif 2 in res:
        return 2
    return 0

def separar_por_palabras(texto: str) -> list[str]:
    res: list[str] = []
    list_aux: list[str] = []
    for caracter in texto:
        if caracter != " ":
            list_aux.append(caracter)
        elif caracter == " " and len(list_aux) > 0:
            res.append(list_aux)
            list_aux = []
    return res

print(separar_por_palabras("hola como andas loco "))



#def cuantos_palindromos_sufijos(texto: str, int) -> int:
