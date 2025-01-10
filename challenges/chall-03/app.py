from flask import Flask, render_template_string, request
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/") 
db = client['flask_app']
collection = db['requests']

@app.route("/")
def home():
    # Enregistrer l'IP et la date de la requête dans MongoDB
    client_ip = request.remote_addr
    now = datetime.now()
    collection.insert_one({"ip": client_ip, "date": now})

    # Récupérer les 10 derniers enregistrements
    last_records = list(collection.find().sort("_id", -1).limit(10))
    formatted_records = [
        {"ip": rec["ip"], "date": rec["date"].strftime("%Y-%m-%d %H:%M:%S")} for rec in last_records
    ]
    # Serve the HTML page
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mon Projet</title>
    </head>
    <body>
        <h1>Bienvenue sur mon site web</h1>
        <p>Nom : OUALGHAZI</p>
        <p>Nom du Projet : Mon Projet</p>
        <p>Version : V2</p>
        <p><strong>Adresse IP du serveur :</strong> <span id="hostname"></span></p>
        <p>Date actuelle : {{ current_date }}</p>

        <h2>Derniers enregistrements :</h2>
        <ul>
            {% for record in records %}
                <li>IP : {{ record.ip }}, Date : {{ record.date }}</li>
            {% endfor %}
        </ul>

        <script>
            // Utiliser JavaScript pour afficher l'adresse IP/hostname
            document.getElementById('hostname').textContent = window.location.hostname;
        </script>
    </body>
    </html>
    """, current_date=now.strftime("%Y-%m-%d %H:%M:%S"), records=formatted_records)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)