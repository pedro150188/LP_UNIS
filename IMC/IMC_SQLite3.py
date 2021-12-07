# -*- coding: utf-8 -*-import sys
import tkinter
from tkinter import *
import tkinter.messagebox
#import tkMessageBox
from tkinter import messagebox, Tk
from sqlite3 import *

conn = connect('IMCBD.db')
c = conn.cursor()


def imc():
    num1 = int(entrada_peso.get())
    num2 = float(entrada_altura.get()) / 100
    imc = (num1 / (num2 * num2))


    if imc == 0 or imc < 18:
        messagebox.showinfo("Resultado", "Você está muito abaixo do peso!")
    elif imc == 18 or imc < 25:
        messagebox.showinfo("Resultado", "Você está com peso normal!")
    elif imc == 25 or imc < 27:
        messagebox.showinfo("Resultado", "Você está acima do peso!")
    elif imc == 27 or imc < 30:
        messagebox.showinfo("Resultado", "Você está com obesidade I!")
    elif imc == 30 or imc < 40:
        messagebox.showinfo("Resultado", "Você está com obesidade II!")
    else:
        messagebox.showinfo("Resultado", "Você está com obesidade III(Móbida)!")


janela = tkinter.Tk()
janela.title("Calculo do IMC - índice de massa corporal")
janela.geometry("600x300")
janela.config(bg="yellow")

vp = Frame(janela)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.rowconfigure(0, weight=1)

nome = str()
email = str()
peso = int()
altura = float()

ins_nome = Label(janela, text='Nome: ', bg='green', fg='White')
ins_nome.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky=N)

tag_nome = Entry(janela, textvariable=nome)
tag_nome.grid(row=2, column=2, padx=(10, 10), pady=(10, 10), sticky=N)

ins_mail = Label(janela, text='E-mail: ', bg='green', fg='White')
ins_mail.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky=W)

tag_mail = Entry(janela, textvariable=email)
tag_mail.grid(row=3, column=2, padx=(10, 10), pady=(10, 10), sticky=N)

tag_peso = Label(janela, text='Peso: ', bg='green', fg='White')
tag_peso.grid(row=4, column=1, padx=(10, 10), pady=(10, 10), sticky=E)

entrada_peso = Entry(janela, textvariable=peso)
entrada_peso.grid(row=4, column=2, padx=(10, 10), pady=(10, 10), sticky=E)

tag_altura = Label(janela, text='Altura: ', bg='green', fg="White")
tag_altura.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky=E)

entrada_altura = Entry(janela, textvariable=altura)
entrada_altura.grid(row=5, column=2, padx=(10, 10), pady=(10, 10), sticky=E)

bconv = Button(janela, bg='green', fg='White', text='Calcular IMC', width=10, height=1, command=imc)
bconv.grid(row=6, column=2, padx=(10, 10), pady=(10, 10))


def cadastro():
    sql = '''CREATE TABLE IF NOT EXISTS IMC
    (   Nome VARCHAR(100),
        Email VARCHAR(100),
        Peso VARCHAR(100),
        Altura FLOAT,
        IMC FLOAT)'''
    c.execute(sql)
    c.execute('INSERT INTO IMC (Nome, Email, Peso, Altura, IMC) VALUES ("' + tag_nome.get() + '",\
        "' + tag_mail.get() + '","' + entrada_peso.get() + '","' + entrada_altura.get() + '","' + messagebox.showinfo.get()+'")')
    conn.commit()

janela.mainloop()