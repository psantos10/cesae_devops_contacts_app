from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/adicionar")
def add():
  return "<h1>Adicionar Contacto</h1>"

@app.route("/adicionar", methods=["POST"])
def save():
  return "<h1>Contacto Adicionado</h1>"

@app.route("/editar")
def edit():
  return "<h1>Editar Contacto</h1>"

@app.route("/editar", methods=["POST"])
def update():
  return "<h1>Contacto Editado</h1>"


if __name__ == '__main__':
  app.run(debug=True)

