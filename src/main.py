# iniciando librerias
# comentado1
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from horoscopo import HoroscopoChino
app = Flask(__name__)


# creando rutas
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def logica():
    # recuperar desde el formulario la variable anyo
    anyo = int(request.form['anyo'])

    # crear el objeto
    persona = HoroscopoChino(anyo)

    global signo_usuario
    # llamar a nuestro método signo
    signo_usuario = persona.signo()

    return redirect(url_for('signo'))


@app.route('/signo')
def signo():
    return render_template('signo.html', signo_usuario=signo_usuario)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
