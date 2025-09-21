# TP 1 - Estructuras Secuenciales - UTN

# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
radio = float(input("Ingresá el radio del círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"Área: {area}, Perímetro: {perimetro}")

# Ejercicio 5
segundos = int(input("Ingresá cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas} horas")

# Ejercicio 6
numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
num1 = int(input("Primer número (≠ 0): "))
num2 = int(input("Segundo número (≠ 0): "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# Ejercicio 8
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc}")

# Ejercicio 9
celsius = float(input("Temperatura en °C: "))
fahrenheit = (celsius * 1.8) + 32
print(f"Equivale a {fahrenheit} °F")

# Ejercicio 10
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio}")