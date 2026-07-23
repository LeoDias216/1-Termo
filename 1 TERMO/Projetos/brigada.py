# Desenvolva um programa em Python que gerencie o status de conformidade dos funcionários de uma empresa.
# 1 - Cadastro de funcionários:
# Armazene o nome, setor e o status dos treinamentos (NR-10, NR-35 e Brigada).
# 2 - Verificação de EPI (NR-6):
# O sistema deve receber o setor do funcionário.
# Se o setor for "Elétrica", liste a obrigatoriedade de luvas de alta tensão e botas dielétricas.
# Se o setor for "Trabalho em Altura", liste o cinturão de segurança e talabarte.
# 3 - Alerta de reciclagem:
# Crie uma função que receba o ano do último treinamento da Brigada de Incêndio.
# Se o treinamento tiver mais de 2 anos, exiba a mensagem: "Treinamento Vencido! Encaminhar para reciclagem."
# Caso contrário, exiba: "Treinamento Válido."
# 4 - Relatório geral:
# Exiba na tela um resumo com o total de funcionários cadastrados e quantos estão com treinamentos em dia.

# Levantamento de ideias:
# Armazenar nome, setor e status dos treinamentos dos funcionários
# Se o setor for elétrica, listar obrigatoriedade de luvas de alta tensão e botas dielétricas
# Se o setor for trabalho em altura, listar o cinturão de segurança e talabarte
# Função que analisa o ano do último treinamento de brigada e pode constar como vencido, para encaminhar para reciclagem
# Exibir um resumo com o total de funcionários cadastrados e quantos estão com os treinamentos em dia

def brigada():

    import time

    funcionarios_cadastrados = 0
    treinamentos_em_dia = 0

    while True:
        print("Bem vindo ao site da empresa Magnum Enterprises")
        print(f"Até o momento temos {funcionarios_cadastrados} funcionários cadastrados e {treinamentos_em_dia} treinamentos em dia")
        nome_funcionario = input("Digite seu nome:")
        if nome_funcionario == "Encerrar":
            print("Encerrando sistemas...")
            time.sleep(1)
            break
        setor_funcionario = input("Digite seu setor (Elétrica ou Altura):")
        if setor_funcionario == "Elétrica":
            print("EPI necessário:")
            time.sleep(2)
            print("Luvas de alta tensão")
            time.sleep(2)
            print("Botas dielétricas")
            time.sleep(2)
        elif setor_funcionario == "Altura":
            print("EPI necessário:")
            time.sleep(2)
            print("Cinturão de segurança")
            time.sleep(2)
            print("Talabarte")
            time.sleep(2)
        else:
            print("Setor inválido")
        nr_10 = input("Você está com o treinamento NR-10 em dia? s/n: ")
        nr_35 = input("Você está com o treinamento NR-35 em dia? s/n: ")
        treinamento_brigada = input("Você está com o treinamento de brigada em dia? s/n: ")
        if nr_10 == "s" and nr_35 == "s" and treinamento_brigada == "s":
            print("Todos os treinamentos em dia, parabéns!")
            treinamentos_em_dia += 1
            time.sleep(1)
        ultimo_ano_brigada = int(input("Quando foi seu último ano em que realizou o treinamento de brigada?"))
        if 2026 - ultimo_ano_brigada > 2:
            print("Treinamento vencido! Encaminhar para reciclagem")
            time.sleep(2)
        else:
            print("Treinamento válido")
            time.sleep(1)
        print(f"Cadastro diário concluído! Bom trabalho {nome_funcionario}")
        funcionarios_cadastrados += 1
        time.sleep(2)
brigada()