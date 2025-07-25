def lists_exercises():
    print("Ejercicios de listas")
    #LISTS:
    #Exercise 1.1
    frutas = ["manzana", "banana", "cereza", "melocotón", "sandía"]

    print(f"{frutas}")
    ultima_fruta = frutas[len(frutas) - 1]
    print(f"La última fruta es: {ultima_fruta}")

    frutas[1] = "fresa"
    print(f"Lista de frutas actualizada: {frutas}")
    frutas[1] = "banana"

    frutas.append("kiwi")
    print(f"Lista de frutas después de añadir kiwi: {frutas}")

    frutas.remove("banana")
    print(f"Lista de frutas después de eliminar banana: {frutas}")

    if "manzana" in frutas:
        print("La lista contiene manzana")
    else:
        print("La lista no contiene manzana")

    #Exercise 1.2
    numeros = [10, 5, 8, 12, 3, 20, 1]
    print(f"Números originales: {numeros}")
    numeros_pares = []
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    print(f"Números pares: {numeros_pares}")
    dobles = []
    for numero in numeros:
        dobles.append(numero * 2)
    print(f"Números dobles: {dobles}")

    print(f"Números ordenados: {sorted(numeros)}")


def tuples_exercises():
    print("Ejercicios de tuplas")
    # TUPLES:
    #Exercise 2.1
    punto = (5, -2, 10)
    print(f"Punto: {punto}")

    print(f"Coordenada y: {punto[1]}")

    try:
        punto[0] = 7
    except TypeError as e:
        print(f"Error al intentar modificar el punto: {e}")

    colores = ("rojo", "verde", "azul")
    print(f"Colores: {colores}")

    colores_nuevos = colores + ("amarillo", "naranja")
    print(f"Colores nuevos: {colores_nuevos}")

    #Exercise 2.2
    informacion_producto = ("PC", 1200.50, 20)
    print(f"Información del producto: {informacion_producto}")

    nombre_producto = informacion_producto[0]
    precio_producto = informacion_producto[1]
    cantidad_producto = informacion_producto[2]
    print(f"Nombre del producto: {nombre_producto}")
    print(f"Precio del producto: {precio_producto}")
    print(f"Cantidad del producto: {cantidad_producto}")


def sets_exercises():
    print("Ejercicios de conjuntos")
    # SETS:
    #Exercise 3.1
    numeros_repetidos = [1, 2, 2, 3, 4, 4, 5, 1]
    print(f"Números repetidos: {numeros_repetidos}")

    numeros_unicos = set(numeros_repetidos)
    numeros_unicos.add(6)
    print(f"Números únicos: {numeros_unicos}")

    numeros_unicos.add(2) # it will not be added again

    #Exercise 3.2
    estudiantes_programacion = {"Alice", "Bob", "Charlie", "David"}
    print(f"Estudiantes que cursan programación: {estudiantes_programacion}")
    estudiantes_matematicas = {"Charlie", "Eve", "Frank", "Alice"}
    print(f"Estudiantes que cursan matemáticas: {estudiantes_matematicas}")

    print(f"Estudiantes que cursan programación y matemáticas: {estudiantes_programacion.intersection(estudiantes_matematicas)}")
    print(f"Estudiantes que cursan programación o matemáticas: {estudiantes_programacion.union(estudiantes_matematicas)}")
    print(f"Estudiantes que cursan programación pero no matemáticas: {estudiantes_programacion.difference(estudiantes_matematicas)}")


def dictionaries_exercises():
    print("Ejercicios de diccionarios")
    # DICTIONARIES:
    #Exercise 4.1
    informacion_persona = {
        "nombre": "Ana",
        "edad": 28,
        "ciudad": "Madrid"
    }
    print(f"Información de la persona: {informacion_persona}")
    print(f"Edad: {informacion_persona["edad"]}")
    informacion_persona.update({"profesion": "Ingeniera"})
    print(f"Información de la persona actualizada: {informacion_persona}")
    informacion_persona["edad"] = 29
    print(f"Información de la persona después de actualizar la edad: {informacion_persona}")
    informacion_persona.pop("ciudad")
    print(f"Información de la persona después de eliminar la ciudad: {informacion_persona}")

    #Exercise 4.2
    inventario = {
        "manzanas": 50, 
        "peras": 30, 
        "uvas": 100, 
        "kiwis": 15
    }
    print(f"Claves del inventario: {inventario.keys()}")
    print(f"Valores del inventario: {inventario.values()}")

    for item in inventario:
        print(f"{item}: {inventario.get(item)} unidades")

    print(f"Número de naranjas en el inventario: {inventario.get('naranjas', 0)}")

    inventario.setdefault("fresas", 25)
    print(f"Inventario después de añadir fresas: {inventario}")
    inventario.setdefault("manzanas", 60)
    print(f"Inventario después de intentar añadir manzanas: {inventario}")

