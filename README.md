# ProyectoIntegradorPython-2025-Solucion202

## 🚀 Cómo comenzar

Para empezar a trabajar con este proyecto, seguí estos pasos:

### 1. Clonar el repositorio

Puede ser a traves de un https o de un ssh. Para hacerlo desde https se puede de la siguiente manera: 

```bash
git clone https://github.com/PowerSystem2024/ProyectoIntegradorPython-2025-Solucion202.git
cd ProyectoIntegradorPython-2025-Solucion202
```

Pero si lo hacemos dsde un SSH debemos primero configurar nuestra PC para que sea reconocido: 

- ### Desde Linux
1. **Generar una clave SSH**

```bash
ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"
```

Presiona Enter para guardar la clave en la ubicación predeterminada (~/.ssh/id_ed25519).

Opcional: Agrega una contraseña segura (recomendado).

2. **Agregar la clave al agente SSH**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

4. **Copiar la clave pública**

```bash
cat ~/.ssh/id_ed25519.pub
```
***Copia el contenido (comienza con ssh-ed25519...).***

4. **Agregar la clave en GitHub**

Ve a GitHub → Settings → SSH and GPG keys → New SSH Key.

Pega la clave pública y guardala.

5. **Probar la conexión SSH**

```bash
ssh -T git@github.com
```

Debes ver:

```bash
Hi [tu_usuario]! You've successfully authenticated...
```

6. **Clonar el repositorio con SSH**

```bash
git clone git@github.com:usuario/repositorio.git
```

### Configurar SSH en Windows

1. **Instalar Git y OpenSSH (si no está instalado)**

Descarga Git desde git-scm.com (incluye OpenSSH).

O instala OpenSSH desde PowerShell (Admin):

```bash
    Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
    Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

2. **Generar clave SSH (Git Bash o PowerShell)**

```bash
ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"
```

Presiona Enter para guardar en **C:\Users\TuUsuario\.ssh\id_ed25519.**

Opcional: Establece una contraseña.

1. **Iniciar el agente SSH y agregar la clave**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
4. **Copiar la clave pública**

```bash
cat ~/.ssh/id_ed25519.pub
```
***Copia el contenido.***

5. **Agregar la clave en GitHub**

Ve a GitHub → Settings → SSH and GPG keys → New SSH Key.

Pega la clave y guarda.

6. **Probar la conexión**

```bash
ssh -T git@github.com
```

Debes ver:

```bash
Hi [tu_usuario]! You've successfully authenticated...
```

7. **Clonar con SSH**

```bash
git clone git@github.com:usuario/repositorio.git
```

## 2. Crear y activar un entorno virtual

Para empezar a trabajar con este proyecto, seguí estos pasos:

<table border="1">
    <thead>
      <tr>
        <th>Sistema Operativo</th>
        <th>Crear entorno virtual</th>
        <th>Activar entorno</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Windows </td>
        <td><code>python -m venv .venv</code></td>
        <td><code>.venv\Scripts\activate</code></td>
      </tr>
      <tr>
        <td>Linux / macOS</td>
        <td><code>python3 -m venv .venv</code></td>
        <td><code>source .venv/bin/activate</code></td>
      </tr>
    </tbody>
  </table>

## 3. Instalar las dependencias

Para guardar las depencias instaladas y mostrar las que instalameos para que nuestro proyecto funciones, hacemos lo siguiente (siempre dentro de nuestro enotorno virtual): 

```bash
pip freeze > requirements.txt
```

Para instalarlas: 

```bash
pip install -r requirements.txt
```

## 🧠 patrón DAO

El **patrón DAO (Data Access Object)** es una práctica de diseño utilizada para **separar la lógica de acceso a datos** del resto del sistema. Este patrón permite:

- Encapsular el acceso a la base de datos.
- Centralizar las operaciones CRUD (crear, leer, actualizar, eliminar).
- Hacer que el código sea más mantenible, reutilizable y testeable.

---

## 📂 Estructura del Proyecto

```
mProyectoIntegradorPython-2025-Solucion202/
│
├── main.py                # Punto de entrada del programa
├── db/
│   ├── __init__.py
│   └── conexion.py        # Conexión a la base de datos PostgreSQL
│
├── models/
│   ├── __init__.py
│   └── turno.py(ejemplo)           # Clase Turno: representación del modelo de dominio
│
├── dao/
│   ├── __init__.py
│   └── turno_dao.py(ejemplo)       # Acceso a datos de Turno (DAO)
│
└── requirements.txt       # Dependencias del proyecto (ej. psycopg2)
```

---

## 🔄 Cómo se conectan los componentes

### `models/`

Contiene las **clases de dominio**. Cada clase representa una entidad lógica del sistema (por ejemplo, un `Turno`). No incluye lógica de base de datos.

### `dao/`

Contiene las **clases DAO**, que encapsulan la lógica de acceso a la base de datos. Estas clases se encargan de leer y escribir datos del modelo (`Turno`) en la base de datos utilizando SQL.

### `db`

Contiene el archivo de conexión a la base de datos (`conexion.py`), centralizando las credenciales y parámetros de conexión. Todos los DAOs deben usar esta conexión para interactuar con PostgreSQL.

### `main.py`

Este archivo contiene la **lógica de interacción con el usuario**. Es responsable de recibir inputs, mostrar menús, y utilizar los DAOs para ejecutar operaciones sobre los datos.

---

## 🧭 Reglas de trabajo con este patrón

1. **No mezclar SQL en `main.py`**: todas las consultas deben estar en los DAOs.
2. **No acceder directamente a la base desde modelos o menú**: usar siempre las clases DAO.
3. **Los modelos (`models/`) solo contienen atributos y comportamiento lógico de la entidad**, sin acceso a datos.
4. **Cada clase del dominio debe tener su propio DAO** (ej: `Turno` → `TurnoDAO`).
5. **La conexión se maneja desde `database/conexion.py`**. No abrir conexiones directas en los DAOs.
6. **El menú solo orquesta las acciones**: crea objetos y delega la persistencia al DAO correspondiente.

---
