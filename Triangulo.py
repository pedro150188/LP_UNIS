#Cada seguimento tem que ser menor que a soma do comprimento dos outros dois complementos
#Criando cabecalho da atividade
print('-='*20)
print('Analisando triangulo')
print('-='*20)

#lendo os seguimentos do triangulo(todo triangulo e composto de 3 retas)
#solicitando valor da reta 1
reta1 = float(input('Primeira reta: '))

#solicitando valor da reta 2
reta2 = float(input('Segunda reta: '))

#Solicitando valor da reta3
reta3 = float(input('Terceira reta: '))

#Aplicando principios matematicos
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os valores das retas acima FORMAM um triangulo")
else:
    print("Os valores das retas acima NAO FORMAM um triangulo")