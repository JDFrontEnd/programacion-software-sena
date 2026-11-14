""" users = [
    {"usuario":"juan", "passward":12345, "saldo":0},
    {"usuario":"pedro", "passward":12345, "saldo":0}
]

users.append({"usuario":"danilo", "passward":3510, "saldo":0})

users[0].update({"passward":000000})

print(users[3].get("usuario")) """

#print(users[0], users[5])

print(5 == 5.0)

  
  


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
contador = 4
passward = 1234

while contador > 0:
  if contador == passward:
    print('acces')
    break
  else:
    print('error')
    contador -= 1
 """


""" contador = 10

while contador > 0:
  print(contador)
  contador -= 1
   """
   
""" num = int(input("ingresa un numero positvo y entero: "))

almacenar = 0

contador = True

while contador:
  contador += num
  num = int(input("ingresa un numero positvo y entero: "))
  if num == 0:
    print('numero logrado')
    contador = False
  else:
    print(f'sigue intentando')
    
print(almacenar)
 """
""" 

"""

num_secreto = 20

num = int(input('intenta adivinar el numero allmacenado en num_secreto: '))

contador = True

while contador:
  if num == num_secreto:
    print('encontraste el numero secreto')
    contador = False
  elif num < num_secreto:
    print('numero ingresado es menor al secreto')
    num = int(input('intenta adivinar el numero allmacenado en num_secreto: '))
  elif num > num_secreto:
    print('numero ingresado es mayor al secreto')
    num = int(input('intenta adivinar el numero allmacenado en num_secreto: '))