""" users = [
    {"usuario":"juan", "passward":12345, "saldo":0},
    {"usuario":"pedro", "passward":12345, "saldo":0}
]

users.append({"usuario":"danilo", "passward":3510, "saldo":0})

users[0].update({"passward":000000})

print(users[3].get("usuario")) """

#print(users[0], users[5])


""" Elementos del diccionario
Los elementos del diccionario están ordenados, son modificables y no permiten duplicados.

Los elementos del diccionario se presentan en pares clave:valor y pueden referirse a ellos por usando el nombre clave.

Ejemplo
Imprime el valor de "marca" del diccionario: """

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict["brand"])

""" 
También existe un método llamado que te dará el mismo resultado:get()

Ejemplo
Obtén el valor de la clave "model":

x = thisdict.get("model")
"""

""" 
num = ["6", "7", "8"]
num1 = ["1", "2", "3", "4", "5"]


for a in num,num1:
    for b in a:
      print(b)

frutas = ["uva", "mora", "pera"]
frutas1 = ["lulo", "anis", "poma", frutas]

for a in frutas1[:3],frutas1[3]:
    for b in a:
      print(b) """
      
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