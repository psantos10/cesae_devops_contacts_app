from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/adicionar", methods=["GET", "POST"])
def add_or_save():
  if request.method == "GET":
      return "<h1>Adicionar Contacto</h1>"
  elif request.method == "POST":
      return "<h1>Contacto Adicionado</h1>"
@app.route("/editar", methods=["GET", "POST"])
def edit_or_update():
  if request.method == "GET":
      return "<h1>Editar Contacto</h1>"
  elif request.method == "POST":
      return "<h1>Contacto Editado</h1>"
if __name__ == '__main__':
  app.run(debug=True)

