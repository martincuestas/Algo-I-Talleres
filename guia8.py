# PILAS
from queue import LifoQueue as Pila

import random

def generar_numeros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila [int]:
    miPila = Pila()
    while cantidad > 0:
        n = random.randint(desde, hasta)
        miPila.put(n)
        cantidad -= 1
    return miPila

x = generar_numeros_al_azar(5, 3, 13)
#print(x.queue)

def duplicar(p: Pila) -> Pila:
    paux = Pila()
    while (not p.empty()):
        n = p.get() 
        paux.put(n)
    duplicado = Pila()
    while (not paux.empty()):
        m = paux.get()
        duplicado.put(m)
        p.put(m)
    return duplicado 

mipila = Pila()
mipila.put(3)
mipila.put(8)
x = duplicar(mipila)
#print(x.queue)


def cantidad_elementos(p: Pila) -> int:
    ps = duplicar(p)
    contador: int = 0
    while (not ps.empty()):
        ps.get()
        contador += 1
    return contador

mipilar = Pila()
mipilar.put(9)
mipilar.put(11)
#print(cantidad_elementos(mipilar))

def buscar_el_maximo(p:Pila[int]) -> int:
    candidato: int = ps.get()
    ps = duplicar (p)
    while not ps.empty():
       elemento = ps.get()
       if elemento > candidato:
          candidato = elemento
    return candidato

mipilare = Pila()
mipilare.put(9)
mipilare.put(89)
mipilare.put(66)
mipilare.put(12)
#print(buscar_el_maximo(mipilare))

def esta_bien_balanceada(s:str) -> bool:
    pila = Pila()
    contador: int = 0
    for char in s:
        if char == "(":
            pila.put(char)
        elif char == ")":
            if pila.empty():
                return False
            pila.get()
    if pila.empty():
        return True
    else:
        return False
#print(esta_bien_balanceada("1 + ( 2 x 3 - ( 2 0 / 5 ) )"))
#print(esta_bien_balanceada("10 ∗ ( 1 + ( 2 ∗ ( −1)))"))
#print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))


def pertenece (s: list, e) -> bool:
    longitud:int = len(s)
    for n in range (longitud):
        if (e == s[n]):
          return True 
    return False


def sacar_espacios(s:str) -> str:
    res: str = []
    for char in s :
        if char != " ":
            res.append(char)
    return res

def evaluar_expresion(s:str) -> float:
    duplicado_sinespacios: str = sacar_espacios(s)
    pila = Pila()
    res: int = 0
    for char in duplicado_sinespacios:
        if (char != "+" and char != "-" and char != "*" and char != "/"):
            pila.put(char)
        if char == "+":
            res = float(pila.get()) + float(pila.get())
            pila.put(res)
        if char == "-":
            res = - float(pila.get()) + float(pila.get())
            pila.put(res)
        if char == "*":
            res = float(pila.get()) * float(pila.get())
            pila.put(res)
        if char == "/":
            a = float(pila.get())
            b = float(pila.get())
            res = b / a
            pila.put(res)
    pila.get(res)
    return res
#print(evaluar_expresion("3 4 + 5 * 5 / 5 +"))
#print(evaluar_expresion("3 7 +"))                
                
# COLAS

from queue import Queue as Cola

def generar_numeros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola [int]:
    cola = Cola()
    while cantidad > 0:
        n = random.randint(desde, hasta)
        cola.put(n)
        cantidad-=1
    return cola
x=generar_numeros_al_azar(7, 2, 20)
#print(x.queue)

def duplicar_cola(c: Cola) -> Cola:
    caux = Cola()
    duplicado = Cola()
    while not c.empty():
        n = c.get()
        caux.put(n)
    while not caux.empty():
      b = caux.get()
      c.put(b)
      duplicado.put(b)
    return duplicado

def cantidad_de_elementos(c:Cola) -> int:  # SIN USAR DUPLICADO PARA PROBAR
    cantidad: int = 0
    caux = Cola()
    while not c.empty():
        n = c.get()
        cantidad += 1
        caux.put(n)
    while not caux.empty():
      b = caux.get()
      c.put(b)
    return cantidad

