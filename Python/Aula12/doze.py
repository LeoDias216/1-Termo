# Revisão Tkinter


# Biblioteca:
import tkinter as tk
from tkinter import messagebox, ttk

# DEF - Linha de blocos de Função
def cadastrar_usuario():
    # .get em todos os componentes que irão receber informação
    nome_usuario = ent_nome_usuario.get()
    nome_escola = cmb_nome_escola.get()

    if nome_usuario == "" or nome_escola == "":
        messagebox.showwarning("Verificar Dados", "Verificar os campos")
    else:
        messagebox.showinfo("Bem-vindo", f"Olá usuário {nome_usuario}")

# 0 Etapa - Janela

janela = tk.Tk()
janela.title("Revisão do Tkinter")
janela.geometry("500x500") # Largura x Altura
janela.configure(bg="crimson")

# Cores Metálicas e Brilhantes (Como Gold e Silver): 
# gold (Ouro)
# silver (Prata)
# bronze (Não existe como nome direto, use chocolate ou peru)
# platinum (Não existe direto, use lightgray ou gainsboro)

# Cores Básicas e Fortes:
# red (Vermelho)
# blue (Azul)
# green (Verde)
# yellow (Amarelo)
# orange (Laranja)
# purple (Roxo)

# Tons Pasteis e Variados:
# crimson (Vermelho escuro/forte)
# cyan ou aqua (Ciano/Azul piscina)
# magenta ou fuchsia (Rosa choque)
# navy (Azul marinho)
# lime (Verde limão)
# coral: É um tom de laranja-avermelhado claro e brilhante
# lightcoral: Uma variação oficial que é um pouco mais clara e rosada
# maroon: Castanho/Bordo (um vermelho bem escuro)
# tomato: Tomate (um vermelho alaranjado vibrante)
# salmon: Salmão (rosa alaranjado)
# firebrick: Tijolo de fogo (um vermelho escuro fechado)
# sienna: Terra de siena (um marrom avermelhado que lembra terracota)
# snow: Neve
# olive: Oliva, verde
# ivory: Marfim
# seashell: Branco perolado

# 1 Etapa - Componentes

lbl_titulo_aplicacao = tk.Label(janela, text="Revisão Tkinter :)", font=("Arial", 14), fg="black", bg="white")
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_nome_usuario = tk.Label(janela, text="Insira seu nome:", font=("Arial", 14), fg="red", bg="white")
lbl_nome_usuario.grid(row=1, column=0, pady=20, padx=20)

lbl_nome_escola = tk.Label(janela, text="Escolha sua escola:", font=("Arial", 12))
lbl_nome_escola.grid(row=2, column=0, pady=10, padx=10)

# Entrys = Caixa de texto ou antigo input
ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), fg="black", bg="white", width=20)
ent_nome_usuario.grid(row=1, column=1, pady=10, padx=10)

# Caixa de seleção ou combobox
# width = largura
# height = altura

cmb_nome_escola = ttk.Combobox(janela, values=["SESI5", "SESI408"], width=20) # height=20
cmb_nome_escola.grid(row=2, column=1, pady=10, padx=10)

# Botões
btn_enviar_dados = tk.Button(janela, text="Cadastrar usuário", width=30, command=cadastrar_usuario) # height=30
btn_enviar_dados.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_aplicacao = tk.Button(janela, text="Fechar aplicação", width=30, command=janela.destroy)
btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# 4 Etapa - Mainloop
janela.mainloop()