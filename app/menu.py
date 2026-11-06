from colorama import Fore, Style
import os

from app.modelos import Tarea
from app.menuoptions import menuOptions, runOptionAction, validateOption

def showTitle() -> None:
    """
    Funcion que imprime el titulo del proyecto
    Retorna:
        None
    """
    print("\033[0;37m█▀▀▀▀▀▀▀█  ▄▀▀▀▀▄  █▀▀▀▀▀▄   ▄▀▀▀▀▀█  ▄▀▀▀▀▄  ▄▀▀▀▀▀█       ▄▀▀▀▀▀█ █▀█      █▀▀▀▀▀█\033[0m")
    print("\033[0;37m▀▀▀█ █▀▀▀ ▓ ▄▀▀▄ ▓ ▓ █▀▀▄ █ ▓ ▄▀▀█▄█ ▓ ▄▀▀▄ ▓ ▓ █▀▀▀▀      ▓ ▄▀▀█ █ █ ▓      ▀▀█ █▀▀\033[0m")
    print("\033[0;37m   \033[0;92m▓\033[0;37m \033[0;92m█\033[0;37m    \033[0;92m▒\033[0;37m \033[0;92m█\033[0;37m  \033[0;92m█\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m█▄▄▀\033[0;37m \033[0;92m█\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m█▄▄\033[0;37m    \033[0;92m▒\033[0;37m \033[0;92m█\033[0;37m  \033[0;92m█\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m▀▄\033[0;37m         \033[0;92m▒\033[0;37m \033[0;92m█\033[0;37m  \033[0;92m█\033[0;37m \033[0;92m█\033[0;37m \033[0;92m▓\033[0;37m \033[0;92m▒\033[0;37m        \033[0;92m▓\033[0;37m \033[0;92m▒\033[0;37m  \033[0m")
    print("\033[0;37m   \033[0;92m▒\033[0;37m \033[0;92m█\033[0;37m    \033[0;92m░\033[0;37m \033[0;92m█▀▀▀\033[0;37m \033[0;92m░\033[0;37m \033[0;92m░\033[0;37m \033[0;92m▄▄▄\033[0;37m \033[0;92m▀▄\033[0;37m \033[0;92m░\033[0;37m \033[0;92m▄▄█\033[0;37m    \033[0;92m░\033[0;37m \033[0;92m█▀▀▀\033[0;37m \033[0;92m░\033[0;37m  \033[0;92m▀▄\033[0;37m \033[0;92m▀▄\033[0;37m       \033[0;92m░\033[0;37m \033[0;92m█\033[0;37m  \033[0;92m▀▀▀\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m░\033[0;37m        \033[0;92m▒\033[0;37m \033[0;92m░\033[0;37m  \033[0m")
    print("\033[0;37m   \033[0;92m░\033[0;37m \033[0;92m█\033[0;37m    \033[0;92m▒\033[0;37m \033[0;92m█▀▀█\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m█\033[0;37m  \033[0;92m█\033[0;37m \033[0;92m▓\033[0;37m \033[0;92m▒\033[0;37m \033[0;92m█\033[0;37m \033[0;32m──\033[0;37m   \033[0;92m▒\033[0;37m \033[0;92m█▀▀█\033[0;37m \033[0;92m▒\033[0;37m    \033[0;92m▀▄\033[0;37m \033[0;92m▓\033[0;37m      \033[0;92m▒\033[0;37m \033[0;92m█\033[0;37m \033[0;32m─\033[0;92m█▀█\033[0;37m \033[0;92m░\033[0;37m \033[0;92m▒\033[0;37m  \033[0;92m▄▄▄\033[0;37m   \033[0;92m░\033[0;37m \033[0;92m▒\033[0;37m  \033[0m")
    print("\033[0;37m   \033[0;32m▒\033[0;37m \033[0;32m█\033[0;37m    \033[0;32m▓\033[0;37m \033[0;32m█\033[0;37m  \033[0;32m█\033[0;37m \033[0;32m▓\033[0;37m \033[0;32m▓\033[0;37m \033[0;32m█\033[0;37m  \033[0;32m█\033[0;37m \033[0;32m▒\033[0;37m \033[0;32m▓\033[0;37m \033[0;32m█\033[0;37m \033[0;32m─█▀█\033[0;37m \033[0;32m▓\033[0;37m \033[0;32m█\033[0;37m  \033[0;32m█\033[0;37m \033[0;32m▓\033[0;37m     \033[0;32m█\033[0;37m \033[0;32m▒\033[0;37m      \033[0;32m▓\033[0;37m \033[0;32m█\033[0;37m \033[0;32m─█\033[0;37m \033[0;32m█\033[0;37m \033[0;32m▒\033[0;37m \033[0;32m▓\033[0;37m  \033[0;32m█\033[0;37m \033[0;32m▓\033[0;37m   \033[0;32m▒\033[0;37m \033[0;32m▓\033[0;37m  \033[0m")
    print("\033[0;37m   \033[0;32m▓\033[0;37m \033[0;32m█\033[0;37m    \033[0;32m█\033[0;37m \033[0;32m█\033[0;37m  \033[0;32m█\033[0;37m \033[0;32m█\033[0;37m \033[0;32m█\033[0;37m \033[0;32m█\033[0;37m  \033[0;32m█\033[0;37m \033[0;32m▓\033[0;37m \033[0;32m▀▄\033[0;37m \033[0;32m▀▀▀\033[0;37m \033[0;32m█\033[0;37m \033[0;32m█\033[0;37m \033[0;32m█\033[0;37m  \033[0;32m█\033[0;37m \033[0;32m█\033[0;37m \033[0;32m█▀▀▀▀\033[0;37m \033[0;32m▓\033[0;37m      \033[0;32m▀▄\033[0;37m \033[0;32m▀▀▀\033[0;37m \033[0;32m█\033[0;37m \033[0;32m▓\033[0;37m \033[0;32m▀▀▀▀\033[0;37m \033[0;32m▒\033[0;37m \033[0;32m█▀▀\033[0;37m \033[0;32m▀▀█\033[0m")
    print("\033[0;37m   \033[0;32m▀▀▀\033[0;37m    \033[0;32m▀▀▀\033[0;37m  \033[0;32m▀▀▀\033[0;37m \033[0;32m▀▀▀\033[0;37m  \033[0;32m▀▀▀\033[0;37m   \033[0;32m▀▀▀▀▀▀\033[0;37m \033[0;32m▀▀▀\033[0;37m  \033[0;32m▀▀▀\033[0;37m \033[0;32m▀▀▀▀▀▀\033[0;37m         \033[0;32m▀▀▀▀▀▀\033[0;37m \033[0;32m▀▀▀▀▀▀▀▀\033[0;37m \033[0;32m▀▀▀▀▀▀▀\033[0m")

