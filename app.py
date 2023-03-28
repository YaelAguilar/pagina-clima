from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configura la conexión a la base de datos
config = {
    'user': 'admin',
    'password': 'soyeladmin',
    'host': 'db-sensorclima.ccl4vdhvd0sd.us-east-2.rds.amazonaws.com',
    'database': 'sensores'
}

@app.route('/')
def index():
    # Conecta a la base de datos
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Ejecuta una consulta SQL para obtener los registros
    cursor.execute('SELECT * FROM registros')

    # Recupera los registros y los almacena en una lista
    registros = []
    for registro in cursor:
        registros.append(registro)

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Renderiza la plantilla HTML y pasa la lista de registros como argumento
    return render_template('index.html', registros=registros)

if __name__ == '__main__':
    app.run()
