from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Aquí podrías guardar en base de datos, enviar email, etc.
        print("Mensaje recibido:", nombre, email, mensaje)

        return render_template('contact.html', enviado=True)

    return render_template('contact.html', enviado=False)

if __name__ == '__main__':
    app.run(debug=True)