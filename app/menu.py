from colorama import Fore, Style
import os

from app.menuoptions import menuOptions, runOptionAction, validateOption

def clearConsole():
    os.system('cls' if os.name == "nt" else None)

def showMenu():
    # Declaracion de variables
    option = None
    
    while True:
        # Limpiamos al iniciar la app siempre
        clearConsole()
        
        # Mostramos el menu
        print(f"{Fore.GREEN}{"*" * 64}")
        print('\n')
        print(f"{Style.BRIGHT}Bievenido a tu gestor profesional de tareas\n")
        print("Opciones:\n")
        menuOptions()
        print('\n')
        
        option = inputOption()
        
        res = runOptionAction(option)
        
        print('\n')
        print(f"{Fore.GREEN}{"*" * 64}")
        
        # Si la funcion retorna False, es que es la de salida
        if res == False:
            break
            
        # Si no entro en el break
        # Le damos la opcion de continuar...
        input(f"\n{Style.DIM}Presione enter para continuar....")
        
        
    
def inputOption() -> str:
    # Pedimos la opcion y si no damos error
    option = None
    while True:
        try:
            option = input(f"> Ingrese una opcion: ")
            
            # Validamos que sea una opcion correcta
            validateOption(option)
            break
        except Exception as e:
                print(f"{Fore.RED}[ERROR]: {e}\n")       
    
    return option