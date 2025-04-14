from backend.config.config import *
from backend.rotas.incluir import *
from backend.rotas.listar import *

# rota padrão
@app.route("/")
def inicio():
    return 'UwU'

# inserindo a aplicação em um contexto :-/
with app.app_context():


# curl -i -X POST -F files=@imagem1.png http://127.0.0.1:5000/upload
# curl -i -X POST -F files="@pdf1 14pgs.pdf" http://127.0.0.1:5000/upload
    @app.route('/upload', methods= ['POST'])
    def upload_file():
        f = request.files['files']
        print(f.filename)
        caminho = os.path.dirname(os.path.abspath(__file__))
        com_pasta = os.path.join(caminho, 'inimigo')
        completo = os.path.join(com_pasta, f.filename)
        f.save(completo)
        return '200'
    
    app.debug = True
    app.run()
