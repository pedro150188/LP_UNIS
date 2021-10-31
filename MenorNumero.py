#Vamos montar um codigo solicitando 3 numeros de entrada e apresentar apenas o menor deles
#solicitando os numeros

numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero: '))
numero3 = int(input('Terceiro numero: '))

#Aplicando a logica matematica
menornumero = numero1
if (numero2 < menornumero):
    menornumero = numero2
if (numero3 < menornumero):
    menornumero = numero3

#Apresentando o menor numero encontrado na logica
print ('->' * 20)
print 'O menor numero e =', menornumero
print ('<-' * 20)