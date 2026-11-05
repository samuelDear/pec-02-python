from typing import Any, Dict
from colorama import Fore, Style
from app.modelos import Tarea

tareas = []

# Funciones
def añadir_tarea() -> Tarea:
    """
    Agregar una tarea registrando datos requeridos y opcionales
    """
    tarea = ''
    extradata = {}
    try:
        separatorPrint()
        print(f"{Fore.BLUE}- NUEVA TAREA\n")
        
        tarea = notAllowEmptyVal(
            label = "> Titutlo de la tarea (Requerido): ",
            field = "titulo"
        )
        
        # Ahora pedimos los datos opcionales
        while True:
            print(f"\n{Style.BRIGHT}Agregar datos adicionales (Pulsa Enter en blanco cuando termines):\n")
            val = ""
            key = input("> Nombre del dato (Ej: nota, prioridad, fecha): ").strip()
            if not key:
                # Si es vacio le dio enter sin ingresar nada asi que salimos
                break
            
            val = notAllowEmptyVal(
                label = f"> Valor del dato '{key}': ",
                field = "valor"
            )
            
            # Formateamos el campo, por si puso algo raro el usuario
            keyFormatted = key.lower().replace(" ", "_")
            extradata[keyFormatted] = val
        
        print(f"{Fore.BLUE}- AÑADIR TAREA FINALIZADO\n")
        tareaInstance = Tarea(tarea, **extradata)
        
        tareas.append(tareaInstance)
        return tareaInstance
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {e}\n")
    
def notAllowEmptyVal(label: str, field: str = "campo"):
     while True:
        value = input(label).strip()
                
        # Si esta vacio, volvemos a pedirselo
        if not value:
            print(f"{Fore.RED}[ERROR]: El {field} no puede ser vacio.")
            continue
                    
        # Si llego aqui es que tiene data
        return value
    
def listar_tareas() -> Dict[str, Any]:
    """
    Funcion para listar todas las tareas registradas
    """
    
    separatorPrint()
    print(f"{Fore.BLUE}- LISTAR TAREAS")
    print("\nListado de tareas:")
    
    if len(tareas) == 0: 
        print(f"\n{Fore.YELLOW}No hay tareas registradas")
        return True
        
    index = 0
    for tarea in tareas:
        print(f"- ID: {index}")
        print(f"{tarea}")
        index += 1
        
def separatorPrint() -> None:
    """
    Funcion para imprimir una separacion entre cada funcionalidad
    """
    print(f"\n{Fore.GREEN}{"*" * 64}\n")
    
def buscar_tarea(texto: str) -> Dict[str, Any]:
    """
    Funcion para buscar alguna tarea en concreto
    """
    
def eliminar_tarea() -> bool:
    """
    Funcion para eliminar una tarea por su Index
    """
    
    separatorPrint()
    print(f"{Fore.BLUE}- ELIMINAR TAREA\n")
    
    # Validamos si hay tareas, si no mostramos un mensaje
    if len(tareas) == 0: 
        print(f"{Fore.YELLOW}No hay tareas registradas\n")
        return True
    
    listar_tareas()
    
    index = ''
    
    print(f"\n{Style.BRIGHT}Ingrese el ID de la tarea que quiere eliminar (Pulsa Enter en blanco cuando termines):\n")
    
    while True:
        try:
            # Pedimos el indice que quiere eliminar
            index = int(input("> ID de la tarea: "))
            
            # Buscamos si el valor existe
            if index < 0 or index > len(tareas) - 1:
                raise Exception("ID ingresado no existe")
                
            del tareas[index]
            
            print(f"{Fore.BLUE}La tarea con ID {index} ha sido eliminada")
            
            break
        except ValueError as e:
            print(f"{Fore.RED}[ERROR]: {e}\n")
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {e}\n")

    return True