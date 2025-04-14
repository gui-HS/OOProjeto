from backend.config.config import *

# classe JOGADOR 2!!
class Jogador2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    nome_imagem = db.Column(db.Text)

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.nome_imagem}'

    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "nome_imagem":self.nome_imagem
        }

