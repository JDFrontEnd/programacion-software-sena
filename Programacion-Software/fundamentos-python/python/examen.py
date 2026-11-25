#Dada una lista de números, calcula el promedio y luego muestra cuántos elementos son mayores que él y cuáles son.
numeros = [3,4,6,7,3,9,3,9]

suma = 0

contador = 0

while contador < len(numeros): 
    suma += numeros[contador]
    contador += 1
promedio = suma / len(numeros)
contador = 0
while contador < len(numeros):
    if promedio < numeros[contador]:
        print(f"{promedio} es menor que {numeros[contador]}")
    else:
        print(f"{promedio} es mayor que {numeros[contador]}")
    contador += 1


#Pide números al usuario hasta que escriba -1. Guarda los números en una lista y al final muestra la suma y el promedio. Si no ingresó ninguno, avisa. No uses sum()

""" num_save = []

contador = 0

suma = 0

while True: 
    num_input = int(input("Ingresa cualquier numero incluyendo numeros negativos y positivos: "))
    if num_input == -1:
        break
    elif num_input == 0:
        print("No se ingreso ningun numero: ") 
    num_save.append(num_input)
    suma += num_save[contador]
    contador += 1
    
promedio = suma / len(num_save)
print(f"suma: {suma}, promedio: {promedio}") """


#Pide nombres al usuario y guárdalos en una lista hasta que escriba "fin". Al terminar, muestra todos los nombres numerados empezando en 1.

""" users = []
print("Ingresa los nombre que quieras cuando quieras ver los nombre ingresados copia 'fin'")
name_user = input("Ingresa el name: ").strip()

contador = 1

while name_user != "fin":  
    users.append(f"{contador}. {name_user}")
    contador += 1
    name_user = input("Ingresa el name: ").strip()
    
for i in users:
    print(i) """

#Dada una lista de números y un valor que el usuario escribe, cuenta cuántas veces aparece ese valor en la lista. No uses el método count()

""" 
num_input = int(input("Ingresa un numero: "))
numeros = [2,4,4,5,7,6,7,2,5,4,0,4,7,10,20,33]
save_num = []

contador = 0
while contador < len(numeros):
    if num_input == numeros[contador]:
        save_num.append(num_input)
    contador += 1
print(f"El numero ingresado esta en mi lista {len(save_num)} veces") """
