[![Watch the video](https://i.sstatic.net/Vp2cE.png)](https://www.youtube.com/watch?v=bOsZc-12O0o&list=PLveJQlIU8i6raECh2pbosHjOFCBr-wg3S)
## Sobre
```bash
O 'piupiu' é um simulador do gênero "Shoot 'em up".
Você pode criar diversos jogadores e colocá-los em uma partida para decidir quem é o melhor!
Ao final da simulação, será mostrado uma tabela de pontos, contendo os jogadores com mais
pontos, vidas e os que concluíram sua partida em menos tempo.
```

## Instalação Necessária

Instalação de pacotes necessários via [pip](https://pip.pypa.io/en/stable/).

```bash
pip3 install pygame
pip3 install flask
pip3 install flask_sqlalchemy
pip3 install flask_cors
```

## Crie jogadores
```bash
1- No arquivo player.txt, faça seu jogador
2- O primeiro atributo será o id (apenas siga a sequência, não pode haver repetidos)
3- Os próximos atributos serão: Quantidade de vida, estrategia utilizada, pontos por tiro e a cor da nave.
4- Tenha certeza que cada número está separado por vírgulas.
5- Coloque uma linha em branco ao final do arquivo;
Exemplo: 1, 10, 2, 20,Blue
         2, 15, 3, 15,Red

```

## Faça batalhas
```bash
1- No arquivo batalhas.txt, insira o id dos players do arquivo player.txt.
2- Note que, a cada linha, um grupo de jogadores será instanciado na partida.
3- Coloque uma linha em branco ao final do arquivo.
Exemplo: 1,2,3,4
         1,3,5

```
## Estratégias
```bash
Para alcançar os 20 pontos, os jogadores possuem 
diferentes estrategias de movimentação e tiro:

- 1: Jogador Manual.
- 2: Movimentação randomizada.
- 3: De uma ponta à outra.
- 4: Velocidade aumenta com pontos.
- 5: Velocidade aumenta com tickrate do jogo.
- 6: Teletransporte.
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
-Obs: As imagens de obstaculos vão para a pasta de 'inimigos'. O arquivo deve ter formato .png.
```

## Adicionar Cores
```bash
-Insira um arquivo na pasta imagem, manualmente ou seguido o tutorial acima.
-O nome do arquivo deve conter a cor, podendo ser em RGB ou uma cor principal.
Exemplo: naveRed.png ou nave#02fffb.png, contendo o valor em hexa decimal (utilize o valor em hexa decimal, não em rgb).
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

## Créditos
```bash
Musica de fundo:
https://opengameart.org/content/nes-shooter-music-5-tracks-3-jingles

Efeitos sonoros:
https://opengameart.org/content/8-bit-sound-effects-library
Attribute Little Robot Sound Factory, and provide this link where possible: www.littlerobotsoundfactory.com
```
#https://www.makeareadme.com/
