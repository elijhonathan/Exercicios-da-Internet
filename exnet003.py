'''
Escreva um programa que leia um numero inteiro maior que zero e devolva na tela
a soma de todos os seus algarismos. Por exemplo o numero 251 que corespondera
ao valor  8 ( 2 + 5 + 1). Se o numero lido nao for maior que zero, o programa terminara
com a mensagem "Numero invalido".
'''
total=0
num=int(input('Digite um numero inteiro maior que zero: '))
if num < 0:
    print('Número inválido, Tente novamente!')
else:
    while(num > 0):
        total += num % 10
        num = int(num / 10)
    print(total)
