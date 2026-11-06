
from colorama import Style
from app.operaciones import añadir_tarea, listar_tareas, eliminar_tarea, buscar_tarea
from app.modelos import Tarea 

OPTIONS = [
    {
        "value": "1",
        "label": "Añadir tarea",
        "action": añadir_tarea
    },
    {
        "value": "2",
        "label": "Eliminar tarea",
        "action": eliminar_tarea
    },
    {
        "value": "3",
        "label": "Listar tarea",
        "action": listar_tareas
    },
    {
        "value": "4",
        "label": "Buscar tarea por palabra clave",
        "action": buscar_tarea
    },
    {
        "value": "0",
        "label": "Salir",
        "action": lambda *args: False
    }
]

def menuOptions() -> None:
    """
    Funcion para imprimir las diferentes opciones del programa
    Retorna:
        None
    """
    # Pintamos las opciones
    for option in OPTIONS:
        print(f"{Style.BRIGHT}> {option["value"]}. {option["label"]}.")
        
def validateOption(val: str) -> None:
    """
    Funcion para validar que la opcion ingresada es valida
    Retorna:
        None
    """
    validOption = False
    
    for option in OPTIONS:
        if option["value"] == val:
            validOption = True
    
    # Si no es una opcion valida, damos error
    if not validOption:
        raise Exception(f"Valor {val} no es una opcion valida.")
    
    
def runOptionAction(val: str, *args) -> bool | Tarea:
    """
    Funcion para ejecutar la funcionalidad de la opcion ingresada
    Retorna:
        bool
    """
    for option in OPTIONS:
        if option["value"] == val:
            return option["action"](*args)
            
    # Si no es ninguna, que repita el flujo
    return True
    