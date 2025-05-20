import os
import psycopg2

def conectar():
    try:
        # Establecer conexión
        conexion = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            port=os.environ.get("DB_PORT")
        )
        
        # Crear cursor
        cursor = conexion.cursor()
        
        # Ejecutar comandos SQL en bloques separados para mejor manejo de errores
        try:
            # Crear tablas
            cursor.execute("""
                INSERT INTO categories (name)
                SELECT unnest(array['Dental', 'Physical Therapy', 'Dermatology'])
                WHERE NOT EXISTS (SELECT 1 FROM categories);

                -- Para providers (similar)

                INSERT INTO providers (name, category_id)
                SELECT * FROM (VALUES
                    ('Dr. Smith', 1),
                    ('Dr. Johnson', 1),
                    ('Therapist Lee', 2),
                    ('Therapist Kim', 2),
                    ('Dr. White', 3),
                    ('Dr. Brown', 3)
                ) AS new_providers(name, category_id)
                WHERE NOT EXISTS (SELECT 1 FROM providers);""")
            
            cursor.execute("DROP TABLE IF EXISTS appointments;")
            
            cursor.execute("""
                CREATE TABLE appointments (
                    id SERIAL PRIMARY KEY, 
                    date_time TIMESTAMP NOT NULL, 
                    provider_id INTEGER NOT NULL,  
                    FOREIGN KEY (provider_id) REFERENCES providers(id)
                );
            """)
            
            # Insertar datos
            cursor.execute("""
                INSERT INTO categories (name) 
                VALUES ('Dental'), ('Physical Therapy'), ('Dermatology')
                ON CONFLICT DO NOTHING;
            """)
            
            cursor.execute("""
                INSERT INTO providers (name, category_id) 
                VALUES 
                    ('Dr. Smith', 1),
                    ('Dr. Johnson', 1),
                    ('Therapist Lee', 2),
                    ('Therapist Kim', 2),
                    ('Dr. White', 3),
                    ('Dr. Brown', 3)
                ON CONFLICT DO NOTHING;
            """)
            
            cursor.execute("""
                INSERT INTO appointments (date_time, provider_id) 
                VALUES
                    ('2025-05-15 09:00:00', 1),
                    ('2025-05-15 11:00:00', 1),
                    ('2025-05-15 14:00:00', 2),
                    ('2025-05-16 09:00:00', 2),
                    ('2025-05-16 11:00:00', 3),
                    ('2025-05-16 14:00:00', 3),
                    ('2025-05-17 09:00:00', 4),
                    ('2025-05-17 11:00:00', 5),
                    ('2025-05-18 09:00:00', 6),
                    ('2025-05-18 11:00:00', 6)
                ON CONFLICT DO NOTHING;
            """)
            
            conexion.commit()
            
        except Exception as e:
            conexion.rollback()
            print("Error al ejecutar consultas SQL:", e)
            raise
        
        finally:
            cursor.close()
        
        return conexion
        
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None