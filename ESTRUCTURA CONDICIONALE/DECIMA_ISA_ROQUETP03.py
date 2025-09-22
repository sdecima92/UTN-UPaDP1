#1.Mayordeedad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#2.Aprobado o desaprobado

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3.Número par

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4.Categoria por edad

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5.Contraseña valida

contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6.calculosestadistico

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución no definida por los criterios dados")

#7.Frase que termina en vocal

frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

#8.Transformar nombre

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para MAYÚSCULAS, 2 para minúsculas, 3 para capitalizar: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#9.MAgnitud de terremoto

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#10.Estacion del año según fecha y hemisferio

hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Convierto la fecha a un número para facilitar comparación

if (fecha >= (12, 21) or fecha <= (3, 20)):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (fecha >= (3, 21) and fecha <= (6, 20)):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (fecha >= (6, 21) and fecha <= (9, 20)):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print("Estación:", estacion)











