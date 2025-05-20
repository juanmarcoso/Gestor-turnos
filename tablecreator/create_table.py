from db.conexion import conectar

def crear_tablas():

    cursor = conectar
    cursor.execute("""

    -- Create categories table
    CREATE TABLE IF NOT EXISTS categories (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );

    -- Create providers table
    CREATE TABLE IF NOT EXISTS providers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    );

    -- Drop appointments table if it already exists
    DROP TABLE IF EXISTS appointments;

    -- Recreate appointments table with provider_id
    CREATE TABLE appointments (
        id SERIAL PRIMARY KEY,
        date_time TIMESTAMP NOT NULL,
        provider_id INTEGER NOT NULL,
        FOREIGN KEY (provider_id) REFERENCES providers(id)
    );

    -- Seed categories
    INSERT INTO categories (name) VALUES 
        ('Dental'),
        ('Physical Therapy'),
        ('Dermatology');

    -- Seed providers
    INSERT INTO providers (name, category_id) VALUES 
        ('Dr. Smith', 1),         -- Dental
        ('Dr. Johnson', 1),       -- Dental
        ('Therapist Lee', 2),     -- Physical Therapy
        ('Therapist Kim', 2),     -- Physical Therapy
        ('Dr. White', 3),         -- Dermatology
        ('Dr. Brown', 3);         -- Dermatology

    -- Seed appointments (example for a few providers)
    INSERT INTO appointments (date_time, provider_id) VALUES
        ('2025-05-15 09:00:00', 1),
        ('2025-05-15 11:00:00', 1),
        ('2025-05-15 14:00:00', 2),
        ('2025-05-16 09:00:00', 2),
        ('2025-05-16 11:00:00', 3),
        ('2025-05-16 14:00:00', 3),
        ('2025-05-17 09:00:00', 4),
        ('2025-05-17 11:00:00', 5),
        ('2025-05-18 09:00:00', 6),
        ('2025-05-18 11:00:00', 6),
    """)
    conectar.commit()
    cursor.close()
    conectar.close()