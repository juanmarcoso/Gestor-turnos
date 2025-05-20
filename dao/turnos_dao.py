from db.conexion import conectar
from models.turnos import Turno
from dao.provider_dao import MedicoDAO

class TurnoDAO:
    @staticmethod
    def obtener_disponibles_por_medico(medico_id: int):
        conexion = conectar()
        turnos = []
        medico = MedicoDAO.obtener_por_id(medico_id)    # usa medicoDao para obtener un objeto Medico
        if conexion and medico:
            try:
                with conexion.cursor() as cursor:       # Hace una consulta a la tabla turnos para buscar todos los turnos disponibles de ese médico
                    cursor.execute("""
                        SELECT id, fecha, horario, disponible
                        FROM turnos
                        WHERE medico_id = %s AND disponible = TRUE
                        ORDER BY fecha, horario
                    """, (medico_id,))                                                            # Con los datos que trae craea objetos turno asociandolos al Medico que se obtuvo
                    for turno_id, fecha, horario, disponible in cursor.fetchall():  # Cambié "id" a "turno_id"
                        turnos.append(Turno(turno_id, medico, fecha, horario, disponible))  # También cambié "id" por "turno_id"
            finally:
                conexion.close()
        return turnos
