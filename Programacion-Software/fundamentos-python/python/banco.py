user = {
    "usuario": "juan diego mesa",
    "passward": 123456789,
    "saldo": 0
}

users = [
    {"usuario":"juan", "passward":12345, "saldo":0},
    {"usuario":"pedro", "passward":12345, "saldo":0}
]


# funcion login usuario
def loginUser():
    global usuario_input
    print("\n-------------------------------------")
    usuario_input = input("ingrese su nombre de usuario: ").strip()
    print("-------------------------------------")   
    for confirmacion in users["usuario"]:
        if confirmacion != usuario_input:
            print('"ALVERTENCIA"\n El nombre de usuario es incorrecto o no esta registrado, por favor ingrese el usuario correctamente')
            return loginUser()
        elif confirmacion == usuario_input:
            confirmacion = usuario_input
            loginPassward()
                
    if usuario_input != users[0].get("usuario"):
        print('"ALVERTENCIA"\n El nombre de usuario es incorrecto o no esta registrado, por favor ingrese el usuario correctamente')
        return loginUser()
    elif usuario_input == users[0].get("usuario"):
        loginPassward()


# funcion login pasward
def loginPassward():
    global passward
    contador = 0
    print("-------------------------------------")
    passward = int(input("ingrese su contraseña: "))
    print("-------------------------------------")
    while contador > 3:
        if passward == user["passward"]:
            action()
            break
        else:
            print("contraseña incorrecta\n-------------------------------------")
            passward = int(input("ingrese su contraseña: "))
            print("-------------------------------------")
            contador += 1
            
            


#funcion para retirear dinero
def Actionleave():
    global actionL
    print("\n-------------------------------------")
    actionL = int(input("cuanto deseas retirar: "))
    print("-------------------------------------") 
    if user["saldo"] - actionL < 0:
        print("Error: saldo insufisiente")
        return Actionleave()
    else: 
        user["saldo"] -= actionL
        print(f"dinero retirado: ${actionL}")
        print(f"su saldo restante: ${user['saldo']}")
    GoBack()
    
#funcion para retirear dinero
def ActionTransfer():
    global actionT
    print("\n-------------------------------------")
    actionT = int(input("cuanto deseas transferir: "))  
    print("-------------------------------------")
    if user["saldo"] - actionT < 0:
            print("Error: saldo insufisiente")
            return ActionTransfer()
    else: 
        user["saldo"] -= actionT
    print(f"dinero transferido: ${actionT}")
    print(f"su saldo restante: ${user['saldo']}")
    GoBack()
    
    
# funcion para consignar dinero
def ActionDeposit():
    global actionD
    print("\n-------------------------------------")
    actionD = int(input("cuanto deseas consignar: "))  
    print("-------------------------------------")
    user["saldo"] += actionD
    print(f"dinero consignado: ${actionD}")
    print(f"su saldo restante: ${user['saldo']}")
    GoBack()
    
    
# funcion navegar al inicio o salir a la interfaz
def GoBack():
    global regresar
    print("\n-------------------------------------")
    regresar = input("Escribe 'salir' para salir de tu cuenta o 'inicio' para ir al menu de inicio: ")
    regresar = regresar.strip()
    print("-------------------------------------")
    if regresar != "salir" and regresar != "inicio":
        print("Error: ingrese la accion correctamente")
        return GoBack()
    elif regresar == "inicio":
        return action()
    elif regresar == "salir":
        return interfaz()
    
#action user
def action():
    global actionUser
    
    print("\n-------------------------------------")
    print(f"Saldo actual: {user['saldo']}")
    print("-------------")
    actionUser = input("que quieres hacer: (retirar, transferir, consignar, salir) ")
    actionUser = actionUser.strip()
    if actionUser != "retirar" and actionUser != "transferir" and actionUser != "consignar" and actionUser != "salir":
        print("¡Error!, copie correctamente el comando")
        return action()
    elif actionUser == "retirar":
        Actionleave()     
    elif actionUser == "transferir":
        ActionTransfer()   
    elif actionUser == "consignar":
        ActionDeposit()
    elif actionUser == "salir":
        interfaz()
        
def registro():
  global getusuario
  global getpassward
  print("==================\n|Registro de cuenta|\n==================\n")
  print("-----------------------------------")
  getusuario = ("Nombre de Usuario: ").strip()
  print("-----------------------------------")
  getpassward = int("Ingresa una Contraseña: ")
  print("solo valores numericos")
  print("-----------------------------------")
  users.append({"usuario": getusuario, "passward": getpassward, "saldo":0})
  interfaz()
    

def interfaz():
    global accoutConfirmation
    print("\n<===============================================================================>\n\t\t\t HOLA BIENVENIDO A BANK.PY\n<===============================================================================>")
    print("\n\t\t\t¿tienes una cuenta abierta?")
    print("\t\t  ----------------------------------------")
    accoutConfirmation = input("\t\t  Ingresar \\ Registrar -> ").strip().lower()
    if accoutConfirmation != "ingresar" and accoutConfirmation != "registrar":
        print("¡Error!, copie correctamente el comando")
        return interfaz()
    elif accoutConfirmation == "ingresar":
        loginUser()
    elif accoutConfirmation == "registrar":
        registro()
        

interfaz()