import os
from flask_cors import CORS
from dotenv import load_dotenv  
from . import create_app
from .utils.clock import clock as clock_util

app = create_app()

# Enable CORS globally for the app
CORS(app)


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la conexión a MySQL utilizando variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

@app.route('/clock')
def clock():
  return clock_util()

if __name__ == '__main__':
  app.run(host="0.0.0.0" , port=5000) 