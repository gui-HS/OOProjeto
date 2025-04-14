from backend.config.config import *
from backend.modelo.jogador import *
from backend.modelo.jogador2 import *
from backend.modelo.armas import *

@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "Jogador":
       dados = db.session.query(Jogador).all()  
    elif classe == "Jogador2":
       dados = db.session.query(Jogador2).all()   
    if dados:
      lista_jsons = [x.json() for x in dados]

      meujson = {"resultado": "ok"}
      meujson.update({"detalhes": lista_jsons})
      return jsonify(meujson)
    else:
      return jsonify({"resultado":"erro", "detalhes":"classe informada inválida: "+classe})
