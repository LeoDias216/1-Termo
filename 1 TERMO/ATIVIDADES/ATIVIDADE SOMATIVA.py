# Atividade 1: Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa
# viagem!"

# print("Bem vindo ao registrador de carros Magnum enterprises!")
# modelo = input("Qual o modelo do seu veículo? ")
# placa = (input("Qual a placa do seu carro? "))
# print("Veículo", modelo,"de placa", placa,"registrado no sistema. Boa viagem!")

# Atividade 2: Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e
# o consumo médio do caminhão (km/l).
# ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque
# cheio.

# print("Bem vindo ao calculador de distância de caminhões Magnum Ride")
# litros = float(input("Qual a capacidade máxima do tanque de combustível do seu caminhão em litros? "))
# consumo = float(input("Qual é o consumo médio de litros do seu caminhão por 1 km?"))
# total = litros / consumo
# print("Se seu caminhão tem capacidade de", litros, "litros e o consumo médio dele por km é", consumo, "ele pode percorrer", total, "km com o tanque cheio")

# Atividade 3: Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em
# Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx
# 5,00~BRL$ e exiba com duas casas decimais.

# print("Bem vindo ao calculador de fretes Magnum Sedex")
# freteD = float(input("Qual o frete do produto em Dolar?"))
# total = freteD * 5
# print("No Brasil, o frete em reias ficará R$", total)

# Atividade 4: Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes
# realizadas por um motorista.
# ○ Exiba a média aritmética simples do tempo dessas entregas.

# print("Bem vindo ao calculador de médias de entrega Magnum Speed")
# rota1 = int(input("Qual o tempo, em horas, da sua primeira entrega? "))
# rota2 = int(input("Qual o tempo, em horas, da sua segunda entrega? "))
# rota3 = int(input("Qual o tempo, em horas, da sua terceira entrega? "))
# total = rota1 + rota2 + rota3
# media = total / 3
# print("Sua média final de tempo em cada entrega será de", media, "horas")

# Atividade 5: Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".

# peso = float(input("Bem vindo ao analisador de peso Magnum Security, insira o peso em toneladas do seu caminhão: "))
# if peso < 10:
#     print("É uma carga leve, tudo certo")
# elif 10 < peso <= 25:
#     print("É uma carga de peso padrão")
# elif peso > 25 :
#     print("É uma carga pesada, excesso de Peso!")

# Atividade 6: Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional".

# print("Bem vindo ao classificador de destino Magnum Locate")
# codigo = input("Insira a primeira letra do código da sua carga em maiúsculo: ")

# if codigo == "N":
#     print("Seu código indica para região Norte")

# elif codigo == "S":
#     print("Seu código indica para região Sul")

# else:
#     print("Seu código é de Região Internacional")

# Atividade 7: Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o
# motorista_identificado == "sim".
# ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

# checklist = input("Bem vindo ao liberador de saída Magnum Autorization, você está com a checklist em dia? Se sim, digite concluído, se não, digite não: ")
# identificado = input("Você é um motorista identificado, sim ou não?: ")

# if checklist == "concluído" and identificado == "sim":
#     print("Você está liberado para iniciar a rota")
# elif checklist == "concluído" and identificado == "não":
#     print("Rota bloqueada, falta identificação")
# elif checklist == "não" and identificado == "sim":
#     print("Rota bloqueada, falta sua checklist")
# elif checklist == "não" and identificado == "não":
#     print("Rota bloqueada, realize suas autorizações primeiro")

# Atividade 8: Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente".

# agendada = int(input("Bem vindo ao analisador de entregas Magnum Next, digite quantas entregas foram entregues agendadas: "))
# atraso = int(input("Agora, quantas entregas foram entregues atrasadas: "))
# total = agendada + atraso
# indice = total * 1.10
# indice2 = indice - total

# if indice2 < atraso:
#     print("Necessário otimizar")
# elif indice2 > atraso:
#     print("Logística eficiente")

# Atividade 9: Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

# pressao = float(input("Bem vindo ao calibrador de pneus Magnum Elastic, digite a medida de PSI do pneu: "))

# if 100 <= pressao <= 110:
#     print("Seu pneu está com o PSI dentro do padrão")
# elif pressao < 100:
#     print("O PSI do pneu está abaixo do recomendado")
# elif pressao > 110:
#     print("O PSI do pneu está acima do recomendado")

# Atividade 10: Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".

# import time
# for contagem in range(5,0,-1):
#     print(f"O portão de embarque se fecha em {contagem} segundos")
#     time.sleep(1)
# print("Portão trancado!")

# Atividade 11: Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de
# vários pedidos.
# ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total
# acumulado.

# valor = 0
# frete = float(input("Bem vindo ao Magnum calculator, qual o valor do frete? "))
# while frete != 0:
#     frete = float(input("Qual o valor do próximo frete? "))
#     valor += frete
# if frete == 0:
#     print("O faturamento total foi de R$", valor)

# Atividade 12: Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos
# diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada.

# for quilometragem in range(1, 6):
#     print(f"")

#Não consegui terminar :(

# Atividade 13: Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador
# ("track99").
# ○ Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se
# esgotar, exiba "Rastreamento Bloqueado".

# valor = 0
# while valor > 3:
# senha = input("Por favor, insira a senha do rastreador: ")

# if senha != "track99":
#     print("Acesso negado")
#     valor += 1
# if senha == "track99":
#     print("Acesso concedido")
# if valor == 3:
#     print("Acesso bloqueado")

#Não consegui terminar :(