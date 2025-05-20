#FROM python:3.14.0b1-alpine

#WORKDIR /app

#Instala dependencias de sistema para psycopg2
#RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

#Copia los requirements primero para aprovechar la caché de Docker
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

#Copia el resto de los archivos
#COPY . .

#Especifica el comando a ejecutar
#CMD ["python3", "main.py"]

FROM python:3.14.0b1-alpine

WORKDIR /app

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecutar primero la inicialización de la base de datos y luego la app principal
CMD ["sh", "-c", "python init_db.py && python main.py"]