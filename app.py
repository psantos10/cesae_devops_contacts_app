import json
import os
import uuid
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ARQUIVO_CONTACTOS = "contactos.json"

def carregar_contactos():
    if os.path.exists(ARQUIVO_CONTACTOS):
        with open(ARQUIVO_CONTACTOS, "r") as file:
            return json.load(file)
    else:
        return []

def guardar_contactos(contactos):
    with open(ARQUIVO_CONTACTOS, "w") as file:
        json.dump(contactos, file)

contactos = carregar_contactos()

@app.route("/")
def index():
  return render_template("index.html", contactos=contactos)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar_contacto():
  if request.method == "GET":
      return "<h1>Adicionar Contacto</h1>"
  elif request.method == "POST":
    novo_contacto = {
      "uuid": str(uuid.uuid4()),
      "nome": request.form["nome"],
      "contacto": request.form["contacto"]
    }
    contactos=carregar_contactos()
    contactos.append(novo_contacto)
    guardar_contactos(contactos)

    return redirect(url_for("index"))


@app.route("/editar/<str:id>", methods=["GET", "POST"])
def editar_contacto(id):
  if request.method == "GET":
      return "<h1>Editar Contacto</h1>"
  elif request.method == "POST":
      return "<h1>Contacto Editado</h1>"

if __name__ == '__main__':
  app.run(debug=True)

