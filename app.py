import json
import os
import uuid
from flask import Flask, render_template, request

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
    novo_uuid = str(uuid.uuid4())

    return f"<h1>Contacto Adicionado: {novo_uuid}</h1>"

@app.route("/editar/<str:id>", methods=["GET", "POST"])
def editar_contacto(id):
  if request.method == "GET":
      return "<h1>Editar Contacto</h1>"
  elif request.method == "POST":
      nome = request.form.get("nome")
      telefone = request.form.get("telefone")

      for contacto in contactos:
          if contacto["id"] == id:
              contacto["nome"] = nome
              contacto["telefone"] = telefone
              break

      guardar_contactos(contactos)
      return f"<h1>Contacto com ID {id} editado com sucesso!</h1>"

if __name__ == '__main__':
  app.run(debug=True)

