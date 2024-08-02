from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'user': 'root',
    'password': 'sistemasUNI2016',
    'host': 'LocalHost',
    'database': 'proyecto_efsrtii'
}

def insert_into_db(data):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = """
    INSERT INTO cotizaciones (nombre, correo, telefono, destino, fecha_salida, fecha_regreso, num_adultos, num_niños, comentarios)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data['nombre'], data['correo'], data['telefono'], data['destino'],
        data['fecha_salida'], data['fecha_regreso'], data['num_adultos'],
        data['num_niños'], data['comentarios']
    ))
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/')
def index():
    return render_template('Inicio.html')

@app.route('/cotizacion', methods=['POST'])
def cotizacion():
    data = {
        'nombre': request.form['nombre'],
        'correo': request.form['correo'],
        'telefono': request.form['telefono'],
        'destino': request.form['destino'],
        'fecha_salida': request.form['fecha_salida'],
        'fecha_regreso': request.form['fecha_regreso'],
        'num_adultos': request.form['num_adultos'],
        'num_niños': request.form['num_niños'],
        'comentarios': request.form['comentarios']
    }
    insert_into_db(data)
    return redirect(url_for('agradecimiento'))

@app.route('/agradecimiento')
def agradecimiento():
    return app.send_static_file('agradecimiento.html')

if __name__ == '__main__':
    app.run(debug=True)
