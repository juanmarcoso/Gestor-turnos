from datetime import datetime, timedelta
from db.conexion import conectar

def seed_appointments():
    conn = conectar()
    if conn:
        try:
            with conn.cursor() as cur:
                # Optional: clear old data
                cur.execute("DELETE FROM appointments;")

                base = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

                for day in range(7):  # 7 days from today
                    for hour in [9, 11, 14, 16]:  # 4 time slots per day
                        appointment_datetime = base + timedelta(days=day, hours=(hour - 9))
                        cur.execute(
                            "INSERT INTO appointments (date_time) VALUES (%s);",
                            (appointment_datetime,)
                        )

            conn.commit()
            print("✅ Appointments seeded successfully.")
        except Exception as e:
            print("❌ Error seeding appointments:", e)
        finally:
            conn.close()

if __name__ == "__main__":
    seed_appointments()
