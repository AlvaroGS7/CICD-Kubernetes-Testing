# app.py

from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def hello():
    return '¡Hola, mundo! Esta es mi aplicación web en Docker.'

# Ruta adicional
@app.route('/about')
def about():
    return 'Esta es una página de ejemplo.'

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
