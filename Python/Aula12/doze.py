# Exercício:
# Crie uma aplicação que pergunte o nome e o ano de nascimento do usuário, com calculo de idade

import tkinter as tk
from tkinter import messagebox

def cadastrar_usuario():
    nome_usuario = ent_nome_usuario.get()
    idade_usuario = ent_ano_usuario.get()


janela = tk.Tk()
janela.title("Identificação de usuário")
janela.geometry("500x500")
janela.configure(bg="maroon")

lbl_titulo_credenciais = tk.Label(janela, text=("Digite suas informações:"), font=("Arial", 14), fg="yellow", bg="maroon")
lbl_titulo_credenciais.grid(row=0, column=0, pady=20, padx=20)

lbl_titulo_nome = tk.Label(janela, text=("Seu nome:"), font=("Arial", 12), fg="yellow", bg="maroon")
lbl_titulo_nome.grid(row=1, column=0, pady=20, padx=20)

lbl_titulo_idade = tk.Label(janela, text=("Seu ano de nascimento:"), font=("Arial", 12), fg="yellow", bg="maroon")
lbl_titulo_idade.grid(row=2, column=0, pady=20, padx=20)

ent_nome_usuario = tk.Entry(janela, font=("Arial", 12), fg="black", bg="snow")
ent_nome_usuario.grid(row=1, column=1, pady=10, padx=10)

ent_ano_usuario = tk.Entry(janela, font=("Arial", 12), fg="black", bg="snow")
ent_ano_usuario.grid(row=2, column=1, pady=10, padx=10)

bnt_cadastrar_usuario = tk.Button(janela, text=("Cadastrar usuário"), width=30, command=cadastrar_usuario)
bnt_cadastrar_usuario.grid(row=3, column=0, pady=10, padx=10)

bnt_fechar = tk.Button(janela, text=("Fechar"), width=30, command=janela.destroy)
bnt_fechar.grid(row=3, column=1, pady=10, padx=10)


janela.mainloop()