from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
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
        <p>Version : V1</p>
        <p><strong>Adresse IP du serveur :</strong> <span id="hostname"></span></p>
        <p>Date actuelle : {{ current_date }}</p>

        <script>
            // Use JavaScript to retrieve the hostname
            document.getElementById('hostname').textContent = window.location.hostname;
        </script>
    </body>
    </html>
    """, current_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
