'''Escreva um programa em Python para resolver o seguinte problema de engenharia:
'Num canteiro de obras, o(a) engenheiro(a) responsável solicitou a produção de treliças para
a construção. O(a) engenheiro(a) tem o seguinte conhecimento:
-Quantidade de armação:
-Produtividade do operário:
-Quantidade de recurso humanos:
-Jornada diária:

Para o planejamento e gerenciamento da obra, o engenheiro quer saber a duração da atividade
a partir de um índice. Desenvolva um programa em Python para realizar esse cálculo. Sabe que
a duração da atividade é calculada dividindo-se a quantidade de armações pelo produto entre
a produtividade, os recurso humanos e a jornada diária.

indice= quantidade de armação / ( Produtividade * Recursos Humanos * Jornada diaria)

Se ocorrer de a duração do serviço ser a superior a 10 dias, informe ao usuário que é preciso aumentar a produção


Ao terminar o código, o execute, entrando com os seguintes dados:
Quantidade armação = 1440 Kg
Produtividade = 10 Kg por hora
Recursos humanos = 3 armadores
Jornada diária = 8 horas

A resposta esperada, obtida através do software, deverá ser:
'O índice calculado foi igual a 6, logo não é preciso aumentar a produção'
'''

quar = int(input('Digite a quantidade de armação em Kg: '))
prpoho = int(input('Digite a Produtivade em Kg por hora: '))
rehu = int(input('Digite a quantidade de pessoas disponíveis: '))
jodi = int(input('Digite a jornada diária em horas: '))
indice = quar / (prpoho * rehu * jodi)
if indice <= 10:
    print(f'O indice calculado foi igual a {indice:.0f}, logo não é preciso aumentar a produção!')
else:
    print(
        f'O indice calculado foi igual a {indice:.0f}, precisamos de 10 ou menos, aumente a produção para alcançar o desejado!')
