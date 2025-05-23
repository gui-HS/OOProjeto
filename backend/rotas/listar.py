from backend.config.config import *
from backend.modelo.jogador import *
from backend.modelo.shoot import *

@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "Jogador":
       dados = db.session.query(Jogador).all()  
    if dados:
      lista_jsons = [x.json() for x in dados]

      meujson = {"resultado": "ok"}
      meujson.update({"detalhes": lista_jsons})
      return jsonify(meujson)
    else:
      return jsonify({"resultado":"erro", "detalhes":"classe informada inválida: "+classe})
