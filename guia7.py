# PRIMERA PARTE

def pertenece (s: list[int], e: int) -> bool:
    indice: int = 0
    longitud:int = len(s)
    for n in range (indice, longitud):
        if (e == s[n]):
          return True 
    return False

def pertenecev2(s:list[int], e: int) -> bool:
    indice: int = 0
    longitud:int = len(s)
    while (indice < longitud):
        if (e == s[indice]):
            return True
        indice += 1
    return False

def divide_a_todos(s:list[int], e:int) -> bool:
    indice = 0
    longitud = len(s)
    for i in range (indice, longitud):
        if (s[i] % e != 0):
           return False
    return True

def suma_total(s:list[int]) -> int:
    indice: int = 0
    sumatotal: int = 0
    longitud: int = len(s)
    for i in range (indice, longitud):
        sumatotal: int = sumatotal + s[i]
    return sumatotal
#print(suma_total([2, 3, 5, 7]))

def suma_totalv2(s:list[int]) -> int:
    indice: int = 0
    sumatotal: int = 0
    longitud: int = len(s)
    while (indice < longitud):
        sumatotal: int = sumatotal + s[indice]
        indice += 1
    return sumatotal

def ordenados(s:list[int]) -> bool:
    indice: int = 0
    longitud: int = len(s)
    for i in range (indice, longitud-1):
        if (s[i] >= s[i +1 ]):
            return False
    return True

def long_mayor_7(s:list[str]):
    indice: int = 0
    longitud: int = len(s)
    while (indice < longitud):
        if (len(s[indice]) > 7):
            return True
        indice += 1
    return False

def invertir(texto:str) -> str:
    inverso = ""
    letras: int = len (texto)
    for i in range (letras-1, -1, -1):
        inverso = inverso + texto[i]
    return inverso
print(invertir("pinguino"))

def palindromo(palabra: str) -> bool:
    if (palabra == invertir(palabra)):
        return True
    else:
        return False

def fortaleza_contraseña(contraseña: list) -> str:
    longitud: int = len(contraseña)
    indice: int = 0
    res1 = res2 = res3 = False
    for l in range (indice, longitud):
        if (contraseña[l] >= "a" and contraseña[l] <= "z"):
            res1: bool = True
        if (contraseña[l] >= "A" and contraseña[l] <= "Z"):
            res2: bool = True
        if (contraseña[l] >= "1" and contraseña[l] <= "9"):
            res3: bool = True
    if (res1 and res2 and res3):
        return "VERDE"
    elif (longitud > 8):
        return "AMARILLA"
    else:
        return "ROJA"

def cuenta_bancaria(s:list[tuple[str, int]]) -> int:
    total: int = 0
    indice: int = 0
    longitud: int = len(s)
    for n in range (indice, longitud):
        if ((s[n])[0] == "I"):
            total = total + (s[n])[1]
        if ((s[n])[0] == "R"):
            total = total - (s[n])[1]
    return total

def tres_vocales_distintas(palabra:str) -> bool:
    total: int = 0
    if (pertenece(palabra, "a")):
            total = total + 1
    if (pertenece(palabra, "e")):
            total = total + 1
    if (pertenece(palabra, "i")):
            total = total + 1
    if (pertenece(palabra, "o")):
            total = total + 1
    if (pertenece(palabra, "u")):
            total = total + 1
    if (total >= 3):
            return True
    else:
            return False
        
# SEGUNDA PARTE

def reemplazar_par_por_0v2(s:list[int]) -> list[int]:
     indice: int = 0
     longitud: int = len(s)
     nuevo: list[int] = []
     for n in range (indice, longitud):
          if (s[n]%2 == 0):
               nuevo = nuevo + [0]
          else:
               nuevo = nuevo + [s[n]]
     return nuevo 

def reemplazar_par_por_0(s:list[int]) -> list[int]:
     indice: int = 0
     longitud: int = len(s)
     for n in range (indice, longitud): 
          if (s[n] % 2 == 0):
               s[n] = 0
     return s

def es_vocal(letra: str) -> bool:
     if letra == "a":
          return True
     if letra == "e":
          return True
     if letra == "i":
          return True
     if letra == "o":
          return True
     if letra == "u":
          return True
     else:
          return False
          
