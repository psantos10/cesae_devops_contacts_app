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
      return '''
      <style>
      body {
        font-family: Arial, sans-serif;
        background: #f0f2f5;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
      }

      .form-container {
        background: #fff;
        padding: 20px 30px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        width: 300px;
      }

      .form-container h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
      }

      label {
        display: block;
        margin-top: 10px;
        color: #555;
      }

      input[type="text"],
      input[type="tel"] {
        width: 100%;
        padding: 10px;
        margin-top: 5px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
      }

      button {
        margin-top: 20px;
        width: 100%;
        padding: 10px;
        background: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
      }

      button:hover {
        background: #45a049;
      }
      </style>

      <h1>Adicionar Contacto</h1>

      <form action="#" method="post">
      <label for="nome">Nome:</label>
      <input type="text" id="nome" name="nome" required>

      <label for="telefone">Telefone:</label>
      <input type="tel" id="telefone" name="telefone" required placeholder="(XX) XXXXX-XXXX">

      <button type="submit">Enviar</button>
      </form>
      '''

  elif request.method == "POST":
    novo_uuid = str(uuid.uuid4())

    return f"<h1>Contacto Adicionado: {novo_uuid}</h1>"

@app.route("/editar/<string:id>", methods=["GET", "POST"])
def editar_contacto(id):
  if request.method == "GET":
      return "<h1>Editar Contacto</h1>"
  elif request.method == "POST":
      return "<h1>Contacto Editado</h1>"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
