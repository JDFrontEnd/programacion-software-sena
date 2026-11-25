import random

name = "juan" #str text
# print(type(name))

age = 24 #int number
# print(type(age))

student = True #bool boleano
# print(type(student))

learning = "python"

#operadores matematicos
a = 4 + 7 
b = 4 * 1
c = 4 / 5

#Many Values to Multiple Variables
x, y, z = "orange", "banana", "cherry"

#One Value to Multiple Variables
x = y = z = "orange"

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

x = 1 # int
y = 2.8 # float
z = 1j # complex

# Presentación personal
name = "juan diego"
age = 25
city = "medellin"

print(f"Hola, soy {name}Tengo {age} años y vivo en {city}.")



# Factura de una compra
utiles = {
    "cuaderno": 4500,
    "lapiz": 1800
}

print("<==============================>\n")
print(utiles)
print("\n<==============================>\n")

cantidadLapiz = int(input("cuantos lapices quieres comprar: "))
cantidadCuaderno = int(input("cuantos cuadernos quieres comprar: "))

totalCuaderno = cantidadCuaderno * utiles["cuaderno"]
totalLapiz = cantidadLapiz * utiles["lapiz"]

print("\n======================================")
print("\tFactura de compra")
print("======================================\n")
print("---------------------------------------")
print(f"Cuadernos: {cantidadCuaderno}\nSubtotal cuadernos: ${totalCuaderno}")
print("---------------------------------------")
print(f"Lapiz: {cantidadLapiz}\nSubtotal lapiz: ${totalLapiz}")
print("---------------------------------------")
print(f"TOTAL: ${totalLapiz + totalCuaderno}")




# Salario semanal

salario = 65000
dia = salario
semana  = salario * 6
mes = semana * 5 - 120000 * 5
print(f"salario semanal: ${semana}\nDinero ganado en 4 semanas: ${semana*4}\nTotal de dinero si gastara $120.000 cada semana: {mes}")

# Analizador de nombres
name = "juan diego mesa"
print(name.upper())
print(name.lower())
print(name.split(" ")[0])
print(name.split(" ")[1])


# Mensaje secreto
mensaje = "Aprender Python es divertido"
print(mensaje[0:8])
print(mensaje[9:14])
print(mensaje[-9:])
new = mensaje.split(" ")
print(new)
print(new[3], new[2], new[1], new[0])


NumImpar = random.randrange(1, 20, 3)
NumPar = random.randrange(2, 20, 2)

L1 = NumImpar
L2 = NumPar
L3 = L1
L4 = L2

Ar = L1 * L2
Per = (L1 + L2)*2

print(f"Lado par es de: {L2}, lado impar es de: {L1},  el area es: {Ar},  el perimetro es: {Per}")

#rectangulo
pR = (L1 + L2)*2
aR = L1 * L2
vR = L1 * L2 * aR
print(f"rectangulo: -area: {aR} -perimetro: {pR} -volumen: {vR}")

a = random.randrange(1, 20)

L1 = L2 = L3 = L4 = a

# cuandrado
pC = L1 * 4 
aC = L1 * 2
vC = L1 * L2 * L3
print(f"cuadrado: -area: {aC} -perimetro: {pC} -volumen: {vC}")

#triangulo
pT = L1 + L2 + L3
aT = (L1 * L2) / 2
vT = L1 * L2 * L3
print(f"triangulo: -area: {aT} -perimetro: {pT} -volumen: {vT}")

    
"""calculo de edad""" 
    
name = input("Cual es tu nombre? ") 
age = int(input("cual es tu edad? "))

if age < 18:
    print(f"Hola, {name} eres menor de edad")
elif age >= 18 and age <= 65:
    print(f"hola, {name} eres mayor de edad")
else:
    print(f"Hola, {name} eres adulto mayor")   
    
    
    
""" calculadora """

print("calculadora")
number1 = int(input("ingrese el primer valor de la operacion: "))
operador = input("ingrese el operador matematico (suma: +, resta: -, multiplicacion: *, division: /): ")
number2 = int(input("ingrese el segundo valor de la operacion: "))


if "+" in operador:
    print(f"Resultado: {number1 + number2}")
elif "-" in operador:
    print(f"Resultado: {number1 - number2}")
elif "*" in operador:
    print(f"Resultado: {number1 * number2}")
elif "/" in operador:
    print(f"Resultado: {number1 / number2}")



a = "Hell0, World!"
b = a.split(",")
c = a[-6:-1], a[:6]
print(b[1] + b[0])
print(c)


hoy = 23
octuber = "octubre"
print(f"hoy es {hoy} de {octuber}")



id = 118735173
nombre = "santo tomas"
apellido = "santo"
edad = 24
print(f"hola, {nombre + " " + apellido} tu cedula es {id} y tienes {edad} años")




TRM = 3240
dolares = 120
print(f"para la TRM de hoy es: ${TRM} total es de ${TRM * dolares}")

saldo = 10000

tranferencia = int(input("ingrese el monto a tranferir:"))
saldo = tranferencia - saldo
print(f"saldo total: ${saldo * TRM}")

retiro = int(input("ingrese el monto a tranferir:"))
saldo = retiro - saldo
print(f"saldo total: ${saldo * TRM}") 

