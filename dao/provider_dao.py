from db.conexion import conectar
from models.provider import Provider
from models.category import Category


from db.conexion import conectar
from models.provider import Provider

class ProviderDAO:
    def __init__(self):
        self.conn = conectar()

    def get_by_category(self, category_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, name, category_id FROM providers WHERE category_id = %s ORDER BY name",
            (category_id,)
        )
        rows = cursor.fetchall()
        cursor.close()
        return [Provider(id=row[0], name=row[1], category_id=row[2]) for row in rows]



'''

class MedicoDAO:
    @staticmethod
    def obtener_por_categoria(categoria_id: int):  # Metodo 1 Devuelve una  lista de médicos que pertenecen a una categoría especifica
        conexion = conectar()
        medicos = []
        if conexion: # conecta bd
            try:
                with conexion.cursor() as cursor:   # Hace un JOIN entre las tablas medicos y categorias
                    cursor.execute("""
                        SELECT m.id, m.nombre, c.id, c.nombre       
                        FROM medicos m
                        JOIN categorias c ON m.categoria_id = c.id
                        WHERE m.categoria_id = %s
                    """, (categoria_id,))
                    for m_id, m_nombre, c_id, c_nombre in cursor.fetchall():    # Busca todos los médicos que tienen la categoria_id pasada como parámetro
                        categoria = Categoria(c_id, c_nombre)                 # por cada resultado crea un objeto categoria
                        medicos.append(Medico(m_id, m_nombre, categoria))      # Dpues, crea un objeto medico  con esa categoría
            finally:
                conexion.close()
        return medicos

    @staticmethod
    def obtener_por_id(medico_id: int):  # Devuelve un único médico, buscado por su ID
        conexion = conectar()
        medico = None
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("""
                            SELECT m.id, m.nombre, c.id, c.nombre
                            FROM medicos m
                            JOIN categorias c ON m.categoria_id = c.id
                            WHERE m.id = %s
                        """, (medico_id,))
                    resultado = cursor.fetchone()                                              # consulta a bd por un médico con id
                    if resultado:                                                              # si lo encuentra arma  objeto medico
                        m_id, m_nombre, c_id, c_nombre = resultado                             # si no lo encuentra devuelve un None
                        categoria = Categoria(c_id, c_nombre)
                        medico = Medico(m_id, m_nombre, categoria)
            finally:
                conexion.close()
        return medico
'''