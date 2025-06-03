FROM python:3.13-alpine

# Instalar dependencias para compilar paquetes Python nativos
RUN apk add --no-cache gcc musl-dev libffi-dev

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements.txt y luego instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente
COPY . .

# Comando por defecto para arrancar app (cámbialo según tu app)
CMD ["python", "app.py"]
