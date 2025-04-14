from backend.config.config import *
from backend.modelo.jogador2 import *

def run():
    print("Teste de Player:")

    pp1 = Jogador2(nome="Amanda", nome_imagem="../../imagem/nave2.png")
    pp2 = Jogador2(nome="Larissa", nome_imagem="../../imagem/nave2.png")
    db.session.add(pp1)
    db.session.add(pp2)
    db.session.commit()
    print(f"Player:{pp1}, Player:{pp2}")