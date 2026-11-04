
from colorama import Style

OPTIONS = [
    {
        "value": "1",
        "label": "Añadir tarea",
        "action": lambda *args: None
    },
    {
        "value": "2",
        "label": "Eliminar",
        "action": lambda *args: None
    },
    {
        "value": "3",
        "label": "Listar tarea",
        "action": lambda *args: None
    },
    {
        "value": "4",
        "label": "Buscar tarea por palabra clave",
        "action": lambda *args: None
    },
    {
        "value": "0",
        "label": "Salir",
        "action": lambda *args: False
    }
]

def menuOptions():
    # Pintamos las opciones
    for option in OPTIONS:
        print(f"{Style.BRIGHT}> {option["value"]}. {option["label"]}.")
        
def validateOption(val: str) -> None:
    validOption = False
    
    for option in OPTIONS:
        if option["value"] == val:
            validOption = True
    
    # Si no es una opcion valida, damos error
    if not validOption:
        raise Exception(f"Valor {val} no es una opcion valida.")
    
    
def runOptionAction(val: str) -> bool:
    for option in OPTIONS:
        if option["value"] == val:
            return option["action"]()
            
    # Si no es ninguna, que repita el flujo
    return True
    