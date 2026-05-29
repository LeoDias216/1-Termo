import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep    
# 1 - Criar a janela principal
janela = tk.Tk()
janela.title("Jogo")
janela.geometry("1000x700")

# Carrega a imagem
imagem_original = Image.open(r"1-Termo/Python/Projetos/Imagens/Fundo pixelado.png")
# 2. Redimensiona a imagem para o tamanho exato da sua janela (400x200)
imagem_redimensionada = imagem_original.resize((1000, 700))
# 3. Converte a imagem para um formato que o Tkinter entende
imagem_fundo = ImageTk.PhotoImage(imagem_redimensionada)

# 4. Cria um Label para exibir a imagem e define as bordas como zero
label_fundo = tk.Label(janela, image=imagem_fundo, bd=0)
# 5. Posiciona o Label para preencher todo o espaço da janela
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
   

def personagemparado():
        imagem_personagem = Image.open(r"1-Termo/Python/Projetos/Imagens/personagemparado.png")
        imagem_personagem_redimensionada = imagem_personagem.resize((200, 300))
        personagem = ImageTk.PhotoImage(imagem_personagem_redimensionada)     
        label_personagem = tk.Label(janela, image=personagem, bd=0)
        label_personagem.place(x=100, y=300)
        label_personagem.image = personagem
        return label_personagem

def batendo():
        imagem_personagembat = Image.open(r"1-Termo/Python/Projetos/Imagens/personagembatendo.png")
        imagem_personagembat_redimensionada = imagem_personagembat.resize((300, 300))
        personagembat = ImageTk.PhotoImage(imagem_personagembat_redimensionada)     
        label_personagembat = tk.Label(janela, image=personagembat, bd=0)
        label_personagembat.place(x=500, y=300)
        label_personagembat.image = personagembat
        return label_personagembat

def jogo():
    ref_parado = personagemparado()
    
    def ataque():
        btn_ataque.config(state="disabled")
        btn_defesa.config(state="disabled")
        ref_parado.destroy()
        lbl_batendo = batendo()
        janela.after(2000, lambda: finalizar_ataque(lbl_batendo))
    def finalizar_ataque(lbl_batendo):
        # 4. Destrói o personagem batendo
        lbl_batendo.destroy()

        # 5. Recria o personagem parado e atualiza a referência na lista
        ref_parado[0] = personagemparado()
        
        # Reativa os botões
        btn_ataque.config(state="normal")
        btn_defesa.config(state="normal")
                 

    btn_ataque=tk.Button(janela, text="╔═════════════╗\n║ㅤ      ㅤ1.ㅤAtacarㅤ      ㅤ║\n╚═════════════╝", font=("Minecraft", 14),  
    bg="#FFFFFF", fg="black", command=ataque)
    btn_ataque.place(x=200, y=620)
    

    def defesa():
         messagebox.showinfo("Defesa", "Você defendeu!")
        
    btn_defesa=tk.Button(janela, text="╔═════════════╗\n║ㅤ     ㅤ2.ㅤDefenderㅤ  ㅤ║\n╚═════════════╝", font=("Minecraft", 14),  
    bg="#FFFFFF", fg="black", command=defesa)
    btn_defesa.place(x=600, y=620)
   
    janela.mainloop()

while True:
    jogo()

    