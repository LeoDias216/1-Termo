import tkinter as tk
from tkinter import messagebox

# 1. Configurar evento

def solicitar_informacoes():
    # .get() serve para buscar o texto que foi digitado
    nome_usuario = campo_nome.get()
    idade_usuario = campo_idade.get()

    if nome_usuario == "":
        messagebox.showwarning("Aviso", "Por favor, digite seu nome :)")
    elif idade_usuario == "":
        messagebox.showwarning("Aviso", "Por favor, digite sua idade :)")
    else:
        messagebox.showinfo("Saudações, querido aluno", f"Olá, {nome_usuario}, {idade_usuario} anos. Seja bem-vindo ao mundo das interfaces gráficas.")

# 2. Configuração de janela

app = tk.Tk()
app.title("Tela de Usuário")
app.geometry("300x300")

# 3. Componentes
lbl_nom_usuario = tk.Label(app, text="Digite seu nome :) ").grid(row=0, column=0, padx=10, pady=10) # grid - posicionamento em grade

lbl_idd_usuario = tk.Label(app, text="Digite sua idade :)")
lbl_idd_usuario.grid(row=1, column=0, padx=10, pady=10)
# lbl_idd_usuario.pack(pady=10)

campo_nome = tk.Entry(app, font=("Arial", 12))
campo_nome.grid(row=2, column=0, padx=10, pady=5)
# campo_nome.pack(pady=5)

campo_idade = tk.Entry(app, font=("Arial", 12))
campo_idade.grid(row=3, column=0, padx=10, pady=5)
# campo_idade.pack(pady=5)

btn_cadastrar = tk.Button(app, text="Cadastrar", command=solicitar_informacoes)
btn_cadastrar.grid(row=4, column=0, pady=15)
# btn_cadastrar.pack(pady=15)

btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
btn_fechar.grid(row=5, column=0, pady=15)
# btn_fechar.pack(pady=5)

# 4, Rodar interface
app.mainloop()