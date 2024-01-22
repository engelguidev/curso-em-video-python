try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados inseridos, tente novamente.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')

