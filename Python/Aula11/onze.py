# Tkinter

# Componentes principais:
# tk : a janela
# Label: Texto em rótulo
# Button: Um botão de clique
# Entry: Um campo de entrada de texto

# Biblioteca
import tkinter as tk
from tkinter import messagebox

# 1. Criar janela principal
janela = tk.Tk()
janela.configure(bg="#FF0000")
janela.title("Minha Primeira Janela em GUI")
janela.geometry("400x200") #Largura x Altura

# 2. Criar a função que o botão vai executar (evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão! :)")

# 3. Criar os componentes
lbl_titulo = tk.Label(janela, text="Bem-vindo à aula de Tkinter!", font=("Arial", 14, "bold"), bg="#001AFF")
btn_clique = tk.Button(janela, text="Clique aqui :) ", font=("Arial", 14,), bg="#000000", fg="white", command=mostrar_mensagem)

# 4. Posicionar os componentes
lbl_titulo.pack(pady=20)
btn_clique.pack(padx=10)
# pady - posicionar vertical
# padx - posicionar horizontal

# 5. Rodar o loop da interface
janela.mainloop()