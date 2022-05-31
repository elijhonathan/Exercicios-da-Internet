'''Leia um valor inteiro 'n', Este valor será a quantidade de valores inteiros 'n2' que serão lidos em seguida.
Mostre quantos destes valores 'n2' estão dentro do intervalo [10, 20] e quantos estão fora do intervalo, conforme o exemplo:

exemplo:
quantos numeros voce vai digitar: 5
Digite um numero: 14
Digite um numero: 35
Digite um numero: 10
Digite um numero: 131
Digite um numero: 8
2 dentro
3 fora
'''

dentro= fora = cont = 0
n=''

n=int(input('Quantos números quer digitar: '))
while n != cont:
  n2=int(input('Digite um número: '))
  cont +=1
  if n2 <= 20 and n2 >= 10:
    dentro +=1
  else:
    fora +=1
print(f'Você digitou {dentro} dentro e {fora} fora!')
