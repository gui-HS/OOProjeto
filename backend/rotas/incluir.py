from backend.config.config import *
from backend.modelo.jogador import *
from backend.modelo.jogador2 import *
from backend.modelo.armas import *

@app.route("/incluir/<string:classe>", methods=['post'])
def incluir(classe):
    dados = request.get_json()  
    try:  
        nova = None
        if classe == "Jogador":
            nova = Jogador(**dados)
        elif classe == "Jogador2":
            nova = Jogador2(**dados)
        db.session.add(nova)
        db.session.commit()
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})
