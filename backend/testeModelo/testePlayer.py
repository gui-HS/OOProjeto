from backend.config.config import *
from backend.modelo.Jogador import *

def run():
    print("Teste de Player:")

    p1 = Jogador(nome="player1", pontos = 0, shotPoints = 1, lifes = 300, estrategia = 2, nome_imagem="imagem\\naveBlue.png")
    p2 = Jogador(nome="player2", pontos = 0, shotPoints = 5, lifes = 100, estrategia = 3, nome_imagem="imagem\\naveGreen.png")
    p3 = Jogador(nome="player3", pontos = 0, shotPoints = 10, lifes = 50, estrategia = 4, nome_imagem="imagem\\naveRed.png")
    p4 = Jogador(nome="player4", pontos = 0, shotPoints = 15, lifes = 25, estrategia = 5, nome_imagem="imagem\\navePink.png")
    p5 = Jogador(nome="player5", pontos = 0, shotPoints = 20, lifes = 5,  estrategia = 6, nome_imagem="imagem\\naveYellow.png")
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.commit()
    print(f"Player:{p1}, Player:{p2}")
