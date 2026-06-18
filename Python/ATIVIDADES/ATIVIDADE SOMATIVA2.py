import time
import tkinter as tk
from tkinter import messagebox, ttk

# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba: "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

def registrar_operador():
    nome_operador = ent_nome_operador.get()
    turno_operador = cmb_turno_operador.get()

    if nome_operador == "" or turno_operador == "":
        messagebox.showwarning("Alerta de informações:", "Preencha todos os campos")
    else:
        messagebox.showinfo("Bem-vindo", f"Operador {nome_operador} registrado no Turno {turno_operador}. Boa jornada!")


janela = tk.Tk()
janela.title("Registro de Operador")
janela.geometry("500x500")
janela.configure(bg="maroon")

lbl_titulo_aplicacao = tk.Label(janela, text="Insira seus dados:", font=("Arial", 14))
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_nome_operador = tk.Label(janela, text="Nome:", font=("Arial", 12))
lbl_nome_operador.grid(row=1, column=0, pady=20, padx=20)

lbl_turno_operador = tk.Label(janela, text="Turno:", font=("Arial", 12))
lbl_turno_operador.grid(row=2, column=0, pady=20, padx=20)

ent_nome_operador = tk.Entry(janela, font=("Arial", 12), width=20)
ent_nome_operador.grid(row=1, column=1, pady=10, padx=10)

cmb_turno_operador = ttk.Combobox(janela, values=["A", "B", "C"], width=20)
cmb_turno_operador.grid(row=2, column=1, pady=10, padx=10)

btn_registrar_cadastro = tk.Button(janela, text="Registrar", width=30, command=registrar_operador)
btn_registrar_cadastro.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_tela = tk.Button(janela, text="Fechar", width=30, command=janela.destroy)
btn_fechar_tela.grid(row=3, column=1, pady=10, padx=10)

janela.mainloop()

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e exiba quantas peças serão produzidas em um turno de 8 horas.

def enviar_pecas():
    quantidade_pecas = int(ent_quantidade_pecas.get())

    if quantidade_pecas == "":
        messagebox.showwarning("Aviso!:", "Insira a quantidade de peças")
    else:
        total_pecas = (quantidade_pecas * 8)
        messagebox.showinfo("Resultado:", f"Em um turno de 8 horas, são produzidas {total_pecas} peças")


janela = tk.Tk()
janela.title("Cálculo de peças")
janela.geometry("700x500")
janela.configure(bg="snow")

lbl_titulo_aplicacao = tk.Label(janela, text="Calculando peças por horas:", font=("Arial", 14))
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_quantidade_pecas = tk.Label(janela, text="Quantas peças são produzidas em 1 hora?", font=("Arial", 10))
lbl_quantidade_pecas.grid(row=1, column=0, pady=20, padx=20)

ent_quantidade_pecas = tk.Entry(janela, font=("Arial", 12), width=20)
ent_quantidade_pecas.grid(row=1, column=1, pady=10, padx=10)

btn_enviar_pecas = tk.Button(janela, text="Enviar", width=30, command=enviar_pecas)
btn_enviar_pecas.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_tela = tk.Button(janela, text="Fechar", width=30, command=janela.destroy)
btn_fechar_tela.grid(row=3, column=1, pady=10, padx=10)

janela.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar ≈ 14.5 PSI) e exiba com duas casas decimais.

def enviar_pressao():
    valor_pressao = int(ent_pressao.get())

    if valor_pressao == "":
        messagebox.showwarning("Aviso!:", "Insira a pressão")
    else:
        pressao_total = valor_pressao * 14.5
        messagebox.showinfo("Resultado:", f"A pressão Bar {valor_pressao} convertida para PSI ficou {pressao_total} PSI")

janela = tk.Tk()
janela.title("Conversor de pressão")
janela.geometry("700x500")
janela.configure(bg="ivory")

lbl_titulo_aplicacao = tk.Label(janela, text="Conversor de pressão: Bar para PSI", font=("Arial", 14))
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_pressao = tk.Label(janela, text="Qual a pressão, em Bar?", font=("Arial", 12))
lbl_pressao.grid(row=1, column=0, pady=20, padx=20)

ent_pressao = tk.Entry(janela, font=("Arial", 12), width=10)
ent_pressao.grid(row=1, column=1, pady=10, padx=10)

btn_enviar_pressao = tk.Button(janela, text="Converter", width=30, command=enviar_pressao)
btn_enviar_pressao.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_tela = tk.Button(janela, text="Fechar", width=30, command=janela.destroy)
btn_fechar_tela.grid(row=3, column=1, pady=10, padx=10)

