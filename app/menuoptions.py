
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
        "action": lambda *args: None
    }
]

def menuOptions():
    # Pintamos las opciones
    for option in OPTIONS:
        print(f"{Style.BRIGHT}> {option["value"]}. {option["label"]}.")