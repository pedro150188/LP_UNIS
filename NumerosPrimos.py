#Nesse codigo vamos apresentar os numeros primos e nao primos no range de 1 a 100
#apresentando a variavel numero
numero = 1

#adicionando o comando de repeticao
while numero <= 100:
    #criando a variavel contador para limitar a quantidade de teste de 1 a 100
    contador = 1
    x = 0
    while contador <= numero:
        if numero % contador == 0:
            x = x + 1
        contador = contador + 1

    #Informando ao codigo a condicao
    if x == 2:
#Imprimindo os numeros primos dentro da condicao de repeticao criada
        print ("Entre os numero de 1 a 100 o", numero, "e primo")
    numero = numero + 1
print("=" * 100)

#criando a mesma condicao anterior porem para numeros nao primos
number1 = 1
while number1 <=100:
    cont = 1
    y = 0
    while cont <= number1:
        if number1 % cont == 0:
            y = y + 1
        cont = cont + 1
    if y != 2:
        print ("Entre os numero de 1 a 100 o", number1, "nao e primo")
    number1 = number1 + 1