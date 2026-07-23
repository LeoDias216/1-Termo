# 1. O Laço 'for' (Repetições determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças)
# Exemplo: Relatório de produção diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
for lote in range(1, 6):
    print(f"Processando lote número {lote}...")
    print("Qualidade verificada. [OK]")
    print("Produção do dia finalizada!")

# Imagine que você queira atingir uma meta de produção de 5 carros e numera-los
for carro in range(1, 6):
    print(f"Produção diária de carros {carro}...")

# Exemplo 2
# Contar até 4
for i in range(5):
    print(i)

# Exemplo 3
peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
tipospecas = ["Barra dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo cabeça chata"]

for item in peças:
    print(f"Item em estoque: {item}")
    for tipos in tipospecas:
        print(f"Minha lista de tipos de peças {tipospecas}")

# Exemplo 4
# Imagine a seguinte situação: Gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos

print("Bem vindo a loja de peças Magnum Tools, escolha uma das opções:")
print("1 - Peças")
print("2 - Tipos de peças")

opcao = int(input("Digite sua opção de pesquisa: "))
peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
tipospecas = ["Barra dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo cabeça chata"]

if opcao == 1:
    for item in peças:
        print(f"Item em estoque: {item}")
        print("Fim da lista")
elif opcao == 2:
    for item in peças:
        print(f"Item em estoque: {tipospecas}")
        print("Fim da lista")
else:
    print("Encerrando sistema")

# Exercício 1: Contador de produção (for)
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com sucesso". No final, exiba "Ciclo de produção concluído".

for peça in range(1, 11):
    print(f"Peça nº {peça} processada com sucesso...")
print("Ciclo de produção concluído")

# Exercício 2:
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxis.

print("Bem vindo a feira Magnum Natural")

for banana in range(1, 11):
    print(f"banana nº {banana} encontrada")

for manga in range(1, 6):
    print(f"manga nº {manga} encontrada")

for melancia in range(1, 11):
    print(f"melancia nº {melancia} encontrada")

for abacaxi in range(1, 14):
    print(f"abacaxi nº {abacaxi} encontrada")

# Exercício 3
# Montar uma tabuada: Inicialmente pode ser usado por um valor fixo e depois usar a pergunta

print("Bem vindo ao calculador de tabuadas Magnum Numbers")
print("Começando pela tabuada do 1:")

for numero in range(1, 11):
    print(f"1 * {numero} =",(1 * numero))

numero = int(input("Bem vindo a calculadora de tabuadas Magnum Gold, digite seu número "))

print(f"Tabuada do {numero}:")
for tabuada in range(1, 11):
    resultado = numero * tabuada
    print(f"{numero} x {tabuada} = {resultado}")

# 2. O Laço while (Repetições indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop infinito controlado)

# Repete enquanto a temperatura estiver segura
# Início

import time
temperatura = 25
while temperatura < 40:
    print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
    time.sleep(2)
    temperatura += 3 # Simulando o aquecimento da máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo: Menu de interação
# != diferente
# lower = minúsculo
# upper = maiúsculo
opcao = ""

while opcao != "sair" and "SAIR":
    opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").lower()
    if opcao != "sair" and "SAIR":
        print(f"Dado '{opcao}' registrado no banco de dados.") 
print("Sistema encerrado.")

# and e or
# and comparações verdadeiras e iguais
# or comparações verdadeiras e não iguais

# Exercício 4 
# Monitor de pressão crítica (while)
# Crie um simulador onde o usuário deve digitar a pressão atual de um compressor
# Enquanto a pressão for menor que 100 PSI, o programa continua pedindo a nova leitura
# Assim que o usuário digitar um valor maior ou igual a 100, o loop para e exibe a mensagem: "ALERTA: Pressão crítica atingida! Desligando sistema."

pressao = int(input("Digite a pressão atual do compressor: "))
while pressao < 100:
    pressao = int(input("Digite a pressão atual do compressor: "))
    if pressao >= 100:
        print("ALERTA, pressão em níveis críticos! Desligando sistemas...")

# Exercício 5
# Criar um menu de opções com 4 itens ex: Escolher Series apresente sua escolha de series das outras três.
# Qualquer opção diferente sai do menu

print("Chegou a sua hora treinador, escolha seu pokemon inicial:")
print("Bulbassauro = 1")
print("Charmander = 2")
print("Squirtle = 3")
print("Pikachu = 4")

pokemon = input("Sua escolha: ")

if pokemon == 1:
    print("Parabéns, você escolheu o Bulbassauro, do tipo planta!")
elif pokemon == 2:
    print("Parabéns, você escolheu o Charmander, do tipo fogo!")
elif pokemon == 3:
    print("Parabéns, você escolheu o Squirtle, do tipo água!")
elif pokemon == 4:
    print("Parabéns, você escolheu o Pikachu, do tipo elétrico!")
else:
    print("Você escolheu sair sem pokemons")
