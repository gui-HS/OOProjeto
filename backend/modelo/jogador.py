from backend.config.config import *

# classe JOGADOR!!
class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    color = db.Column(db.Text)
    pontos = db.Column(db.Integer)
    shotPoints = db.Column(db.Integer)
    lifes = db.Column(db.Integer)
    estrategia = db.Column(db.Integer)

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.color}, {self.pontos}, {self.lifes}, {self.estrategia}'

    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "color":self.color,
            "pontos":self.pontos,
            "lifes":self.lifes,
            "estrategia":self.estrategia
        }