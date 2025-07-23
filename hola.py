#Hi!
print("Hola, mundo")

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
