users = [
    {"usuario":"juan", "passward":12345, "saldo":0},
    {"usuario":"pedro", "passward":12345, "saldo":0},
    {"usuario":"ana", "passward":12345, "saldo":0},
    {"usuario":"jan", "passward":12345, "saldo":0},
    {"usuario":"sol", "passward":12345, "saldo":0},
]

users.append({"usuario":"danilo", "passward":3510, "saldo":0})

users[0].update({"passward":000000})

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
      

