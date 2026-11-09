""" Ejercicio 1: ¿Mayor o menor de edad? 

Enunciado: Pide al usuario su edad. Si es 18 o más, muestra “Eres mayor de edad”. Si no, muestra “Eres menor de edad”. 
"""
print("=============================================")
print("\tCALCULA SI ERES MAYOR O MENOR")
print("=============================================")
name = input("Cual es tu nombre? ") 
print("-------------------------------")
age = int(input("cual es tu edad? "))
print("===============================")

if age < 18:
    print(f"Hola, {name} eres menor de edad")
elif age >= 18 and age <= 65:
    print(f"hola, {name} eres mayor de edad")
else:
    print(f"Hola, {name} eres adulto mayor") 

""" 
Ejercicio 2: ¿Positivo, negativo o cero? 

Enunciado: Pide un número al usuario y dile si es positivo, negativo o cero. 
"""
print("\n============================================")
print("\tNUMERO NEGATIVO, POSITIVO O 0")
print("============================================")
num = int(input("por favor ingrese un numero: "))
print("---------------------------------------------")
if num > 0:
    print(f"el numero ingresado ({num}) es un nunero positivo")
elif num < 0:
    print(f"el numero ingresado ({num}) es un nunero negativo")
elif num == 0:
    print(f"el numero ingresado ({num}) es cero")
    
""" 
Ejercicio 3: ¿Par o impar? 

Enunciado: Pide un número entero y dile si es par o impar. (Pista: usa el operador %, que da el residuo de una división). 
"""


print("\n================================================")
print("\tNUMERO PAR O IMPAR")
print("==================================================")
num1 = int(input("Ingresa un numero entero mayor a 0 para determinar si es par o inpar: "))
print("--------------------------------------------------")

if num1 == 0:
    print("¡ERROR!\nRecuerda que es un numero mayor a 0 osea de 1 pa'rriba. ")
elif num1 % 2 == 0:
    print(f"el numero ingresado ({num1}) es par")
else:
    print(f"el numero ingresado ({num1}) es impar") 
    

""" 
Ejercicio 4: Nota de un estudiante 
Enunciado: Pide la nota de un estudiante (de 0 a 5) y muestra un mensaje según el rango: 
De 4.5 a 5.0: “Excelente” 
De 3.5 a 4.4: “Bueno” 
De 3.0 a 3.4: “Aprobado” 
Menos de 3.0: “Reprobado” 
"""
print("\n================================================")
print("\tNOTA DE UN ESTUDIANTE")
print("================================================")
NombreEstudiante = input("Ingresa el nombre del estudiante: ")
print("--------------------------------------------------")
nota = float(input("Ingresa la nota del estudiante (0.0 a 5.0): "))
print("==================================================")

if nota > 5.0:
    print("¡ERROR!\nLa calificacion va de 0.0 a 5.0")
elif nota >= 4.5 and nota <= 5.0:
    print(f"La nota estudiante ({nota}) es excelente =)")
elif nota >= 3.5 and nota <= 4.4:
    print(f"La nota del estudiante ({nota}) es buena =)")
elif nota >= 3.0 and nota <= 3.4:
    print(f"La nota del estudiante ({nota}) esta suave, hay que mejorar queda aprobado =|")
elif nota < 3.0 and nota > 0.0:
    print(f"¡PAILAS! La nota del estudiante ({nota}) es mala, piense porque esta aqui =( mal, mal, mal.. perdio hasta la pecueca mijo, busque que hacer") 
    
""" 
Ejercicio 5: Descuento en una tienda 
Enunciado: Pide el valor de una compra. Si es mayor o igual a 100000, aplica un descuento del 10%. Si es menor, no hay descuento. Muestra el total a pagar.  
"""

print("\n================================================")
print("\t\tTIENDA EL PELUDO")
print("================================================")
ValorCompra = int(input("Ingresa el valor de la compra: "))
print("--------------------------------------------------")

descuento = ValorCompra * 0.1 

if ValorCompra >= 100000:
    ValorCompra -= descuento
    print("=========================\n\tFactura")
    print("=========================")
    print("Por su compra mayor a $100.000 en tiendas el peludo le vamos a dar un descuento del 10%")
    print(f"TOTAL A PAGAR: {ValorCompra}")
