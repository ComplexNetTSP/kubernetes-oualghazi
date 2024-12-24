# Utilise une image Python officielle
FROM python:3.9-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app


RUN pip install flask

# Exposer 
EXPOSE 5000

#  lancer l'application
CMD ["python", "app.py"]
