## Sobre

```bash
O 'piupiu' é um jogo do gênero "Shoot 'em up" multiplayer.
Seu objetivo é alcançar vinte pontos antes do seu adversário
```

## Instalação Necessária

Instalação de pacotes necessários via [pip](https://pip.pypa.io/en/stable/).

```bash
pip3 install pygame
pip3 install flask
pip3 install flask_sqlalchemy
pip3 install flask_cors
```

## Controles

```bash
**Player 1:**
A - Mover para a esquerda
D - Mover para a direita
Espaço - Atirar

**Player 2:**
Seta para esquerda - Mover para a esquerda
Seta para direita - Mover para a direita
P - Atirar
```

## Inserir Imagens de Obstáculos por rota de upload:

```bash
-Inicie o arquivo 'ex_backend'
-Abra o terminal do seu computador
-Escreva: curl -i -X POST -F files=@imagem.png http://127.0.0.1:5000/upload
-Em que @imagem.png corresponde ao arquivo a ser adicionado
-Inicie o jogo no arquivo 'jogo.py'
-Digite 'sim' no terminal do python para personalizar os obstaculos
-Digite o nome do arquivo
-Exemplo: tohou.png
-Obs: As imagens de obstaculos vão para a pasta de 'inimigos'
```

## Atualizações:
*Versão 1.2:
```bash
-Exclusão de imagens fora da pasta de imagens C:
-Inclusão do arquivo .gitignore
-Importação de diversas classes via __all__ em modulo
-Classe Player,Player2 movida a um arquivo exclusivo
-Objetos em pasta separada
-Criação da pasta "web" para arquivos html e javascript
-Inclusão da rota de upload para imagens
-Criação da pasta 'objetos' para instâncias de classes
-Upload de arquivos
-Obstáculos possuem imagens
```
#https://www.makeareadme.com/