def sin_vocales(palabra:str) -> str:
     indice: int = 0
     longitud: int = len(palabra)
     nuevapalabra: str = []
     for i in range (indice, longitud):
          if es_vocal(palabra[i]) == False:
               nuevapalabra = nuevapalabra + [palabra[i]]
          else:
               nuevapalabra
     return nuevapalabra

def dar_vuelta_str(a:str) -> str:
     longitud: int = len(a)
     indice: int = 0
     res: str = []
     while (indice < longitud):
          res = res + [a[longitud - indice - 1]]
          indice += 1
     return res
     
def es_repetido(s:str, t:str) -> bool:
     indice: int = 0
     longitud: int = len(t)
     apariciones: int = 0
     for n in range (indice, longitud):
          if s == t[n]:
               apariciones = apariciones + 1
     if apariciones > 1:
          return True 

def eliminar_repetidos(s:str) -> str:
     indice: int = 0
     longitud: int = len(s)
     sinrepetir: str = []
     for n in range (indice, longitud):
               if(pertenece (sinrepetir, s[n])):
                     sinrepetir = sinrepetir 
               else:
                    sinrepetir = sinrepetir + [s[n]]
     return sinrepetir

# TERCERA PARTE

def notas_mayora4(n:list[int]) -> bool:
     indice: int = 0
     longitud: int = len(n)
     for i in range (indice, longitud):
          if (n[i] < 4):
               return False
     return True
          
def promedio_notas(s:list[int]) -> int:
     indice: int = 0
     longitud: int = len(s)
     total: int = 0
     for i in range (indice, longitud):
          total = total + s[i]
     return total / longitud
          
def aprobado(s:list[int]) -> int:
     if (notas_mayora4(s) and promedio_notas(s) >= 7):
          return 1
     if (notas_mayora4(s) and (promedio_notas(s) <= 7 or promedio_notas(s) >= 4)):
          return 2
     if ((notas_mayora4(s) == False) or promedio_notas(s) < 4):
          return 3
#print(aprobado([4, 3, 6, 4, 7]))

# CUARTA PARTE

def estudiantes() -> list[str]:
     estudiantes_ingresados: list[str] = []
     user_input: str = input ("ingresar estudiante: ")
     while (user_input != "listo"):
          estudiantes_ingresados.append(user_input)
          user_input: str = input ("ingresar estudiante: ")
     return estudiantes_ingresados
     
def historial_SUBE() -> list[tuple[str, int]]:
     historial: list[tuple[str, int]] = []
     user_input: str = ""

     while user_input != "X":
          print("Ingrece 'letra' para operar.")
          print("Ingrese 'C' para cargar.")
          print("Ingrese 'D' para descontar.")
          print("Ingrese 'X' para terminar.")
        
          user_input = input ("ingresar letra: ")
          if user_input == "C":
               cargar: int = input ("Ingrese monto a cargar: $")
               historial.append(("C", cargar))
          elif user_input == "D":
               descontar: int = input ("Ingrese monto a descargar: $")
               historial.append(("D", descontar))
     return historial 

# QUINTA PARTE

def pertenece_a_cada_uno_v1(s:list[list[int]], e:int, res:list[bool]) -> None:
     res.clear()
     for n in s:
            res.append(pertenece(n, e))

# SEXTA PARTE
def es_matriz(s:list[list[int]]) -> bool:
    res = True
    for n in s:
         if (len(n) != len(s[0])): 
               res = False
    return res

def filas_ordenadas(s:list[list[int]], res:list[bool]) -> None:
     res.clear()
     for n in s:
          res.append(ordenados(n))

def columna_de_matriz(m:list[list[int]], columna: int) -> list[int]:
     columna_res: list[int] = []
     for fila in m:
          columna_res.append(fila[columna]) 
     return columna_res

def sumar_columnas_matriz(m: list[list[int]]) -> list[int]:
     cant_colum: int = len(m[0])
     n_columna: int = 0
     filas: int = len(m)
     total_aux: int = 0
     res: list[int] = []
     for columna in range (n_columna, cant_colum):
          lista_colum: list[int] = columna_de_matriz(m, columna)
          for elem in range (0, filas):
               total_aux += lista_colum[elem]
          res.append(total_aux)
          total_aux = 0
     return res







               
          







