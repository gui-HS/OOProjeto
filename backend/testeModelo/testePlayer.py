from backend.config.config import *
from backend.modelo.jogador import *

def run():
    print("Teste de Player:")

    p1 = Jogador(nome="player1", nome_imagem="imagem\\naveBlue.png")
    p2 = Jogador(nome="player2", nome_imagem="imagem\\naveGreen.png")
    p3 = Jogador(nome="player3", nome_imagem="imagem\\naveRed.png")
    p4 = Jogador(nome="player4", nome_imagem="imagem\\navePink.png")
    p5 = Jogador(nome="player5", nome_imagem="imagem\\naveYellow.png")
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.commit()
    print(f"Player:{p1}, Player:{p2}")
