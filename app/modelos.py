from typing import Dict, Any

class Tarea:
    tarea: str
    extradata: Dict
    
    def __init__(self, tarea, **kwargs: Any) -> None:
        self.tarea = tarea
        print(kwargs)
        
    def __str__(self) -> str:
        return f"- Tarea: {self.tarea}\n- Detalles: {self.extradata}"