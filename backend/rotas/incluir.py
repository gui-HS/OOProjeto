from backend.config.config import *
from backend.modelo import *

@app.route("/incluir/<string:classe>", methods=['post'])
def incluir(classe):
    dados = request.get_json()  
    try:  
        nova = None
        if classe == "Jogador":
            nova = Jogador.Jogador(**dados)
        elif classe == "ResultadoDaPartida":
            nova = ResultadoDaPartida.ResultadoDaPartida(**dados)
        db.session.add(nova)
        db.session.commit()
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})
