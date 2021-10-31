#Leitura da idade em dias
idade = int(input())

#calculo de anos
anos = int(idade / 365)
saldo = idade - (anos * 365)

#calculo dos meses
meses = int(saldo / 30)

#calculo dos dias
dias = saldo - (meses *30)

#Apresentando resultado
print anos, 'ano(s)'
print meses, 'mes(es)'
print dias, 'dia(s)'