consignacion = int(input("ingrese el monto a tranferir:"))
saldo = consignacion + saldo
print(f"saldo total: ${saldo * TRM}")  


""" datos personales """
print("<==================================>")
print("\n \t Registro de datos \n")
print("<==================================>")
print("\n-----------------------------------")
nameUser = input("Nombre Completo: ")
numberIdentification = int(input("Numero de identificacion: "))
fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AA): ")
gender = input("Genero (Masculino, femenino, otro.): ")
Chilldren = input("Tienes Hijos: ")
numberChilldren = int(input("Si tienes hijos, cuantos hijos tienes? "))
print("------------------------------------\n")

print("<===== Datos Personales =====>")
print(f"Nombre de usuario: {nameUser}\nNuemeeo de identificacion: {numberIdentification}\nFecha de nacimiento: {fechaNacimiento}\n")

respueste = input("señor usuario ingrese la traduccion literal de la palabra ")

"""    
passward = int(input('pasward: '))
contador = 0
passward = 1234

while contador < 4:
  if contador == passward:
    print('Acceso concedido')
    break
  else:
    print('error')
    contador += 1



contador = 10

while contador > 0:
  print(contador)
  contador -= 1
   
num = int(input("Adivina el numero positvo y entero para terminar el bucle: "))

almacenar = num

contador = 1

while contador > 0:
  num = int(input("ingresa un numero positvo y entero: "))
  if num == 0:
    print('numero logrado')
    contador = 0
  else:
    print(f'sigue intentando')
    contador += 1
    almacenar += num
    
print(almacenar)



num_secreto = 20

num = int(input('intenta adivinar el numero almacenado en num_secreto: '))

contador = 1

while contador > 0:
  if num == num_secreto:
    print('encontraste el numero secreto')
    contador = 0
  elif num < num_secreto:
    print('numero ingresado es menor al secreto')
    num = int(input('intenta adivinar el numero allmacenado en num_secreto: '))
  elif num > num_secreto:
    print('numero ingresado es mayor al secreto')
    num = int(input('intenta adivinar el numero allmacenado en num_secreto: '))
    
    
    

user = {
    "usuario": "chipichipi",
    "passward": 123456789,
}

contador = 1

while contador > 0:
    usuario_input = input('Ingrese su nombre de usuario: ').strip().lower()
    if usuario_input != user['usuario']:
      print('Nombre de usuario incorrecto o no esta registrado')
      contador += 1
    else: 
      contador1 = 0
      while contador1 < 3:
        passward = int(input('Ingresa tu contraseña: '))
        if passward != user['passward']:
          print('Contraseña incorreta')
          contador1 += 1
          if contador1 == 3:
            print('Usuario bloqueado')
            break
        else:
          print('acceso concedido')
          break 
       """
  
"""   
my_int_1 = 56
my_int_2 = -4
print(type(my_int_2))

my_float_1 = -12.0
my_float_2 = 4.9

floor_div_ints = my_int_1 // my_int_2

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>
print('Integer Floor Division:', floor_div_ints) """


""" users = [
  {"user": "juan", "passward": 123},
  {"user": "ana", "passward": 456}
]

print(users[0].get("passward"))
print(users[1].get("passward"))
 """
      
  
# while True:
  
""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, True]

contador = 0 """

""" while contador < len(numeros):
  print(f"{numeros[contador]} Esta en el indice: {contador}")
  contador += 1 """

""" while True:
  if numeros[contador] is True:
    break
  else: 
    print(f"{numeros[contador]} Esta en el indice: {contador}")
  contador += 1
 """



# Calcula la suma y el promedio de una lista de notas con while, sin usar sum(
""" notas = [3.5, 4.0, 2.8, 5.0, 4.2]
contador = 0
suma = 0

while contador < len(notas):
  suma += notas[contador]
  contador += 1
print(f"nota: {suma} promedio: {suma / len(notas)}") """

1
2

#Dada una lista de numeros, crea una nueva lista que contenga solo los numeros pares y otra con los impares.


""" numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pares = []
impares = []
contador = 0

while contador < len(numeros):
    if numeros[contador] % 2 == 0:
      pares.append(numeros[contador])
    else:
      impares.append(numeros[contador])
    contador += 1
  
print(pares)
print(impares) """

# Pide numeros al usuario y guárdalos en una lista hasta que escriba 0. Luego muestra cuántos ingreso, el
# mayor y el menor (sin usar max() ni min()).

""" a = []

while True:
  numeros = int(input("Ingrese el primer número: "))
  if numeros != 0:
    a.append(numeros)
  else:
    break
print(a) """


""" num = int(input("Ingresa un numero: "))

contador = num

while contador > 0:
  print(contador)
  contador -= 1
print("¡Despegue!") """




numbers = []
numPositivos = []
numNegativos = []

num = int(input("Ingrese numeros positivos o negativos el programa termina cuando ingrese -1: "))

while num != -1:
  numbers.append(num)
  if num < 0:
    numNegativos.append(num)
  else:
    numPositivos.append(num)
  num = int(input("Ingrese numeros positivos o negativos: "))

print(f"Cantidad de numeros ingresados: {numbers} \nNuemeros positivos ingresados: {numPositivos} \nNumeros negativos ingresados: {numNegativos}")
