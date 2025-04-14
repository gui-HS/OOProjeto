from backend.config.config import *
from backend.modelo.jogador import *

def run():
    print("Teste de Player:")

    p1 = Jogador(nome="Gabriel", nome_imagem="../../imagem/nave.png")
    p2 = Jogador(nome="Fernando", nome_imagem="../../imagem/nave.png")
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(f"Player:{p1}, Player:{p2}")
