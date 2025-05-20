from dao.appointment_dao import AppointmentDAO

class AppointmentService:
    def __init__(self):
        self.dao = AppointmentDAO()

    def list_appointments(self):
        return self.dao.get_all()

    def book_appointment(self, index):
        appointments = self.dao.get_all()
        if 0 <= index < len(appointments):
            selected = appointments[index]
            self.dao.remove_appointment(selected)
            return selected
        else:
            return None
        
    def list_appointments_for_provider(self, provider_id):
        return self.dao.get_by_provider(provider_id)

    def book_appointment_by_provider(self, provider_id, index):
        appointments = self.dao.get_by_provider(provider_id)
        if 0 <= index < len(appointments):
            selected = appointments[index]
            self.dao.remove_appointment(selected)
            return selected
        return None
