condicao = True
while condicao:
    try:
        n = int(input("Escolha um número para ser convertido:"))
    except:
        print("OCORREU ALGUM ERRO!"
              "Verifique se você realmente digitou um número...")