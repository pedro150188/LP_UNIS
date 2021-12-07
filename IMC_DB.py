# -*- coding: utf-8 -*-import sys
import sqlite3
import tkinter
from tkinter import *
import tkinter.messagebox
#import tkMessageBox
from tkinter import messagebox, Tk
from sqlite3 import *

conn = connect('IMCS.db')
c = conn.cursor()


#Definindo Cores
co0 ='#ffffff' #branco
co1 ='#444466' #preto
co2 ='#4065a1' #azul

#Criando a Janela
janela = Tk()
janela.title('')
janela.geometry('400x320')
janela.configure(bg=co0)

#Dividindo a Janela em tres partes (cima, central e baixa)
frame_cima= Frame(janela, width=295, height=50,bg=co0, padx=0, pady=0, relief='flat')
frame_cima.grid(row=0, column=0,sticky=NSEW)

frame_central= Frame(janela, width=295, height=180, bg=co0, padx=0, pady=0, relief='flat')
frame_central.grid(row=1, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=310,bg=co0, padx=0, pady=0, relief='flat')
frame_baixo.grid(row=2, column=0,sticky=NSEW)

#Adicionado o título da janela
app_nome = Label(frame_cima, text='CALCULADORA DE IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivi 16 bold'), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

#Criando linha para separar as informações
app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat',anchor='center', font=('Ivi 1 '), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

# Definindo Funções

def imc():

    massa = float(e_peso.get())
    altura = float(e_altura.get())

    imc = massa / altura**2

    #resultado = imc

#Aplicando as condições

    if imc < 16.99:
        messagebox.showinfo('Resultado', 'Muito abaixo do Peso!')
    elif imc >= 17 and imc < 18.49:
        messagebox.showinfo('Resultado', 'Abaixo do Peso!')
    elif imc >= 18.50 and imc < 24.99:
        messagebox.showinfo('Resultado', 'No Peso Normal!')
    elif imc >= 25 and imc < 29.99:
        messagebox.showinfo('Resultado', 'Acima do Peso!')
    elif imc >= 30 and imc < 34.99:
        messagebox.showinfo('Resultado', 'OBESO do tipo I!')
    elif imc >= 35 and imc < 39.99:
        messagebox.showinfo('Resultado', 'OBESO do tipo II (PREOCUPANTE)!')
    else:
        messagebox.showinfo('Resultado', 'OBESO do tipo III (MÓRBIDA)!')

    l_resultado['text'] = "{:.{}f}".format(imc, 2)
    
peso = int()
altura = float()
nome = str()
endereco = str()

#Criando a Frame do Peso e o campo de entrada
l_peso = Label(frame_baixo, text='Insira seu Peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivi 10 bold'), bg=co0, fg=co1)
l_peso.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivi 10 bold'), justify='center', textvariable=peso)
e_peso.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

#Criando a Frame da Altura e o campo de entrada
l_altura = Label(frame_baixo, text='Insira sua Altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivi 10 bold'), bg=co0, fg=co1)
l_altura.grid(row=2, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivi 10 bold'), justify='center', textvariable=altura)
e_altura.grid(row=2, column=1, sticky=NSEW, pady=10, padx=3)

#Criando a Frame do Resultado
l_resultado = Label(frame_baixo, text='___', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivi 24 bold'), bg=co2, fg=co0)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(frame_baixo, text='', width=37, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ivi 10 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=90)

#Criando a Frame do nome e o campo de entrada
l_nome = Label(frame_central, text='Insira seu nome', height=1, padx=0, relief='flat', anchor='center', font=('Ivi 10 bold'), bg=co0, fg=co1)
l_nome.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_nome = Entry(frame_central, width=35, relief='solid', font=('Ivi 10 bold'), justify='center', textvariable=nome)
e_nome.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

#Criando a Frame do Endereco e o campo de entrada
l_endereco = Label(frame_central, text='Insira seu Endereco', height=1, padx=0, relief='flat', anchor='center', font=('Ivi 10 bold'), bg=co0, fg=co1)
l_endereco.grid(row=2, column=0, sticky=NSEW, pady=10, padx=3)
e_endereco = Entry(frame_central, width=35, relief='solid', font=('Ivi 10 bold'), justify='center', textvariable=endereco)
e_endereco.grid(row=2, column=1, sticky=NSEW, pady=10, padx=3)

#Criando o botão de calculo
b_calcular = Button(frame_baixo,command=imc, text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivi 10 bold'), bg=co2, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

#Declarando o banco de dados
def cadastro():
    sql = '''CREATE TABLE IF NOT EXISTS IMCS
    (   peso FLOAT,
    altura FLOAT,
    nome VARCHAR(100),
    endereco VARCHAR(100),
    IMC FLOAT)'''
    c.execute(sql)
    c.execute('INSERT INTO IMCS (peso, altura, nome, endereco, IMC) VALUES ("' + e_peso.get() + '", "' + e_altura.get() + '",\
        "' + e_nome.get() + '","' + e_endereco.get() + '","' + messagebox.showinfo.get()+'")')
    
conn.commit()

janela.mainloop()