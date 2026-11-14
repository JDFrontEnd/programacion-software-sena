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
      
   
passward = int(input('pasward: '))
contador = 0
passward = 1234

while contador > 4:
  if contador == passward:
    print('Acceso concedido')
    break
  else:
    print('error')
    contador -= 1



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
      
  

