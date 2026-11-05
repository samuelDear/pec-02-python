from typing import Dict, Any

class Tarea:
    tarea: str
    extradata: Dict
    
    def __init__(self, tarea, **kwargs: Any) -> None:
        self.tarea = tarea
        self.extradata = kwargs
        
    def __str__(self) -> str:
        text = f"\tTarea: {self.tarea}\n"
        
        
        if self.extradata:
            detalles = []
            for key, val in self.extradata.items():
                detalles.append(f"{key}: {val}")
            
            detalles = "\n\t  ".join(f"{key}: {val}" for key, val in self.extradata.items())
            text += f"\tDetalles:\n\t  {detalles}"
        else:
            text += "\tDetalles: N/A"
            
        return text