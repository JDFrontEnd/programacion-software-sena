users = [{"usuario":"juan", "passward":12345, "saldo":0},
         {"usuario":"pedro", "passward":12345, "saldo":0},
         {"usuario":"ana", "passward":12345, "saldo":0},
         {"usuario":"jan", "passward":12345, "saldo":0},
         {"usuario":"sol", "passward":12345, "saldo":0},
    ]

# print(users[0].get("usuario"))


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

# Reto 6. La operación engañosa
numero = input("Ingresa un número: ")
numero = int(numero)
numero = numero + 10
numero = str(numero)
# print("Resultado: " + numero)
# print(type(numero))



# Preguntas:
# 1. ¿Qué tipo tiene numero después del primer input()?
# 2. ¿Qué tipo tiene después de int()?
# 3. ¿Qué tipo tiene después de str()?
# 4. ¿Por qué se convierte nuevamente a texto?


""" 
Reto 9. Contraseña secreta

Pide una contraseña y realiza estas operaciones:
- Convierte toda la contraseña a mayúsculas.
- Muestra los primeros tres caracteres.
- Muestra los últimos dos caracteres.
- Invierte la contraseña.
- Comprueba si la contraseña tiene al menos ocho caracteres utilizando if y else.
Pregunta trampa: ¿Puedes modificar directamente un carácter haciendo contraseña[0] = "A"?
"""

""" 
Nivel 4. Random y condicionales
Razonamiento
Reto 11. Número aleatorio

Utiliza la librería random para generar un número entre 1 y 10.

Pide al usuario que intente adivinarlo.
- Si acierta, muestra un mensaje de felicitación.
- Si falla, muestra cuál era el número.
"""

""" 
Reto 12. El número aleatorio convertido

Genera un número aleatorio entre 1 y 100.

Después:
1. Convierte el número a texto.
2. Muestra su tipo de dato.
3. Obtén el primer y último carácter del número convertido.
4. Convierte nuevamente el número a entero.
5. Comprueba si es mayor o igual a 50.
"""

""" 
Nivel 5. Retos de detección de errores
Aquí no basta con programar: deben explicar por qué el código funciona o falla.

Reto 14. Predice el resultado
x = "10"y = 5x = int(x)y = str(y)print(x + int(y))print(type(x))print(type(y))



¿Qué aparecerá en pantalla?
"""

""" 
Prueba final: el reto integrador
Desafío final
Reto 17. Sistema de identificación aleatoria

El programa debe pedir al usuario:
1. Nombre completo.
2. Edad.
3. Un número entre 1 y 10.
Después debe:
- Convertir el nombre a mayúsculas.
- Separar el nombre completo usando split().
- Mostrar el primer nombre utilizando índices.
- Convertir la edad a entero.
- Generar un número aleatorio entre 1 y 10.
- Comparar el número ingresado con el generado.
- Comprobar si el usuario es mayor de edad utilizando if y else.
- Mostrar los tipos de datos de las variables principales.
Reglas:
- No utilizar ciclos (for o while).
- No utilizar funciones creadas con def.
- No utilizar elif.
- No crear variables innecesarias: deben reutilizar algunas sobrescribiendo sus valores.
- Deben explicar dónde y por qué utilizaron casting.
"""