""" 
Ejercicio 1: ¿Mayor o menor de edad? 
Enunciado: Pide al usuario su edad. Si es 18 o más, muestra “Eres mayor de edad”. Si no, muestra “Eres menor de edad”. 
"""
print("=============================================\n\tCALCULA SI ERES MAYOR O MENOR\n=============================================")
name = input("Cual es tu nombre? ")
print("-------------------------------¬")
age = int(input("cual es tu edad? "))
print("-------------------------------¬")

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
print("\n==============================================\n\tNUMERO NEGATIVO, POSITIVO O 0\n============================================")
num_Po_Ne = int(input("por favor ingrese un numero: "))
print("-------------------------------------------------------¬")
if num_Po_Ne > 0:
    print(f"El numero ingresado ({num_Po_Ne}) es un numero positivo")
elif num_Po_Ne < 0:
    print(f"El numero ingresado ({num_Po_Ne}) es un numero negativo")
elif num_Po_Ne == 0:
    print(f"El numero ingresado ({num_Po_Ne}) es cero")
    
    
    
    
    
""" 
Ejercicio 3: ¿Par o impar? 
Enunciado: Pide un número entero y dile si es par o impar. (Pista: usa el operador %, que da el residuo de una división). 
"""
print("\n================================================\n\t  NUMERO PAR O IMPAR\n==================================================")
num_Par_Imp = int(input("Ingresa un numero entero mayor a 0 para determinar si es par o impar: "))
print("--------------------------------------------------¬")

if num_Par_Imp == 0:
    print("¡ERROR!\nRecuerda que es un numero mayor a 0 osea de 1 pa'rriba. ")
elif num_Par_Imp % 2 == 0:
    print(f"El numero ingresado ({num_Par_Imp}) es par")
else:
    print(f"El numero ingresado ({num_Par_Imp}) es impar")  
    
    
    

""" 
Ejercicio 4: Nota de un estudiante 
Enunciado: Pide la nota de un estudiante (de 0 a 5) y muestra un mensaje según el rango: 
De 4.5 a 5.0: “Excelente” 
De 3.5 a 4.4: “Bueno” 
De 3.0 a 3.4: “Aprobado” 
Menos de 3.0: “Reprobado” 
"""
print("\n================================================\n\t NOTA DE UN ESTUDIANTE\n================================================")
NombreEstudiante = input("Ingresa el nombre del estudiante: ")
print("--------------------------------------------------¬")
nota = float(input("Ingresa la nota del estudiante (0.0 a 5.0): "))
print("--------------------------------------------------¬")

if nota > 5.0:
    print("¡ERROR!\nLa calificacion va de 0.0 a 5.0")
elif nota >= 4.5 and nota <= 5.0:
    print(f"La nota de {NombreEstudiante}({nota}) es excelente =)")
elif nota >= 3.5 and nota <= 4.4:
    print(f"La nota de {NombreEstudiante}({nota}) es buena =)")
elif nota >= 3.0 and nota <= 3.4:
    print(f"La nota de {NombreEstudiante}({nota}) esta suave, hay que mejorar pero queda aprobado =|")
elif nota < 3.0 and nota > 0.0:
    print(f"{NombreEstudiante} ¡PAILAS! Reprobado la nota ({nota}) es mala, piense porque esta aqui =( mal, mal, mal.. perdio hasta la pecueca mijo, busque que hacer") 

  
  
  
    
""" 
Ejercicio 5: Descuento en una tienda 
Enunciado: Pide el valor de una compra. Si es mayor o igual a 100000, aplica un descuento del 10%. Si es menor, no hay descuento. Muestra el total a pagar.  
"""
print("\n======================================================\n-||-||-||-||-||-||-TIENDA EL PELUDO-||-||-||-||-||-||-\n======================================================")
ValorCompra = int(input("Ingresa el valor de la compra: "))
print("--------------------------------------------------¬")
descuento = int(ValorCompra * 0.1) 

if ValorCompra >= 100000:
    ValorCompra -= descuento
    print("=========================\n\tFactura\n=========================\nPor su compra mayor a \n$100.000 en tiendas el peludo\nle vamos a dar un descuento del 10%")
    print(f"TOTAL A PAGAR: ${ValorCompra}")
elif ValorCompra < 100000:
    print("=========================\n\tFactura\n=========================")
    print("Gracias por su compra")
    print(f"TOTAL A PAGAR: ${ValorCompra}")
    
    
    
""" 
Ejercicio 6: El mayor de dos números 
Enunciado: Pide dos números y muestra cuál es el mayor. Si son iguales, indícalo. 
"""
print("\n================================================\n\t  EL MAYOR DE DOS NUMEROS\n================================================")

num_May_Men = int(input("Ingresa un numero de cualquier valor: "))
print("--------------------------------------------------")
num_May_Men2 = int(input("Ingresa otro numero de cualquier valor: "))
print("--------------------------------------------------")

if num_May_Men > num_May_Men2:
    print(f"{num_May_Men} es mayor que {num_May_Men2}")