def buscar_maximo_cola(c:Cola[int]) -> int:
    copia = duplicar_cola(c)
    candidato = copia.get()
    while not copia.empty():
        elem = copia.get()
        if elem > candidato:
            candidato = elem
    return candidato
x = Cola()
x.put(33)
x.put(8)
x.put(109)
x.put(1)
#print(buscar_maximo_cola(x))

def pertenece_cola(c:Cola, i) -> bool:
    colaux = duplicar_cola(c)
    res: bool = False
    while not colaux.empty():
        n = colaux.get()
        if n == i:
            res = True
    return res

def armar_secuencia_de_bingo() -> Cola[int]:
    res: Cola = Cola()
    total: int = 100
    while total > 0:
        n_azar: int = random.randint(0, 99)
        if not pertenece_cola(res, n_azar):
            res.put(n_azar)
            total-=1
    return res

x = armar_secuencia_de_bingo()
#print(x.queue)

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    bolilleroaux = duplicar_cola(bolillero)
    carton_nums: int = 12
    while carton_nums > 0:
        n: int = bolilleroaux.get() 
        if pertenece(carton, n):
            carton_nums -=1
        jugadas += 1
    return jugadas 

bolillero = armar_secuencia_de_bingo()
print(jugar_carton_de_bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], bolillero))

def n_pacientes_urgentes(c: Cola[(int, str, str)]) -> str:
    copia = duplicar_cola(c)
    contador: int = 0
    while not copia.empty():
        n: tuple[int, str, str] = copia.get()
        if n[0] >0 and n[0] < 4:
                contador +=1
    return contador
cola = Cola()
cola.put((5, "hola", "chau"))
cola.put((2, "holanda", "chauu"))
cola.put((1, "jeje", "a"))
#print(n_pacientes_urgentes(cola))

