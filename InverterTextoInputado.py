#Nesse codigo iremos inverter um texto inputado
#solicitando o texto a ser convertido
print ("Digite seu texto")
txt = input( )

#Adicionando uma funcao para converter texto sempre que necessario no codigo
def inverter(texto):
    return texto[::-1]
print(inverter(texto=txt))