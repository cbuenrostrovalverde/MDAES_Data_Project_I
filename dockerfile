# Generamos una imagen de Python. En este caso la última.
FROM python:latest

# Configuración del directorio de ejecución.
WORKDIR /app

# Copia del archivo requirements.txt para la imagen creada.
COPY requirements.txt .

# Dependencias
RUN pip install --no-chache-dir -r requirements.txt \ && apt-get clean \ && rm -rf /var/lib/apt/list/*

# Copia de los archivos .py necesarios para la ejecución del entorno.
COPY generador.py .
COPY suma.py .

#
ENTRYPOINT [ "python", "requierements.txt", "generador.py", "suma.py" ]