elif ValorCompra < 100000:
    print("=============\n\tFactura")
    print("Gracias por su compra")
    print(f"TOTAL A PAGAR: {ValorCompra}")
    
""" 
Ejercicio 6: El mayor de dos números 
Enunciado: Pide dos números y muestra cuál es el mayor. Si son iguales, indícalo. 
"""
print("\n================================================")
print("\tEL MAYOR DE DOS NUMEROS")
print("================================================")
Valor1 = int(input("Ingresa un numero de cualquier valor: "))
Valor2 = int(input("Ingresa otro numero de cualquier valor: "))
print("--------------------------------------------------")
if Valor1 > Valor2:
    print(f"{Valor1} es mayor que {Valor2}")
elif int(Valor1) < int(Valor2):
    print(f"{Valor1} es menor que {Valor2}")
elif int(Valor1) == int(Valor2):
    print(f"{Valor1} es igual que {Valor2}")
    

""" Ejercicio 7: Calculadora sencilla 

Enunciado: Pide dos números y una operación (+, -, *, /). Realiza la operación elegida y muestra el resultado. Si la operación no es válida, avisa al usuario.  """
    
print("\n================================================")
print("\t\tCALCULADORA")
print("================================================")
number1 = int(input("ingrese el primer valor de la operacion: "))
operador = input("ingrese el operador matematico (suma: +, resta: -, multiplicacion: *, division: /): ")
number2 = int(input("ingrese el segundo valor de la operacion: "))
#corre
if operador == "+":
    print(f"Resultado: {number1 + number2}")
elif "-" in operador:
    print(f"Resultado: {number1 - number2}")
elif "*" in operador:
    print(f"Resultado: {number1 * number2}")
elif "/" in operador:
    print(f"Resultado: {number1 / number2}")
    
""" 
Ejercicio 8: Calculadora con división segura (if anidado) 

Enunciado: Mejora el ejercicio anterior: si el usuario elige la división, verifica con un if anidado que el segundo número no sea 0 (no se puede dividir entre cero). 
"""
print("\n================================================")
print("\tCALCULADORA DE DIVISION")
print("================================================")
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
    if number1 == 0 or number2 == 0:
        print("¡ERROR!\nno se puede dividir entre cero")
    else:
        print(f"Resultado: {number1 / number2}")
        
""" 
Ejercicio 9: Entrada al cine (if anidado) 

Enunciado: Una película es para mayores de 12 años. Pide la edad del usuario: 

Si tiene 12 años o menos, no puede entrar. 

Si tiene más de 12, pregunta si tiene dinero suficiente (responde “si” o “no”). Si responde “si”, puede entrar; si no, debe esperar a tener dinero. 
"""

print("\n================================================")
print("\tCINE EL ANGELLO")
print("================================================")
edad = int(input("ingresa tu edad: "))

if edad <= 12:
    print(f"Lo siento no puedes ingresar la pelicula tiene restrincion de edad")
if edad > 12:
    pregunta = input("tienes dinero suficiente para ingresar (si/no): ")
    if "no" in pregunta:
        print("no puedes ingresar sin money F en el chat. volve la procima que con mucho gusto")
    elif "si" in pregunta:
        print("disfrute de la pelicula y gracias por preferir ver sus peliculas en este cine")
        

"""Ejercicio 10: Cálculo de tarifa de transporte (variables, operaciones e if anidados) 

Enunciado: Un bus cobra $3000 por pasaje normal. Pide la edad del pasajero y si es estudiante (“si”/”no”): 

Si es mayor de 65 años, viaja gratis. 

Si tiene 65 o menos y es estudiante, paga la mitad del pasaje. 

Si tiene 65 o menos y no es estudiante, paga el pasaje completo. 

Luego pide cuántos pasajes quiere comprar y muestra el total a pagar.  """
print("\n================================================")
print("\tTARIFA DE TRANSPORTE")
print("================================================")
pasaje = 3000
edad = int(input("Ingresa tu edad: "))

if edad > 65:
    print(f"Por ser mayor de 65 viajas gratis")
elif edad <= 65:
    pregunta = input("Eres estudiante (si/no): ")
    pregunta.lower()
    pregunta.strip()
    if "si" in pregunta:
        pasaje/=2
        print(f"Por ser estudiante tu pasaje sera de {pasaje}")
    elif "no" in pregunta:
        print(f"El valor del pasaje es {pasaje}")