from backend.config.config import *

class ResultadoDaPartida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lifes = db.Column(db.Integer) #Player's life
    strategy = db.Column(db.Integer) #Player's Strategy
    points = db.Column(db.Integer) #Player's points

    def __str__(self):
        return f'{self.id}, {self.lifes}, {self.strategy}, {self.points}'

    def json(self):
        return {
            "id":self.id,
            "lifes":self.lifes,
            "strategy":self.strategy,
            "points":self.points
        }

    