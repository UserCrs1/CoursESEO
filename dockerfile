FROM python:3.9-slim
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer la librairie DANS l'image
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY app.py .
CMD ["python", "app.py"]