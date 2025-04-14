#Perguntas para personalizar o jogo ou algo assim

personalizar = "Nope"

while personalizar != "sim" and personalizar != "nao":
    personalizar = input("Você quer personalizar seu jogo?\n"+
                    "Digite 'sim' ou 'nao': " )

if personalizar == "sim":
    inimigoImagem = input("Digite o nome do inimigo: ")
    inimigoImagem2 = input("Digite o nome do inimigo: ")

elif personalizar != "sim":
    inimigoImagem = "tohou.png"
    inimigoImagem2 = "tohou2.png"