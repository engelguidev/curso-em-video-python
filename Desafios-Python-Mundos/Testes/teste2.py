continua = True
while continua:
  try:
    n = int(input("Escolha um número para ser convertido:"))
    if isinstance(n, int):
      continua = False
  except:
    print("OCORREU ALGUM ERRO!"
    " Verifique se você realmente digitou um número...")