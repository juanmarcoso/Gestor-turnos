from db.conexion import conectar

def inicializar_db():
    conexion = conectar()
    if not conexion:
        print("❌ No se pudo conectar a la base de datos.")
        return

    print("✅ Base de datos inicializada con éxito.")

if __name__ == "__main__":
    inicializar_db()