def atencion_a_clientes(c : Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    copia: Cola = duplicar_cola(c)
    ordenada: Cola = Cola()
    reserva: Cola = Cola()
    reserva2: Cola = Cola()
    while not copia.empty():
        n: tuple[str, int, bool, bool] = copia.get()
        if n[3] == True:
            ordenada.put(n)
        else:
            reserva.put(n)
    while not reserva.empty():
        m: tuple[str, int, bool, bool] = reserva.get()
        if m[2] == True:
            ordenada.put(m)
        else: 
            reserva2.put(m)
    while not reserva2.empty():
        k: tuple[str, int, bool, bool] = reserva2.get()
        ordenada.put(k)
    return ordenada

clientes = Cola()
clientes.put(("Ana", 30, False, False))
clientes.put(("Carlos", 70, False, False))
clientes.put(("Beatriz", 28, True, False))
clientes.put(("Daniel", 45, False, True))
clientes.put(("Elena", 65, False, True))
clientes.put(("Fernando", 50, False, False))
cola_atendidos = atencion_a_clientes(clientes)
#print(cola_atendidos.queue)

# ARCHIVOS

import typing

#def contar_lineas(nombre_archivo: str) -> int:
 #   arch: typing.IO = open(nombre_archivo, "r")
  #  res: int = len(arch.readlines())
   # arch.close()
    #return res
#print(contar_lineas("hola.txt"))

def separar_palabras(texto: str) -> list[str]:
    res: list[str] = []
    resaux: str = ""
    for caracter in texto:
        if not caracter in " \n\r\t":
            resaux += (caracter)
        elif caracter in " \n\r\t" and (len(resaux) > 0):
            res.append(resaux)
            resaux = ""
    if len(resaux) > 0:
        res.append(resaux)
    return res
print(separar_palabras("hola  como anda usted"))

def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
     arch: typing.IO = open(nombre_archivo, "r")
     lineas: list[str] = arch.readlines()
     res = False
     for linea in lineas:
         words: list[str] = separar_palabras(linea)
         for word in words:
             if word == palabra:
                 res = True
     arch.close()
     return res
#print(existe_palabra("hola", "hola.txt"))

def cantidad_de_apariciones(nombr_archivo: str, palabra:str) -> int:
    arch: typing.IO = open(nombr_archivo, "r")
    lineas: list[str] = arch.readlines()
    conteo: int = 0
    for line in lineas:
        words: list[str] = separar_palabras(line)
        print(words)
        for word in words:
            if word == palabra:
                conteo += 1
    arch.close()
    return conteo
#print(cantidad_de_apariciones("hola.txt", "san"))

def es_comentario(linea: str) -> bool:
    for i in linea:
        if i == "#":
            return True
        elif i != " ":
            return False
    return False


def clonar_sin_comentarios(nombre_archivo: str):
    archivo: typing.IO = open(nombre_archivo, "r")
    archivo_sin_comentarios: typing.IO = open("archivo_clonado", "w")
    lineas: list[str] = archivo.readlines()
    for linea in lineas:
        if not es_comentario(linea): 
            archivo_sin_comentarios.write(linea)
        archivo.close()
        archivo_sin_comentarios.close()

def invertir_lineas(nombre_archivo: str) -> None:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    longitud: int = len(lineas)
    archivo.close()
    reverso: typing.IO = open('reverso.txt', "w")
    for i in range (longitud-1, -1, -1):
        reverso.write(lineas[i])
    reverso.close()
    # PARA PROBAR SI ANDA:
    reverso = open('reverso.txt', "r")
    print(reverso.readlines())
    reverso.close()
#invertir_lineas("hola.txt")

def agregar_frase_al_final(nombre_archivo: str, frase: str) -> None:
    arch: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = arch.readlines()
    arch.close()
    arch: typing.IO = open(nombre_archivo, "w")
    for linea in lineas:
      arch.write(linea)
    arch.write(frase)
    arch.close()

#agregar_frase_al_final("hola.txt", " perro")

def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    arch: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = arch.readlines()
    arch.close()
    arch: typing.IO = open(nombre_archivo, "w")
    arch.write(frase)
    for linea in lineas:
      arch.write(linea)
    arch.close()
#agregar_frase_al_principio("hola.txt", "SAPE LOQUITA ")

def es_legible(char: str) -> bool:
    res: bool = False
    if ((char >= 0 and char <= 9) or (char >= "a" and char <= "z") or (char >= "A" and char <= "Z") or (char == " ") or (char == "_")):
        res = True
    return res

def listar_palabras_de_archivos(nombre_archivo: str) -> list:
    resultado: list[str] = []
    palabra_legible = ""

    archivo_exe = open(nombre_archivo, "rb")
    bytes_contentido: str = archivo_exe.read()
    archivo_exe.close()

    for byte in bytes_contentido:
        caracter = chr(byte)
        if es_legible(caracter):
            palabra_legible += caracter
        else:
            if len(palabra_legible) >= 5:
               resultado.append(palabra_legible)
               palabra_legible = ""
    if len(palabra_legible) > 0:
        resultado.append(palabra_legible)
    return resultado

def obtener_datos_alumno(datos_csv: str) -> list[str]:    # CONVIERTE DATOS SEPARADOS POR , EN LISTAS DE STR
    datos_alumno:list[str] = []
    dato: str = ""
    for caracter in datos_csv:
        if caracter in ',\n' and len(dato) > 0:
            datos_alumno.append(dato)
            dato:str = ""
        elif caracter != ",\n":
            dato += caracter
    if len(dato) > 0:
        datos_alumno.append(dato)
    return datos_alumno

def promedio_estudiante(nombre_archivo: str, lu: str) -> float:
    total_nota: float = 0
    cantidad_notas: int = 0
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    for linea in lineas:
        informacion: list[str] = obtener_datos_alumno(linea)
        if informacion[0] == lu:
            total_nota += informacion[3]
            cantidad_notas += 1
    promedio: float = total_nota / cantidad_notas 
    return promedio

def calcular_promedio_por_estudiante(nombre_achivo_notas: str, nombre_archivo_promedio: str) -> None:
    archivo: typing.IO = open(nombre_achivo_notas, "r")
    archivo_promedio = open(nombre_archivo_promedio, "w")
    lineas: list[str] = archivo.readlines()
    lista_nombres: list[str] = []
    for linea in lineas:
      if len(linea) > 0:
          datos_alumno: list[str] = obtener_datos_alumno(linea)
          lu: str = datos_alumno[0]
          if not lu in lista_nombres:
              lista_nombres += lu
              archivo_promedio.write(lu + "," + str(promedio_estudiante(lu)) + "\n")
    archivo.close()
    archivo_promedio.close()

# DICCIONARIOS

def pertenece_dict(d: dict, k) -> bool:
    lista = list (d.keys())
    for e in lista:
        if e == k:
            return True
    return False

def palabras_archivo(nombre_archivo: str) -> list[str]:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    palabras: list[str] = []
    for linea in lineas:
        palabras_sep: list[str] = separar_palabras(linea)
        palabras += palabras_sep
    archivo.close()
    return palabras

print(palabras_archivo("hola.txt"))

def agrupar_por_longitud(nombre_archivo: str) -> dict:
    listapalabras: list[str] = palabras_archivo(nombre_archivo)
    resultado: dict[int, int] = dict()
    for palabra in listapalabras:
        largo_palabra = len(palabra)
        if largo_palabra in resultado.keys():
            resultado[largo_palabra] += 1
        else:
            resultado[largo_palabra] = 1
    return resultado
print(agrupar_por_longitud("hola.txt"))

def calcular_promedio_por_estudiante(nombre_archivo_notas: str) -> dict[str, float]:
    res: dict[str, float] = dict()
    arch: typing.IO = open(nombre_archivo_notas, "r")
    lineas: list[str] = arch.readlines()
    for linea in lineas:
        if len(linea) > 0:
            datos: list[str] = obtener_datos_alumno(linea)
            alumno: str = datos[0]
            if not alumno in res.keys():
                res[alumno] = promedio_estudiante(nombre_archivo_notas, alumno)
    return res

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    arch: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = arch.readlines()
    repeticiones: dict[str, int] = dict()
    arch.close()
    for linea in lineas:
        palabras: list[str] = separar_palabras(linea)
        for palabra in palabras:
            if palabra in repeticiones.keys():
                repeticiones[palabra] += 1
            else:
                repeticiones[palabra] = 1
    mayor: int = 0
    clave_candidato: str = ""
    for clave in repeticiones.keys():
        if repeticiones[clave] > mayor:
            mayor = repeticiones[clave]
            clave_candidato = clave
    return clave_candidato
print(la_palabra_mas_frecuente("hola.txt"))

def visitar_sitio(historiales:dict[str, Pila[str]], usuario:str, sitio:str) -> None:
        if not usuario in historiales.keys():
            historial: Pila[str] = Pila()
            historial.put(sitio)
            historiales[usuario] = historial
        else:
            historiales[usuario].put(sitio)

def navegar_atras(historiales: dict[str, Pila[str]], usuario:str):
    for clave in historiales.keys():
        if usuario == clave:
            ultimo_sitio = historiales[usuario].get()
            anteultimo_sitio = historiales[usuario].get()
            historiales[usuario].put(ultimo_sitio)
            historiales[usuario].put(anteultimo_sitio)

historiales = {}
visitar_sitio(historiales, "martin", "google.com")
visitar_sitio(historiales, "martin", "clubpenguin.com")
visitar_sitio(historiales, "martin", "youtube.com")
for valor in historiales.values():
    print(valor.queue)

navegar_atras(historiales, "martin")
for valor in historiales.values():
    print(valor.queue)

def agregar_producto(inventario:dict[str, dict:[str, int]], nombre:str, precio:float, cantidad: int):
    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad
    }

def actualizar_stock(inventario:dict[str, dict:[str, int]], nombre:str, cantidad: int):
    for clave in inventario.keys():
        if clave == nombre:
            (inventario[clave])["cantidad"] = cantidad

def cantidad_x_precio(diccionario: dict[str, int|float]) -> float:
    return diccionario["cantidad"] * diccionario["precio"]

def calcular_valor_inventario(inventario:dict[str, dict:[str, int]]) -> float:
    total: float = 0
    for clave in inventario.keys():
        total += cantidad_x_precio(inventario[clave])
    return total


inventario = {}
agregar_producto(inventario, "papasfritas", 2000, 3)
agregar_producto(inventario, "carnedepinguino", 30000, 5)
agregar_producto(inventario, "heladodefernet", 900, 11)
print(inventario.keys())
print(inventario.values())
actualizar_stock(inventario, "papasfritas", 30)
print (inventario.values())
print(calcular_valor_inventario(inventario))


