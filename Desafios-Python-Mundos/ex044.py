print('-'*40)
print('{:^40}'.format('LOJAS DO GORDIN'))
print('-'*40)
preco = float(input('Valor total das compras: R$ '))
print('{:^40}'.format('FORMA DE PAGAMENTO'))
print('[1] - à vista no dinheiro, débito ou pix')
print('[2] - à vista no cartão de crédito')
print('[3] - 2x no cartão de crédito')
print('[4] - 3x ou mais no cartão de crédito')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    vista = (preco - (preco*0.10))
    print('Pagamentos à vista têm 10% de desconto, sua compra de R$ {:.2f} irá custar R$ {:.2f}.'.format(preco, vista))
elif opcao == 2:
    vista = (preco - (preco*0.05))
    print('Pagamentos à vista no cartão de crédito têm 5% de desconto, sua compra de R$ {:.2f} irá custar R$ {:.2f}'.format(preco, vista))
elif opcao == 3:
    duas = (preco/2)
    print('Pagamento em duas vezes sem juros, R$ {:.2f} em duas vezes de R$ {:.2f}'.format(preco, duas))
elif opcao == 4:
    vezes = int(input('Quantas parcelas? '))
    parc = (preco + (preco * 0.20))/vezes
    tot = (preco + (preco* 0.20))
    print('Sua compra será parcelada em {} vezes de R$ {} com juros, totalizando R$ {}.'.format(vezes, parc, tot))
else:
    print('Opção inválida, digite novamente')

