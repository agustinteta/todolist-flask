import os

from flask import Flask
from config import SECRET_KEY, DATABASE, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD

#entorno de la aplicacion
app = Flask(__name__)
app.debug = True
#app.config.from_object('config')
#configuracion del proyecto
app.config.from_mapping(
    SECRET_KEY = SECRET_KEY,
    DATABASE_HOST = DATABASE_HOST,
    DATABASE_PASSWORD = DATABASE_PASSWORD,
    DATABASE_USER = DATABASE_USER,
    DATABASE = DATABASE,
)

# ********** INICIO **************
@app.route('/')
def main():
    return 'Todo list with Flask!'
    
if __name__ == '__main__':
    app.run(port=6000, debug=True)
