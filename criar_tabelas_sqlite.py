from backend.config.config import *
from backend.modelo import *

# inserindo a aplicação em um contexto :-/
with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    print("Criação de BD e tabelas bem sucedidada")
