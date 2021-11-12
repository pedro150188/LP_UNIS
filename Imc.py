#importando bibliotecas

from tkinter import *
from tkinter import ttk

#Definindo Cores
co0 ='#ffffff' #branco
co1 ='#444466' #preto
co2 ='#4065a1' #azul

#Criando a Janela
janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co0)

#Dividindo a Janela em duas partes (cima e baixa)
frame_cima= Frame(janela, width=295, height=50,bg=co0, padx=0, pady=0, relief='flat')
frame_cima.grid(row=0, column=0,sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180,bg=co0, padx=0, pady=0, relief='flat')
frame_baixo.grid(row=1, column=0,sticky=NSEW)

#Adicionado o título da janela
app_nome = Label(frame_cima, text='CALCULADORA DE IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivi 16 bold'), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

#Criando linha para separar as informações
app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat',anchor='center', font=('Ivi 1 '), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

# Definindo Funções

def calcular():

    massa = float(e_peso.get())
    altura = float(e_altura.get())

    imc = massa / altura**2

    resultado = imc

#Aplicando as condições

    if resultado < 16.99:
        l_resultado_texto['text'] = 'Você está muito abaixo do Peso!'
    elif resultado >= 17 and resultado < 18.49:
        l_resultado_texto['text'] = 'Você está abaixo do Peso!'
    elif resultado >= 18.50 and resultado < 24.99:
        l_resultado_texto['text'] = 'Você está no Peso Normal!'
    elif resultado >= 25 and resultado < 29.99:
        l_resultado_texto['text'] = 'Você está acima do Peso!'
    elif resultado >= 30 and resultado < 34.99:
        l_resultado_texto['text'] = 'Você está OBESO do tipo I!'
    elif resultado >= 35 and resultado < 39.99:
        l_resultado_texto['text'] = 'Você está OBESO do tipo II (PREOCUPANTE)!'
    else:
        l_resultado_texto['text'] = 'Você está OBESO do tipo III (MÓRBIDA)!'

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)
    

#Criando a Frame do Peso e o campo de entrada
l_peso = Label(frame_baixo, text='Insira seu Peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivi 10 bold'), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivi 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

#Criando a Frame da Altura e o campo de entrada
l_altura = Label(frame_baixo, text='Insira sua Altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivi 10 bold'), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivi 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

#Criando a Frame do Resultado
l_resultado = Label(frame_baixo, text='___', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivi 24 bold'), bg=co2, fg=co0)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(frame_baixo, text='', width=37, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ivi 10 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=90)

#Criando o botão de calculo
b_calcular = Button(frame_baixo,command=calcular, text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivi 10 bold'), bg=co2, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

janela.mainloop()