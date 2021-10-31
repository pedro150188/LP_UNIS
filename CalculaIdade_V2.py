#Calculo de dias conforme idade
#impotanto a biblioteca de data datetime
import datetime
#solicitando o dia do nascimento
print("Informe o dia de nascimento")
dia = int(input())

#solicitando o mes do nascimento
print("Informe o mes de nascimento")
mes = int(input())

#Solicitando o ano de nascimento
print("informe o ano de nascimento")
ano = int(input())

#Calculando a diferenca dos anos meses e dias dentro da biblioteca datetime
data1 = datetime.datetime(ano, mes, dia)
data2 = datetime.datetime.now()
diff = data2 - data1

days = diff.days
years, days = days // 365, days %365
months, days = days // 30, days % 30

#apresentando o ano inputado anteriormente e o resultado da diferenca
print("Desde {} se passaram {} anos, {} meses, {} dias".format(data1, years, months, days))
totaldias = (years * 365) + (months * 30) + (days)

#apresentando o calculo de dias
print "Total em dias e =" ,totaldias