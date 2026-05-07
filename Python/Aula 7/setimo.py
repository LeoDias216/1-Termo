# Revisão Somativa - Aula 7

# Atividade 1:

# print("Registro de veículo")
# modelo = input("Qual é o modelo do veículo? ")
# placa = input("Informe a placa do veículo: ")
# print(f"Veículo {modelo} de placa {placa} registrado no sistema, Boa Viagem!")

# Atividade 2:

# print("Cálculo de Autonomia")
# capacidade_tanque = float(input("Digite a capacidade de litros"))
# consumo_medio = float(input("Digite o consumo do caminhão em km/l"))
# distancia_total = capacidade_tanque * consumo_medio
# print(f"Capacidade {capacidade_tanque} do tanque e sua distancia {consumo_medio} em média km/l e o total {distancia_total}")

# Atividade 3:

# print("Conversor de moeda (frete internacional)")
# valor_frete = float(input("Valor de frete em Dolar "))
# conversao_real = float(input("Valor da taxa em reais "))
# total_conversao = valor_frete * conversao_real
# print(f"O valor do frete foi {valor_frete} e a taxa aplicada foi de {conversao_real} e o total do frete {total_conversao:.2f}") # :.2f para exibir com duas casas decimais
# print("O valor do frete foi",valor_frete,"E a taxa aplicada foi de",conversao_real,"e o total do frete",round(total_conversao,2)) # round para exibir com duas casas decimais

# Atividade 4:

# print("Média de entregas")
# rota1 = int(input("Digite a primeira rota em horas: ")) # Alt + Shift + Seta para baixo
# rota2 = int(input("Digite a segunda rota em horas: "))
# rota3 = int(input("Digite a terceira rota em horas: "))
# media_rota = (rota1 + rota2 + rota3) /3
# print(f"A média de entregas das rotas realizadas foi de... {media_rota:.2f}")

# Atividade 5:

# print("Monitor de Carga - Peso em Toneladas")
# peso_caminhao = float(input("Informe o peso do caminhão em Toneladas"))
# if peso_caminhao <= 10:
#     print("Carga leve -)")
# elif peso_caminhao < 25:
#     print("Carga Padrão --)")
# elif peso_caminhao >= 25:
#     print("ALERTA: Excesso de Peso! ---)")
# else:
#     print("Digite outro valor ----)")
# # else:
# #     print("ALERTA: Excesso de Peso! ---)")

# # Atividade 6:

# print("Classificador de Destino - Código de Cargas")
# print("Código de Cargas = N - Norte S - Sul e Outros Internacional")
# codigo_carga = input("Inserir o código da Carga").upper()
# if codigo_carga == "N":
#     print("Região Norte")
#     #lower() # texto minusculo
# elif codigo_carga == "S":
#     print("Região Sul")
# elif codigo_carga == "O":
#     print("Região Internacional")
# else:
#     print("Região Internacional")

# # Atividade 7:

# print("Liberação de Saída - Checklist e Motorista")
# checklist = input("O Checklist foi realizado (Concluído ou Não Concluído)")
# motorista = input("O motorista foi identificado (Sim ou Não)")
# # and = verdadeiro verdadeiro
# # or + verdadeiro e falso
# if checklist == "Concluído" and motorista == "Sim":
#     print("Iniciar rota - Boa viagem")
# else:
#     print("Voltar e realizar o Checklist! :(")

# # Atividade 8:

# print("Cálculo de atrasos")
# entregas_agendadas = int(input("Quantidade de entregas agendadas"))
# entregas_atraso = int(input("Quantidade de entregas com atraso"))
# total = entregas_atraso / entregas_agendadas
# if total > 0.1:
#     print("Necessário otimizar rotas")
# else:
#     print("Logística eficiente")

# # Atividade 9:

