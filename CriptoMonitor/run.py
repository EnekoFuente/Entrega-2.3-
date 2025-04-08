from flask import Flask
from app import models
from app.api import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    models.init_db()
    print("Servidor iniciando en http://127.0.0.1:5000")
    app.run(debug=True)
