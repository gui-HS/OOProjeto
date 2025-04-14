from backend.config.config import *
from backend.testeModelo import *

# inserindo a aplicação em um contexto :-/
with app.app_context():

    testePlayer.run(),
    testePlayer2.run()
