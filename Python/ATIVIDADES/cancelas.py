import time

vaga = 500

while True:
    print("Bem vindo ao estacionamento do shopping!")
    print(f"Ainda temos {vaga} vagas disponíveis")

    print("Siga abaixo a tabela de preços:")
    print("Até 15 minutos: Grátis")
    print("Até 3 horas: Valor fixo de R$ 15,00.")
    print("Hora adicional: R$ 3,00 por hora extra")
    print("Obs: Clientes com TAG possuem 10% de desconto sobre o valor total, lembre de verificar se a TAG está ativa.")
    print("")

    print("Digite 1 se deseja ticket físico, 2 para TAG ou 3 para sair do estacionamento")
    tipo_de_acesso = int(input("Insira a opção desejada: "))

# Entrada com o ticket:
    if tipo_de_acesso == 1:
        if vaga > 0:
            hora_de_entrada_ticket = int(input("Insira o horário atual (14:30 = 1430): "))
            print("Pegue seu ticket impresso e avance pela catraca aberta")
            vaga -= 1
            time.sleep(3)
        else:
            print("Estacionamento lotado para tickets!")

# Entrada com a TAG:
    elif tipo_de_acesso == 2:
        tag_ativa = input("A TAG está ativa? (s/n): ")
        if tag_ativa == "s":
            hora_de_entrada_tag = int(input("Insira o horário atual (14:30 = 1430): "))
            print("TAG válida, avance pela catraca aberta")
            vaga -= 1
            time.sleep(3)
        else:
            print("TAG inválida ou inativa!")

# Saída:
    elif tipo_de_acesso == 3:
        print("Você escolheu sair")
        print("1=ticket")
        print("2=TAG")
        print("3=Perdi meu ticket")
        forma_de_entrada = int(input("Insira a forma de entrada: "))

        if forma_de_entrada == 1:
            hora_de_saida = int(input("Insira o horário atual como o exemplo (14:30 = 1430 ou 17:00 = 1700): "))
            hora_total = hora_de_saida - hora_de_entrada_ticket
            hora_a_ser_paga = hora_total - 40
            if hora_a_ser_paga <= 15:
                print("Saída grátis, catraca aberta, boa viagem!")
                vaga += 1
                time.sleep(3)
            elif 15 < hora_a_ser_paga <= 180:
                print("O ticket está no valor de R$15,00, insira a forma de pagamento")
                time.sleep(7)
                print("Ticket pago, catraca aberta, boa viagem!")
                vaga += 1
                time.sleep(3)
            elif hora_a_ser_paga > 180:
                horas_extras = int(input("Quantas horas extras você ficou, além de 3? "))
                valor_por_hora = horas_extras * 3
                valor_final = valor_por_hora + 15
                print(f"O valor do seu ticket é de R${valor_final},00, insira a forma de pagamento")
                time.sleep(7)
                print("Ticket pago, catraca aberta, boa viagem!")
                vaga += 1
                time.sleep(3)
        elif forma_de_entrada == 2:
            hora_de_saida = int(input("Insira o horário atual como o exemplo (14:30 = 1430 ou 17:00 = 1700): "))
            hora_total = hora_de_saida - hora_de_entrada_tag
            hora_a_ser_paga = hora_total - 40
            hora_final = hora_a_ser_paga * 0.90
            if hora_final <= 15:
                print("Saída grátis, catraca aberta, boa viagem!")
                vaga += 1
                time.sleep(3)
            elif 15 < hora_final <= 180:
                print("A TAG está no valor de R$15,00, insira a forma de pagamento")
                time.sleep(7)
                print("TAG paga, catraca aberta, boa viagem!")
                vaga += 1
                time.sleep(3)
            elif hora_final > 180:
                horas_extras = int(input("Quantas horas extras você ficou, além de 3? "))
                valor_por_hora = horas_extras * 3
                valor_final = valor_por_hora + 15
                print(f"O valor da sua TAG é de R${valor_final},00, insira a forma de pagamento")
                time.sleep(7)
                print("TAG paga, catraca aberta, boa viagem!")
                vaga += 1
                time.sleep(3)
        elif forma_de_entrada ==3:
            print("Em caso de perda de Ticket, o valor a ser pago é R$50,00")
            print("Insira sua forma de pagamento")
            time.sleep(7)
            print("Pagamento concluído, catraca aberta, boa viagem!")
            vaga += 1
            time.sleep(3)
            