elif int(num_May_Men) < int(num_May_Men2):
    print(f"{num_May_Men} es menor que {num_May_Men2}")
elif int(num_May_Men) == int(num_May_Men2):
    print(f"{num_May_Men} es igual que {num_May_Men2}")
    





""" Ejercicio 7: Calculadora sencilla 

Enunciado: Pide dos números y una operación (+, -, *, /). Realiza la operación elegida y muestra el resultado. Si la operación no es válida, avisa al usuario.  """
    
print("\n=================================================================\n\t\t\tCALCULADORA=================================================================")
operacionC1= input("Ingrese una operacion matematica, formato(2 + 4): ").strip().split(" ")
print("-----------------------------------------------------------------¬")
operacionC1[0] = int(operacionC1[0])
operacionC1[2] = int(operacionC1[2])

if len(operacionC1) != 3:
    print("¡Operacion no valida!")
elif operacionC1[1] == "+":
    print(f"Resultado: {operacionC1[0] + operacionC1[2]}")
elif operacionC1[1] == "-":
    print(f"Resultado: {operacionC1[0] - operacionC1[2]}")
elif operacionC1[1] == "*":
    print(f"Resultado: {operacionC1[0] * operacionC1[2]}")
elif operacionC1[1] == "/":
    print(f"Resultado: {operacionC1[0] // operacionC1[2]}")
    
    
    
""" 
Ejercicio 8: Calculadora con división segura (if anidado) 

Enunciado: Mejora el ejercicio anterior: si el usuario elige la división, verifica con un if anidado que el segundo número no sea 0 (no se puede dividir entre cero). 
"""
print("\n=================================================================\n\t\t\tCALCULADORA\n=================================================================")
operacionC2 = input("Ingrese una operacion matematica, formato(2 + 4): ").strip().split(" ")
print("-----------------------------------------------------------------¬")
operacionC2[0] = int(operacionC2[0])
operacionC2[2] = int(operacionC2[2])

if len(operacionC2) != 3:
    print("¡Operacion no valida!")
elif operacionC2[1] == "+":
    print(f"Resultado: {operacionC2[0] + operacionC2[2]}")
elif operacionC2[1] == "-":
    print(f"Resultado: {operacionC2[0] - operacionC2[2]}")
elif operacionC2[1] == "*":
    print(f"Resultado: {operacionC2[0] * operacionC2[2]}")
elif operacionC2[1] == "/":
    if operacionC2[0] == 0 or operacionC2[2] == 0:
        print("-----------ERROR--------------¬\nNo se puede dividir entre cero\n------------------------------¬")
    else:
        print(f"Resultado: {operacionC2[0] // operacionC2[2]}")





""" 
Ejercicio 9: Entrada al cine (if anidado) 

Enunciado: Una película es para mayores de 12 años. Pide la edad del usuario: 

Si tiene 12 años o menos, no puede entrar. 

Si tiene más de 12, pregunta si tiene dinero suficiente (responde “si” o “no”). Si responde “si”, puede entrar; si no, debe esperar a tener dinero. 
"""

print("\n====================================================\n-||-||-||-||-||-||-CINE EL PELUDO-||-||-||-||-||-||-\n====================================================")
edad = int(input("ingresa tu edad: "))
print("--------------------------------¬")
if edad <= 12:
    print(f"Niño aca no estamos presentando Pepa Pig la pelicula es para mayores de 12 años: ")
if edad > 12:
    pregunta = input("tienes dinero suficiente para ingresar (si/no): ")
    print("--------------------------------------------------------------¬")
    if "no" in pregunta:
        print("¡aahhh! y entonces como quiere entrar sin plata, aca no somos beneficiencia volve cuando tengas money")
    elif "si" in pregunta:
        print("disfrute de la pelicula y gracias por preferir ver sus peliculas en este cine")
    
            
        
        

"""Ejercicio 10: Cálculo de tarifa de transporte (variables, operaciones e if anidados) 

Enunciado: Un bus cobra $3000 por pasaje normal. Pide la edad del pasajero y si es estudiante (“si”/”no”): 

Si es mayor de 65 años, viaja gratis. 

Si tiene 65 o menos y es estudiante, paga la mitad del pasaje. 

Si tiene 65 o menos y no es estudiante, paga el pasaje completo. 

Luego pide cuántos pasajes quiere comprar y muestra el total a pagar.  """

print("\n================================================\n\t TARIFA DE TRANSPORTE\n================================================")

pasaje = 3000
edad = int(input("Ingresa tu edad: "))
pregunta = input("¿Eres estudiante? (si/no): ").strip().lower()

if edad > 65:
    print(f"Por ser mayor de 65 viajas gratis")
elif edad <= 65:
    cantidad = int(input("¿cuantos pasajes quieres comprar? "))
    if pregunta == "si":
        pasaje/=2
        print(f"Por ser estudiante tu pasaje sera menor. Total a pagar: {int(pasaje * cantidad)}")
    elif pregunta == "no":
        print(f"El valor del pasaje es {int(pasaje * cantidad)}") 