from models.provider import Medico

class Turno:
    def __init__(self, turno_id: int, medico: Medico, fecha: str, horario: str, disponible: bool = True):   # atributos
        self.id = turno_id  # Se mantiene como 'id' / Guarda el número del turno
        self.medico = medico  # Objeto Medico       / Guarda el médico que atiende ese turno
        self.fecha = fecha
        self.horario = horario
        self.disponible = disponible

    def __str__(self):   # método  _ _str_ _ muestra el turno como un texto legible
        return f"Turno #{self.id}: {self.medico} el {self.fecha} a las {self.horario}"



#  medico: Medico   es un objeto de la clase Medico