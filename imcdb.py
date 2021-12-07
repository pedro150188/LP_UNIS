#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exemplo Tkinter com SQLite"""
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


class ConectarDB:
    def __init__(self):
        self.conexao = sqlite3.connect('fdb.db')
        self.cursor = self.conexao.cursor()

    def buscar_marca(self):
        return self.cursor.execute('SELECT DISTINCT marca FROM veiculos').fetchall()

    def busca_modelo(self, marca):
        return self.cursor.execute(
            "SELECT DISTINCT modelo FROM veiculos WHERE marca=? COLLATE NOCASE", (marca,)).fetchall()

    def buscar_ano(self, modelo):
        return self.cursor.execute(
            "SELECT DISTINCT ano FROM veiculos WHERE modelo=? COLLATE NOCASE", (modelo,)).fetchall()

    def buscar_veiculos(self, marca, modelo, ano):
        return self.cursor.execute(
            "SELECT * FROM veiculos WHERE marca=? and modelo=? and ano=? COLLATE NOCASE",
            (marca, modelo, ano,)).fetchall()


class Janela(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # Coletando informações do monitor
        largura = round(self.winfo_screenwidth() / 2)
        altura = round(self.winfo_screenheight() / 2)
        tamanho = ('%sx%s' % (largura, altura))

        # Título da janela principal.
        self.master.title('Exemplo')
        # Tamanho da janela principal.
        self.master.geometry(tamanho)
        # Gerenciador de layout da janela principal.
        self.pack()

        # Criando uma instancia do banco de dados (Abrindo a conexão).
        self.banco = ConectarDB()

        # Inserindo widgets na janela principal.
        self.criar_widgets()

    def criar_widgets(self):
        # Combobox marcas.
        self.comboboxMarca = ttk.Combobox()
        # Preenchedo o combobox com os valores do banco.
        self.comboboxMarca['values'] = self.banco.buscar_marca()
        # Evento que é disparado quando algo é selecionado.
        self.comboboxMarca.bind('<<ComboboxSelected>>', self.pegar_modelo)
        self.comboboxMarca.pack()

        # Combobox modelo.
        self.comboboxModelo = ttk.Combobox()
        self.comboboxModelo.bind('<<ComboboxSelected>>', self.pegar_ano)
        self.comboboxModelo.pack()

        # Combobox ano.
        self.comboboxAno = ttk.Combobox()
        self.comboboxAno.bind('<<ComboboxSelected>>', self.resultado)
        self.comboboxAno.pack()

        # Listbox que irá exibir os resultados localizados.
        self.listbox = tk.Listbox()
        self.listbox.pack()

    def pegar_modelo(self, event):
        # Coletando o valor que foi selecionado no combobox marca.
        marca = self.comboboxMarca.get()

        # Buscando dados no banco e preenchendo o combobox modelo.
        self.comboboxModelo['values'] = self.banco.busca_modelo(marca=marca)

    def pegar_ano(self, event):
        # Coletando o valor que foi selecionado no combobox modelo.
        modelo = self.comboboxModelo.get()

        # Buscando dados no banco e preenchendo o combobox ano.
        self.comboboxAno['values'] = self.banco.buscar_ano(modelo=modelo)

    def resultado(self, event):
        # Coletando os valores de todos os combobox.
        marca = self.comboboxMarca.get()
        modelo = self.comboboxModelo.get()
        ano = self.comboboxAno.get()

        # Limpando o listbox.
        self.listbox.delete(0, tk.END)

        # Buscando dados no banco e utilizando um
        # laço de repetição para preencher o listbox.
        for veiculo in self.banco.buscar_veiculos(marca=marca, modelo=modelo, ano=ano):
            self.listbox.insert(tk.END, veiculo)


root = tk.Tk()
app = Janela(master=root)
app.mainloop()