# print("Validação de calibragem - pressão de pneus")
# carga_pressao = float(input("Digite a medida da pressão em PSI dos pneus"))
# if carga_pressao <= 100:
#     print("Abaixo do recomendado")
# elif carga_pressao >=110:
#     print("Acima do recomendado") 
# else:
#     print("Dentro do padrão recomendado")

# # Atividade 10:

# import time
# print("Contagem de embarque")
# for embarque in range(5,0,-1):
#     time.sleep(1)
#     print(f"Embarque em {embarque}")

# # Atividade 11:

# print("Somatório de frete (Acumulador)")
# faturamento = 0
# frete = 1

# while frete != 0:
#     frete = float(input("Valor do frete ou 0 para encerrar"))
#     faturamento += frete
# print(f"Faturamento total foi de {faturamento}")


# print("Somatório de Frete (Acumulador) - Versão 2.0")
# faturamento = 0
# while True:
#     valor = float(input("Valor do Frete ou 0 para finalizar"))
#     if valor == 0:
#         break
#     faturamento += valor
# print(f"Faturamento total {faturamento}em Reais")

# # Atividade 12:

# print("Monitoramento de Frota - Quilometragem")
# maior_km = 0
# for i in range(1,6):
#     km = float(input(f"Digite a quilometragem do veículo {i}"))
#     if km > maior_km:
#         maior_km = km
# print(f"A maior quilometragem registrada foi de {maior_km} km")


# var = 0
# print("Monitoramento de Frota - Km - Versão 2.0")
# veiculo1 = int(input("Informe a KM do veiculo 1"))
# for km in range(2,6):
#     veiculos = float(input(f"Informe a KM do veiculo{km}registrada"))
#     if veiculos > var:
#         var = var + veiculos
#     print(f"A maior KM foi de {var}")

# Atividade 13:

# print("Sistema de Rastreio")
# erros = 0
# tentativas = 3

# while erros != 3:
#     codigo = input("Insira o código de acesso")
#     if codigo != "track99":
#         erros = erros + 1
#         tentativas = tentativas - 1
#         print(f"Codigo incorreto você possui {tentativas}")
#     else:
#         break
#     if erros == 3:
#         print("Rastreamento bloqueado!")
#     else:
#         print("Acesso liberado :)")


# print("Sistema de rastreio - versão 2")
# acesso_negado = 0
# while acesso_negado != 3:
#     codigo = input("Digite o código de acesso do rastreador: ")
#     if codigo != "track99":
#         acesso_negado = acesso_negado + 1
#         print("Acesso Negado :(")
#         print("Rastreamento Bloqueado! ")
#     elif codigo:
#         print("Acesso Liberado")
#         break

# # Atividade 14:

# print("Gerenciador de combústivel")
# tanque = 500
# while True:
#     print("1 - Abastecer")
#     print("2 - Retirar")
#     print("3 - Sair")
#     opcao = input("Escolha uma opção")
#     if opcao == "1":
#         valor = float(input("Quantidade a abastecer"))
#         tanque += valor
#         print(f"Tanque atual: {tanque}")
#     elif opcao == "2":
#         valor = float(input("Quantidade a retirar"))
#         if valor > tanque:
#             print("Quantidade indisponível")
#         else:
#             tanque -= valor
#             print(f"Tanque atual {tanque}")
#     elif opcao == "3":
#         print("Encerrando o Sistema")
#         break
#     else:
#         print("Opção inválida")
#         if tanque < 50:
#             print("Reserva crítica")

# # Atividade 15:

# print("Relatório de inspeção de pneus")
# contagem = 0
# total = 5
# for pneu in range(1,6):
#     medida = float(input(f"Medida do sulco do pneu {pneu} em mm"))
#     if medida >= 1.6:
#         contagem = contagem + 1
#         print("Pneu aprovado e adicionado a contagem")
#     else:
#         print("Pneu fora das medidas regulares não foi adicionado a contagem")
#         pass 
#     porcentagem = (contagem / total) * 100
#     print(f"Tiveram {contagem} pneus aprovados hoje com uma taxa de {porcentagem}% de conformidade")


