from flask import Flask, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from config import db  # Importar la configuración de la base de datos

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        # Encriptar la contraseña
        hashed_password = generate_password_hash(contraseña)

        cursor = db.cursor()
        cursor.execute("INSERT INTO users (nombre, contraseña) VALUES (%s, %s)", (nombre, hashed_password))
        db.commit()

        return "usuario registrado"
    except Exception as e:
        print(f"Error en el registro: {e}")
        return f"Error en el registro: {e}"

@app.route('/login', methods=['POST'])
def login():
    try:
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        cursor = db.cursor()
        cursor.execute("SELECT contraseña FROM users WHERE nombre = %s", (nombre,))
        result = cursor.fetchone()

        if result and check_password_hash(result[0], contraseña):
            return "Inicio de sesión exitoso"
        else:
            return "Nombre de usuario o contraseña incorrectos"
    except Exception as e:
        print(f"Error en el inicio de sesión: {e}")
        return f"Error en el inicio de sesión: {e}"

if __name__ == '__main__':
    app.run(debug=True)
