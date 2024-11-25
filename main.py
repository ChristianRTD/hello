from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, Mundo!"

@app.route('/uce')
def uce():
    return "¡hola amigos universitarios !"


if __name__ == '__main__':
    app.run(debug=True)
