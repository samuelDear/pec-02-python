from typing import Any, List
from colorama import Fore, Style
from app.modelos import Tarea

# Funciones
def añadir_tarea(*args: Any) -> Tarea:
    """
    Agregar una tarea registrando datos requeridos y opcionales
    Retorna:
        Class Tarea
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
        
        print(f"\n{Fore.BLUE}- AÑADIR TAREA FINALIZADO\n")
        return Tarea(tarea, **extradata)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {e}\n")
    
def notAllowEmptyVal(label: str, field: str = "campo") -> str:
    """
    Funcion para validar que el input no es vacio
    Retorna:
        str
    """
    while True:
        value = input(label).strip()
                
        # Si esta vacio, volvemos a pedirselo
        if not value:
            print(f"{Fore.RED}[ERROR]: El {field} no puede ser vacio.")
            continue
                    
        # Si llego aqui es que tiene data
        return value
    
def listar_tareas(tareas: List[Tarea] = []) -> bool:
    """
    Funcion para listar todas las tareas registradas
    Retorna:
        None
    """
    
    separatorPrint()
    print(f"{Fore.BLUE}- LISTAR TAREAS")
    print("\nListado de tareas:")
    
    if isTareasEmpty(tareas):
        return True
        
    showListTareas(tareasArr = tareas)
    
    print("")
    return True

def showListTareas(tareasArr: List[Tarea] = []) -> None:
    """
    Funcion para mostrar cada una de las tareas ingresadas
    """
    index = 0
    for tarea in tareasArr:
        print(f"- ID: {Style.BRIGHT}{index}")
        print(f"{tarea}")
        index += 1
        if index != len(tareasArr):
            print(f"{Style.DIM}{"**" * 32}")
        
       
def separatorPrint() -> None:
    """
    Funcion para imprimir una separacion entre cada funcionalidad
    """
    print(f"\n{Fore.GREEN}{"*" * 64}\n")
    
def buscar_tarea(tareas: List[Tarea] = []) -> bool:
    """
    Funcion para buscar alguna tarea en concreto
    Retorna:
        bool
    """
    
    separatorPrint()
    print(f"{Fore.BLUE}- BUSCAR TAREAS\n")
    
    if isTareasEmpty(tareas):
        return True
    
    # Validamos si alguna o algunas tareas tienen la palabra ingresada por el usuario
    search = notAllowEmptyVal("> Ingrese que palabra o texto desea buscar: ")
    
    # Recorremos cada tarea y vemos si coincide algo
    findedTareas = []
    for tarea in tareas:
        if search.lower() in tarea.tarea.lower():
            findedTareas.append(tarea)
    
    # validamos si se encontro algo
    if len(findedTareas) == 0:
        print(f"{Fore.YELLOW}No se encontraron tareas con el texto '{search}'\n")
        return True
    
    # Imprimimos lo que encontramos
    print(f"\n{Style.BRIGHT}Tareas encontradas ({len(findedTareas)}): \n")
    showListTareas(tareasArr = findedTareas)
    
    return True
    
def isTareasEmpty(tareas: List[Tarea] = []) -> bool:
    """
    Funcion para validar si hay tareas
    """
    # Validamos si hay tareas, si no mostramos un mensaje
    if len(tareas) == 0: 
        print(f"{Fore.YELLOW}No hay tareas registradas\n")
        return True
    
    return False
    
def eliminar_tarea(tareas: List[Tarea] = []) -> bool:
    """
    Funcion para eliminar una tarea por su Index
    Retorna:
        bool
    """
    
    separatorPrint()
    print(f"{Fore.BLUE}- ELIMINAR TAREA\n")
    
    # Validamos si hay tareas, si no mostramos un mensaje
    if isTareasEmpty(tareas):
        print("\n")
        return True
    
    showListTareas(tareas)
    
    index = ''
    
    print(f"\n{Style.BRIGHT}Ingrese el ID de la tarea que quiere eliminar (Pulsa Enter en blanco si deseas cancelar):\n")
    
    while True:
        try:
            # Pedimos el indice que quiere eliminar
            index = input("> ID de la tarea: ")
            
            if index == '':
                print(f"\n- {Fore.CYAN}Operacion cancelada\n")
                break
            
            index = int(index)
            
            # Buscamos si el valor existe
            if index < 0 or index > len(tareas) - 1:
                raise Exception("ID ingresado no existe")
                
            del tareas[index]
            
            print(f"- {Fore.BLUE}La tarea con ID {index} ha sido eliminada\n")
            
            break
        except ValueError as e:
            print(f"{Fore.RED}[ERROR]: El valor ingresado es incorrecto\n")
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {e}\n")

    return True