janela.mainloop()

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média aritmética simples delas.

def enviar_notas():
    nota_inserida1 = float(ent_nota1.get())
    nota_inserida2 = float(ent_nota2.get())
    nota_inserida3 = float(ent_nota3.get())

    if nota_inserida1 == "" or nota_inserida2 == "" or nota_inserida3 == "":
        messagebox.showwarning("Aviso!:", "Insira todas as notas corretamente")
    else:
        total_notas = nota_inserida1 + nota_inserida2 + nota_inserida3
        media = total_notas / 3
        messagebox.showinfo("Média:", f"A média final das notas das peças foi de {media}")


janela = tk.Tk()
janela.title("Inspetor de peças")
janela.geometry("700x500")
janela.configure(bg="tomato")

lbl_titulo_aplicacao = tk.Label(janela, text="Insira 3 notas de peças para a média:", font=("Arial", 14))
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_notas_inseridas = tk.Label(janela, text="Notas:", font=("Arial", 12))
lbl_notas_inseridas.grid(row=1, column=0, pady=20, padx=20)

ent_nota1 = tk.Entry(janela, font=("Arial", 12), width=10)
ent_nota1.grid(row=1, column=1, pady=10, padx=10)

ent_nota2 = tk.Entry(janela, font=("Arial", 12), width=10)
ent_nota2.grid(row=2, column=1, pady=10, padx=10)

ent_nota3 = tk.Entry(janela, font=("Arial", 12), width=10)
ent_nota3.grid(row=3, column=1, pady=10, padx=10)

btn_enviar_notas = tk.Button(janela, text="Enviar", width=30, command=enviar_notas)
btn_enviar_notas.grid(row=4, column=0, pady=10, padx=10)

btn_fechar_tela = tk.Button(janela, text="Fechar", width=30, command=janela.destroy)
btn_fechar_tela.grid(row=4, column=1, pady=10, padx=10)

janela.mainloop()

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

def enviar_temperatura():
    temperatura_atual = int(ent_temperatura_motor.get())

    if temperatura_atual == "":
        messagebox.showwarning("Aviso!", "Insira a temperatura")
    else:
        if temperatura_atual < 40:
            messagebox.showinfo("Temperatura fraca", "Baixa carga")
        elif 40 <= temperatura_atual <= 70:
            messagebox.showinfo("Temperatura OK", "Carga normal")
        elif temperatura_atual > 70:
            messagebox.showwarning("Temperatura Alta!", "ALERTA: Resfriamento ativado!")
        

janela = tk.Tk()
janela.title("Termostato do motor")
janela.geometry("700x500")
janela.configure(bg="crimson")

lbl_titulo_aplicacao = tk.Label(janela, text="Verificação de temperatura:", font=("Arial", 14))
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_temperatura_motor = tk.Label(janela, text="Qual a atual temperatura do motor?", font=("Arial", 10))
lbl_temperatura_motor.grid(row=1, column=0, pady=20, padx=20)

ent_temperatura_motor = tk.Entry(janela, font=("Arial", 12), width=20)
ent_temperatura_motor.grid(row=1, column=1, pady=10, padx=10)

btn_enviar_temperatura = tk.Button(janela, text="Checar", width=30, command=enviar_temperatura)
btn_enviar_temperatura.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_tela = tk.Button(janela, text="Fechar", width=30, command=janela.destroy)
btn_fechar_tela.grid(row=3, column=1, pady=10, padx=10)

janela.mainloop()

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

def enviar_letra_lote():
    letra_lote = ent_letra_lote.get()

    if letra_lote == "":
        messagebox.showwarning("Aviso!", "Insira uma letra válida de lote")
    else:
        if letra_lote == "A":
            messagebox.showinfo("Lote A", "Lote de Alimentos")
        elif letra_lote == "E":
            messagebox.showinfo("Lote E", "Lote de Eletrônicos")
        else:
            messagebox.showinfo("Lote Desconhecido", "Favor, revisar o produto")

janela = tk.Tk()
janela.title("Classificador de Lotes")
janela.geometry("500x500")
janela.configure(bg="coral")

lbl_titulo_aplicacao = tk.Label(janela, text="Verificação de Lotes:", font=("Arial", 14))
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_letra_lote = tk.Label(janela, text="Insira a primeira letra do seu Lote:", font=("Arial", 10))
lbl_letra_lote.grid(row=1, column=0, pady=20, padx=20)

