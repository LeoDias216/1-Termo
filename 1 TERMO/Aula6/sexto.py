# Lista de temperaturas lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
#     print(f"Temperatura está em {temp}°C. Operação normal.")

# print("Sistema desligado. Aguardando manutenção.")

# Cenário 2
# Adicionar outra condição para temperatura abaixo de 50 e quando chegar até 10 parar

# leituras = [70, 75, 82, 98, 110, 85, 80]
# baixos = [10, 20, 30, 40, 50, 40, 10]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
# for temp1 in baixos:
#     if temp < 50:
#         print(f"CRÍTICO: {temp1}°C detectado! Acionando parada de emergência.")
#         break
#     else:
#         print(f"Temperatura está em {temp1}°C. Operação com valores baixos.")
# print("Checar sistema. Aguardando manutenção.")

# Próximo:

# materiais = ["metal", "metal", "plástico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
#         continue # Pula o restante do código abaixo e vai para a próxima peça

#     # Este código só roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando e polindo...")

# print("Fim do lote de produção.")

# Exercício 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5).

# from time import sleep
# for numero in range (1, 11):
#     if numero == 5:
#         print("Erro na impressão")
#         sleep(1.5)
#         continue
#     print(f"Contando número {numero}")
#     sleep(2)

# Exercício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa.

# from time import sleep
# for cor in range (1, 14):
#     if cor < 6:
#         print("Semáforo Verde")
#         sleep(1)
#     if cor == 6:
#         print("Semáforo amarelo")
#         sleep(1)
#     if cor == 7:
#         print("Semáforo amarelo")
#         sleep(1)
#     if cor == 8:
#         print("Semáforo amarelo")
#         sleep(1)
#     if cor > 8:
#         print("Semáforo vermelho")
#         sleep(1)

# Exercício 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# for maquina in range (1, 6):
#     if maquina == 1:
#         maq = float(input("Qual o consumo da primeira máquina em kWh? "))
#     if maquina == 2:
#         maq2 = float(input("Qual o consumo da segunda máquina em kWh? "))
#     if maquina == 3:
#         maq3 = float(input("Qual o consumo da terceira máquina em kWh? "))
#     if maquina == 4:
#         maq4 = float(input("Qual o consumo da quarta máquina em kWh? "))
#     if maquina == 5:
#         maq5 = float(input("Qual o consumo da quinta máquina em kWh? "))
# total = maq + maq2 + maq3 + maq4 + maq5
# print("O total de consumo foi", total,"kWh")

# Exercício 4 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for pecas in medidas:
#     if pecas >= 50:
#         print(f"Peça {pecas} aceita...")
#     else:
#         print(f"Peça {pecas} rejeitada")

# Exercício 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.

# sacos = [49.5, 50.0, 51.2, 48.9, 50.5, 47.8]
# for peso in sacos:
#     if 49.0 <= peso <= 51.0:
#         print(f"Saco com peso {peso}Kg: Aceitável")
#     else:
#         print(f"Saco com peso {peso}Kg: Rejeitado - Fora do limite aceitável")

# O Desafio: Gestão de Ciclo Térmico
# Você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças.
# Regras do Sistema:
# O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# Para cada peça, peça ao usuário a temperatura atual (input).
# Filtro de Erro (continue): Se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de Emergência (break): Se a temperatura for maior que 150°C, o sistema deve exibir "ALERTA CRÍTICO: Risco de Explosão!", interromper o loop imediatamente e encerrar o programa.

# estufa = 0
# while estufa < 5:
#     temp = float(input("Digite a temperatura da estufa: "))
#     if temp < 0:
#         print("Erro de leitura no sensor. Por favor, insira uma temperatura válida.")
#         continue
#     elif temp > 150:
#         print("ALERTA CRÍTICO: Risco de Explosão!")
#         break
#     else:
#         print(f"Peça {estufa + 1} processada com sucesso a {temp}°C.")
#         estufa += 1

# Exercicio 8 - Monitoramento de Vibração
# Uma máquina industrial tem um sensor de vibração que registra os seguintes valores em mm/s: [0.5, 1.2, 0.8, 2.5, 0.3, 1.0, 3.0, 0.4]. O limite de vibração aceitável é de até 1.5 mm/s.
# Crie um programa que percorra a lista de vibração e:
# - Se a vibração for maior que 1.5 mm/s, exiba "ALERTA: Vibração excessiva detectada!" e continue para a próxima leitura.
# - Se a vibração for menor ou igual a 1.5 mm/s, exiba "Vibração dentro do limite aceitável." para cada leitura.

valores = [0.5, 1.2, 0.8, 2.5, 0.3, 1.0, 3.0, 0.4]
for vibracao in valores:
    if vibracao > 1.5:
        print("ALERTA: Vibração excessiva detectada!")
        continue
    elif vibracao <= 1.5:
        print("Vibração dentro do limite aceitável.")
        continue
