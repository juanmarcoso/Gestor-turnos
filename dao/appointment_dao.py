from models.appointment import Appointment
from db.conexion import conectar


class AppointmentDAO:
    def __init__(self):
        self.conn = conectar()
        self.conn.autocommit = True  # Optional, depends on your usage

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, date_time FROM appointments ORDER BY date_time")
        rows = cursor.fetchall()
        cursor.close()
        # Map rows to Appointment objects, include ID if needed
        return [Appointment(date_time=row[1]) for row in rows]

    def remove_appointment(self, appointment: Appointment):
        cursor = self.conn.cursor()
        # Assuming you have an 'id' attribute; if not, you might want to add it to Appointment
        cursor.execute(
            "DELETE FROM appointments WHERE date_time = %s",
            (appointment.date_time,)
        )
        cursor.close()


    def get_by_provider(self, provider_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, date_time, provider_id FROM appointments WHERE provider_id = %s ORDER BY date_time",
            (provider_id,)
        )
        rows = cursor.fetchall()
        cursor.close()
        return [Appointment(id=row[0], date_time=row[1], provider_id=row[2]) for row in rows]

