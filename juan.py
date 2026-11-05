from flask import Flask, render_template, request
import pymysql

app = Flask(_name_)

#Configuracion de conexion para la base de datos en phpmyadmin
def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='estudiantes_db',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    correo = request.form['correo']

    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO registros (nombre, correo) VALUES (%s, %s)"
            cursor.execute(sql, (nombre,correo))
            conexion.commit()
        conexion.close()
        mensaje = "Datos registrados"
    except Exception as e:
        mensaje = f"Hubo un error: {e}"

    return render_template('index.html', mensaje=mensaje)

if _name_ == '_main_':
    app.run(debug=True)
    