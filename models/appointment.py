from datetime import datetime

class Appointment:
    def __init__(self, id, date_time: datetime, provider_id: int):
        self.id = id
        self.date_time = date_time
        self.provider_id = provider_id

    def __str__(self):
        return self.date_time.strftime('%A %d/%m/%Y - %H:%M')