def strings_exercises():
    print("Ejercicios de cadenas")
    #STRINGS:
    #Exercise 1.1
    nombre = "Juan"
    apellido = "Pérez"
    nombre_completo = nombre + " " + apellido
    print(f"Nombre completo: {nombre_completo}")
    saludo = "Hola "
    saludo_triple = saludo * 3
    print(f"Saludo repetido: {saludo_triple}")

    #Exercise 1.2
    frase = "Python es divertido y poderoso"
    print(f"Frase original: {frase}")
    primer_caracter = frase[0]
    print(f"Primer carácter de la frase: {primer_caracter}")
    ultimo_caracter = frase[-1]
    print(f"Último carácter de la frase: {ultimo_caracter}")

    print(f"Subcadena de la frase (índices 7 a 15): {frase[7:16]}")
    subcadena_poderoso = frase[frase.index("poderoso"):]
    print(f"Subcadena 'poderoso': {subcadena_poderoso}")
    frase_reversa = frase[::-1] #[start,end,step]
    print(f"Frase al revés: {frase_reversa}")

    #Exercise 2.1
    texto_largo = "El perro de San Roque no tiene rabo porque Ramón Ramírez se lo ha cortado."
    if "perro" in texto_largo:
        print("La frase contiene 'San Roque'")
    else:
        print("La frase no contiene 'San Roque'")
    print(f"Índice de Ramón: {texto_largo.index('Ramón')}")
    texto_con_cola = texto_largo.replace("rabo", "cola")
    print(f"Texto después de reemplazar 'rabo' por 'cola': {texto_con_cola}")
    texto_o_reemplazada = texto_largo.replace("o", "X", 1)
    print(f"Texto después de reemplazar 'o' por 'X': {texto_o_reemplazada}")

    #Exercise 2.2
    elementos = "agua,fuego,tierra,aire"
    elementos_lista = elementos.split(",")
    print(f"Lista de elementos: {elementos_lista}")
    palabras = ["Python", "es", "fantástico"]
    frase_unida = " ".join(palabras)
    print(f"Frase unida: {frase_unida}")
    frase_con_guiones = "-".join(palabras)
    print(f"Frase unida con guiones: {frase_con_guiones}")

    #Exercise 3.1
    cadena_formato = "eStO Es uNa cAdEnA De pRueBA."
    print(f"Cadena original: {cadena_formato}")
    mayusculas = cadena_formato.upper()
    print(f"Cadena en mayúsculas: {mayusculas}")
    minusculas = cadena_formato.lower()
    print(f"Cadena en minúsculas: {minusculas}")
    capitalizada = cadena_formato.capitalize()
    print(f"Cadena capitalizada: {capitalizada}")
    titulo = cadena_formato.title()
    print(f"Cadena en formato título: {titulo}")

    #Exercise 3.2
    email = "usuario@ejemplo.com"
    print(f"Email original: {email}")
    if email.endswith(".com"):
        print("El email termina con '.com'")
    else:
        print("El email no termina con '.com'")
    if email.startswith("usuario"):
        print("El email comienza con 'usuario'")
    else:
        print("El email no comienza con 'usuario'")

    espacios = "   Hola, mundo!   "
    print(f"Texto original con espacios: '{espacios}'")
    espacios_eliminados = espacios.strip()
    print(f"Texto sin espacios al inicio y al final: '{espacios_eliminados}'")

    digitos = "1234567890"
    print(f"Texto original con dígitos: '{digitos}'")
    if digitos.isdigit():
        print("El texto contiene solo dígitos")
    else:
        print("El texto no contiene solo dígitos")