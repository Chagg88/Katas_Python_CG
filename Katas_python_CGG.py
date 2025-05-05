#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario 
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencia(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias


#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map

def doblar_lista(lista):
    nueva_lista = list(map(lambda x: x*2,lista))
    return nueva_lista

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra
#  objetivo.

def palabra_objetivo(lista_palabras,objetivo):
    resultado = []
    for palabra in lista_palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map

def diferencia_lista(lista1,lista2):
    return list(map(lambda x, y:x-y, lista1,lista2))


#5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, 
# que por defecto es 5. La función debe calcular la media de los números en la lista y determinar 
# si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, 
# será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def media_estado(lista_numeros,nota_aprobado=5):
    suma = sum(lista_numeros)
    cantidad = len(lista_numeros)
    media = suma / cantidad

    if media >= nota_aprobado:
        estado = "Aprobado"
    else:
        estado = "Suspenso"

    return (media,estado)


#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)


#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map

def tuplas_a_strings(lista_tuplas):
    lista_strings = list(map(lambda tupla: " ".join(tupla), lista_tuplas))
    return lista_strings


#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa
#  un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. 
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir():
    try:
        num1 = float(input("Introduce el primer número"))
        num2 = float(input("Introduce el segundo número"))
        resultado = num1/num2
    except ValueError:
        print("Error:debes ingresar números validos")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0")
    else:
        print(f"La división fue existosa: {resultado}")


#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva 
# lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es 
# ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter

def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache","Tigre","Serpiente Pitón","Cocodrilo","Oso"]
    lista_filtrada = list(filter(lambda mascota: mascota not in prohibidas, mascotas))
    return lista_filtrada


#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, 
# lanza una excepción personalizada y maneja el error adecuadamente.

def calcular_promedio(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return sum(lista)/ len(lista)


#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no 
# numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las
#  excepciones adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad"))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años")
    except ValueError as error:
        print(f"Error:{error}")
    else:
        print(f"Edad corecta: {edad}")


#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. 
# Usa la función map

def longitud_palabras(frase):
    palabras = frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada 
# letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map

def mayus_minus_unicas(caracteres):
    unicos = set(caracteres)
    resultado = list(map(lambda letra: (letra.upper(), letra.lower(), unicos)))
    return resultado

#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en
#  especifico. Usa la función filter

def palabras_con_letra(palabras,letra):
    resultado = list(filter(lambda palabra: palabra.startswith(letra), palabras))
    return resultado

#15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda x: x+3,lista))


#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva 
# una lista de todas las palabras que sean más largas que n. Usa la función filter

def palabras_largas(cadena, n):
    palabras =cadena.split()
    resultado = list(filter(lambda palabra: len(palabra) > n, palabras))
    return resultado


#17.  Crea una función lamda que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce

from functools import reduce

def lista_a_numero(lista_digitos):
    resultado = reduce(lambda x, y:x *10 + y, lista_digitos)
    return resultado
 

#18.  Escribe un programa en Python que cree una lista de diccionarios que contenga información de 
# estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes 
# con una calificación mayor o igual a 90. Usa la función filter

def estudiantes_excelentes(lista_estudiantes):
    resultado = list(filter(lambda estudiante: estudiante ["calificación"] >= 90, lista_estudiantes))
    return resultado

#19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))


#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int.
#  Usa la función filter

def filtrar_enteros(lista):
    resultado = list(filter(lambda x: isinstance(x,int), lista))
    return resultado


#21. Crea una función que calcule el cubo de un número dado mediante una función lamda

cubo = lambda x : x **3

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce

from functools import reduce

def producto_total(lista):
    return reduce (lambda x, y: x * y, lista)

#23. Concatena una lista de palabras.Usa la función reduce    

from functools import reduce

def concatenar_palabras(lista):
    return reduce (lambda x, y: x + y,lista)

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce 

from functools import reduce

def diferencia_total(lista):
    return reduce ( lambda x, y:x-y, lista)

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return(len(texto))


#26.  Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y


#27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set ()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None 

#29.  Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres 
# con el carácter '#', excepto los últimos cuatro.

def enmascarar(texto):
    texto = str(texto)
    if len (texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto [-4:]

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las 
# mismas letras pero en diferente orden.

def son_anagramas(palabra1,palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

#31.  Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre
# para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue 
# encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    nombres = input("Introduce una lista de nombre (separados por comas):").split(",")
    nombres = [nombre.strip() for nombre in nombres]

    nombre_buscar = input("Introduce el nombre a buscar:").strip()

    if nombre_buscar in nombres:
        print(f"El nombre {nombre_buscar} fue encontrado en la lista")
    else:
        raise ValueError(f"El nombre {nombre_buscar} no se encuentra en la lista")
    
try:
    buscar_nombre()
except ValueError as e:
    print(e)

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en
# la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje
# indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado ["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí"

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))


#34. Crea la clase arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos 
# disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_ramas y info_arbol. El objetivo es 
# implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    def __init__(self, longitud_tronco = 1):
        self.longitud_tronco = longitud_tronco
        self.ramas =[]
    def crecer_tronco(self):
        self.longitud_tronco += 1
        print("El tronco ha crecido")
    def nueva_rama(self, longitud = 1):
        self.ramas.append(longitud)
        print(f"Se ha añadido una nueva rama de longitud {longitud}")
    def crecer_ramas(self):
        if not self.ramas:
            print("El árbol no tiene ramas para crecer")
            return
        self.ramas = [longitud + 1 for longitud in self.ramas]
        print("Todas las ramas han crecido")
    def quitar_rama(self, indice):
        if 0 <= indice < len(self.ramas):
            rama_eliminada = self.ramas.pop(indice)
            print(f"Se ha eliminado la rama en la posicion {indice} (longitud {rama_eliminada})")
        else:
            print(f"No existe una rama en la posicion {indice}")
    def info_arbol(self):
        num_ramas = len(self.ramas)
        longitudes_ramas = ", ".join(map(str,self.ramas)) if self.ramas else "Ninguna"
        return (f"Información del árbol:\n"
                f"Longitud del tronco: {self.longitud_tronco}\n"
                f"Número de ramas:{num_ramas}\n"
                f"Longitudes de las ramas: {longitudes_ramas}")


#36. Crea la clase Usuario Banco,representa a un usuario de un banco con su nombre, saldo y si tiene o
# no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir 
# dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente
    
    def retirar_dinero (self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"{self.nombre} ha retirado {cantidad}. Saldo actual {self.saldo}")
        else: 
            print (f"{self.nombre} no tiene saldo suficiente. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            otro_usuario.saldo += cantidad
            print(f"{self.nombre} ha transferido {cantidad} a {otro_usuario.nombre}.")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para transferir.")

    def agregar_dinero (self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad} a su cuenta. El saldo actual es {self.saldo}.")

#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
# contar_palabras, reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos
# que definir primero y llamar dentro de la funcion procesar_texto

def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}
    for palabra in palabras:
        palabra_limpia = "".join(char for char in palabra if char.isalnum())
        if palabra_limpia:
            contador[palabra_limpia] = contador.get(palabra_limpia,0) + 1
    return contador

def reemplazar_palabras(texto,palabra_original, palabra_nueva):
    return texto.lower().replace(palabra_original.lower(),palabra_nueva.lower())

def eliminar_palabra (texto, palabra_a_eliminar):
    palabras = texto.lower().split()
    texto_filtrado = [palabra for palabra in palabras if palabra != palabra_a_eliminar.lower()]
    return " ".join(texto_filtrado)

def procesar_texto(texto,opcion,*args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) == 2:
            palabra_original, palabra_nueva = args
            return reemplazar_palabras(texto,palabra_original, palabra_nueva)
        else:
            print ("Error: Para la opción reemplazar se necesitan dos argumentos (palabra_original, palabra_nueva)")
            return None
    elif opcion == "eliminar":
        if len(args) == 1:
            palabra_a_eliminar = args[0]
            return eliminar_palabra(texto, palabra_a_eliminar)
        else:
            print ("Error: Para la opción eliminar se necesits un argumento (palabra_a_eliminar)")
            return None
    else: print (f"Opción {opcion} no válida")
    return None


#38.  Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el
# usuario.

def determinar_parte_día():
    hora = int(input("Introduce la hora (en formato de 24 horas):"))

    if 6 <= hora < 12:
        print("Es de día")
    elif 12 <= hora <18:
        print("Es de tarde")
    else:
        print("Es de noche")


#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación
# numérica. Las reglas de calificación son: (i) 0 a 69 insuficiente (ii) 70 a 79 bien (iii) 80 a 89 
# muy bien (iv) 90 a 100 excelente

def calificacion_texto():

    calificacion = int(input("Introduce la calificación númerica del alumno:"))

    if 0 <= calificacion <= 69:
        print("Insuficiente")
    elif 70 <= calificacion <= 79:
        print("Bien")
    elif 80 <= calificacion <= 89:
        print("Muy bien")
    elif 90 <= calificacion <= 100:
        print("Excelente")
    else:
        print("Calificación no valida, debe ser entre 0 y 100")

#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo"
# o "triangulo" y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area (figura,datos):
    if figura == "rectángulo":
        base, altura = datos
        return base * altura
    elif figura == "círculo":
        (radio,) = datos
        return math.pi * radio ** 2
    elif figura == "triángulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no válida")


#41 En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para
# determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. 
# El programa debe hacer lo siguiente:
#a. Solicita al usuario que ingrese el precio original de un artículo.
#b. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#c. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#d. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido
# (es decir, mayor a cero). Por ejemplo, descuento de 15€.
#e. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# f. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas 
# acciones en tu programa de Python.

def calcular_precio_final():
    precio_original = float(input("Introduce el precio original del artículo:"))
    tiene_cupon = input("¿Tienes cupón de descuento? (si/no)").lower()

    if tiene_cupon == "si":
        valor_cupon = float(input("Introduce el valor del cupón de descuento:"))

        if valor_cupon > 0:
            precio_final = precio_original - valor_cupon
            print("Se aplico un descuento de {valor_cupon} euros. El precio final es {precio_final} euros.")
        else:
            print("El valor del cupón no es válido, debe ser mayor a cero.")
            print("El precio final es {precio_original}")
    else:
        print("No tienes cupón. El precio final es {precio_original}")