ent_letra_lote = tk.Entry(janela, font=("Arial", 12), width=20)
ent_letra_lote.grid(row=1, column=1, pady=10, padx=10)

btn_enviar_lote = tk.Button(janela, text="Verificar", width=30, command=enviar_letra_lote)
btn_enviar_lote.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_tela = tk.Button(janela, text="Fechar", width=30, command=janela.destroy)
btn_fechar_tela.grid(row=3, column=1, pady=10, padx=10)

janela.mainloop()

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

def requisitos_segurança():
    sensor_porta = cmb_sensor_porta.get()
    botao_emergencia = cmb_botao_emergencia.get()

    if sensor_porta == "" or botao_emergencia == "":
        messagebox.showwarning("Aviso!", "Insira os requisitos")
    else:
        if sensor_porta == "Fechada" and botao_emergencia == "Desligado":
            messagebox.showinfo("Máquina ligada", "Requisitos corretos")
        else:
            messagebox.showwarning("Atenção!", "Requisitos em falta, verifique a máquina")

janela = tk.Tk()
janela.title("Segurança de Máquina")
janela.geometry("700x500")
janela.configure(bg="navy")

lbl_titulo_aplicacao = tk.Label(janela, text="Insira os dados atuais da operação:", font=("Arial", 14))
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_sensor_porta = tk.Label(janela, text="Qual o estado da porta?", font=("Arial", 12))
lbl_sensor_porta.grid(row=1, column=0, pady=20, padx=20)

lbl_botao_emergencia = tk.Label(janela, text="Qual o estado do botão de emergência?", font=("Arial", 12))
lbl_botao_emergencia.grid(row=2, column=0, pady=20, padx=20)

cmb_sensor_porta = ttk.Combobox(janela, values=["Aberta", "Fechada"], width=20)
cmb_sensor_porta.grid(row=1, column=1, pady=10, padx=10)

cmb_botao_emergencia = ttk.Combobox(janela, values=["Ligado", "Desligado"], width=20)
cmb_botao_emergencia.grid(row=2, column=1, pady=10, padx=10)

btn_registrar_cadastro = tk.Button(janela, text="Registrar", width=30, command=requisitos_segurança)
btn_registrar_cadastro.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_tela = tk.Button(janela, text="Fechar", width=30, command=janela.destroy)
btn_fechar_tela.grid(row=3, column=1, pady=10, padx=10)

janela.mainloop()

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

def eficiencia_pecas():
    pecas_produzidas = float(ent_pecas_produzidas.get())
    pecas_defeituosas = float(ent_pecas_defeituosas.get())

    if pecas_produzidas == "" or pecas_defeituosas == "":
        messagebox.showwarning("Aviso!", "Insira a quantidade de peças corretamente")
    else:
        total_pecas = pecas_produzidas + pecas_defeituosas
        um_por_cento = pecas_defeituosas / 100
        cinco_por_cento = um_por_cento * 5
        if cinco_por_cento < pecas_defeituosas:
            messagebox.showwarning("Aviso!", "Revisar Processo")
        elif cinco_por_cento > pecas_defeituosas:
            messagebox.showinfo("Tudo certo", "Processo Otimizado")

janela = tk.Tk()
janela.title("Cálculo de Descarte")
janela.geometry("700x500")
janela.configure(bg="firebrick")

lbl_titulo_aplicacao = tk.Label(janela, text="Calculando eficiência das peças produzidas:", font=("Arial", 14))
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_pecas_produzidas = tk.Label(janela, text="Total de peças produzidas hoje:", font=("Arial", 12))
lbl_pecas_produzidas.grid(row=1, column=0, pady=20, padx=20)

lbl_pecas_defeituosas = tk.Label(janela, text="Total de peças defeituosas hoje:", font=("Arial", 12))
lbl_pecas_defeituosas.grid(row=2, column=0, pady=20, padx=20)

ent_pecas_produzidas = tk.Entry(janela, font=("Arial", 12), width=20)
ent_pecas_produzidas.grid(row=1, column=1, pady=10, padx=10)

ent_pecas_defeituosas = tk.Entry(janela, font=("Arial", 12), width=20)
ent_pecas_defeituosas.grid(row=1, column=1, pady=10, padx=10)

btn_verificar_pecas = tk.Button(janela, text="Registrar", width=30, command=eficiencia_pecas)
btn_verificar_pecas.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_tela = tk.Button(janela, text="Fechar", width=30, command=janela.destroy)
btn_fechar_tela.grid(row=3, column=1, pady=10, padx=10)

janela.mainloop()

# Faltou 9 e 10 :(