def clearConsole() -> None:
    """
    Funcion para limpiar la consola donde se ejecute
    Retorna:
        None
    """
    os.system('cls' if os.name == "nt" else None)


def showMenu() -> None:
    """
    Funcion para agrupar y ejecutar las funciones necesarias para mostrarle
    al usuario el menu de la app
    Retorna:
        None
    """
    # Declaracion de variables
    option = None
    tareas = []
    
    while True:
        # Limpiamos al iniciar la app siempre
        clearConsole()
        
        # Mostramos el menu
        print(f"{Fore.GREEN}{"*" * 64}")
        print('\n')
        showTitle()
        print(f"{Style.BRIGHT}Bievenido a tu gestor profesional de tareas\n")
        print("Opciones:\n")
        menuOptions()
        print('\n')
        
        option = inputOption()
        
        res = runOptionAction(option, tareas)
        
        print(f"{Fore.GREEN}{"*" * 64}")
        
        # Si la funcion retorna False, es que es la de salida
        if res == False:
            break
        elif type(res) == Tarea:
            # Si es una instancia de tarea, lo colocamos en el arreglo
            tareas.append(res)
            
        # Si no entro en el break
        # Le damos la opcion de continuar...
        input(f"\n{Style.DIM}Presione enter para continuar....")
        
def inputOption() -> str:
    """
    Funcion para capturar la opcion ingresada por el usuario,
    aca se valida que sea un valor valido
    Retorna:
        str: la opcion valida ingresada por el usuario
    """
    # Pedimos la opcion y si no damos error
    option = ""
    while True:
        try:
            option = input(f"> Ingrese una opcion: ")
            
            # Validamos que sea una opcion correcta
            validateOption(option)
            break
        except Exception as e:
                print(f"{Fore.RED}[ERROR]: {e}\n")       
    
    return option

if __name__ == "__main__":
    """
    Prueba de docstrings
    """
    
    help(inputOption)
    print("*" * 64)
    help(showMenu)
    print("*" * 64)
    help(clearConsole)
    print("*" * 64)
    help(showTitle)