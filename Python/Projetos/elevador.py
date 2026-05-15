# Sistema de elevador de prédio
# O prédio possui 10 andares sendo o térreo o andar 0. O elevador pode se mover para cima e para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

# Levantamento de Ideias:
# 10 andares, sendo 0 o térreo
# Capacidade de subir e descer
# Capacidade máxima de 5 pessoas
# Começa no 0 e pode ser chamado em qualquer andar
# Anda até onde a pessoa está e até o destino escolhido
# Mensagens indicando o andar atual, número de pessoas no elevador e ação atual
# O elevador pode parar se a senha do técnico for inserida

import time

andar_do_elevador = 0

while True:
    print("")
    print("Bem-vindo ao elevador Magnum Up, onde deseja ir hoje?")
    print(f"Andar atual: {andar_do_elevador}")
    print("A música de hoje é jazz")
    print("0 = Térreo")
    print("Andares 1 - 10")
    print("AVISO: Máximo de 5 pessoas no elevador")
    print("")
    andar = int(input("Digite o andar que deseja ir: "))

    if andar == andar_do_elevador:
        print("Você já está nesse andar")
        time.sleep(3)
    elif andar <= 10:
        print("Fechando portas...")
        time.sleep(3)
        if andar > andar_do_elevador:
            print("SUBINDO...")
            time.sleep(4)
        elif andar < andar_do_elevador:
            print("DESCENDO...")
            time.sleep(4)
        andar_do_elevador = andar
        print(f"Andar atual: {andar_do_elevador}")
        time.sleep(3)
        print("Abrindo portas...")
        time.sleep(3)
    elif andar == 11:
        print("Encerrando sistemas...")
        break
    else:
        print("Digite um andar válido")
        time.sleep(3)