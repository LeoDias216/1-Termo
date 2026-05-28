import time
vida_jogador = 15
vida_inimigo= 20

def status():
    print("╔═══════════════════════════╗")
    print("║   == STATUS DE JOGO  ==   ║")
    print("║═══════════════════════════║")
    print(f"║ Vida do Jogador: {vida_jogador}/15    ║")
    print(f"║ Vida do Inimigo: {vida_inimigo}/20    ║")
    print("╚═══════════════════════════╝")

def acoes():
    global vida_inimigo, vida_jogador
    print("ESCOLHA SUA AÇÃO:")
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗")
    print("║ 1. Atacar   ║ ║ 2. Defender ║ ║ 3. Item     ║")
    print("╚═════════════╝ ╚═════════════╝ ╚═════════════╝")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print("Você ataca o Orc com sua espada")
        time.sleep(1)
        print("4 de dano causado!")
        vida_inimigo -= 4
    elif opcao == 2:
        print("Você escolheu se defender com seu escudo")
        time.sleep(1)
        print("Em guarda!")
    elif opcao == 3:
        print("BOLSA:")
        print("╔═════════════════════╗ ╔══════════════════╗")
        print("║ 1. Poção de vida x2 ║ ║ 2. Arco e flecha ║")
        print("╚═════════════════════╝ ╚══════════════════╝")
        item_usado = int(input("Opção: "))
        if item_usado == 1:
            print("Você bebe a poção...")
            time.sleep(1)
            print("Recuperou 5 pontos de vida!")


        

while True:
    print("╔════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                                ║")
    print("║            ██╗ ██████╗ ██████╗ ███╗   ██╗ █████╗ ██████╗  █████╗               ║")
    print("║            ██║██╔═══██╗██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔══██╗              ║")
    print("║            ██║██║   ██║██████╔╝██╔██╗ ██║███████║██║  ██║███████║              ║")
    print("║       ██   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══██║██║  ██║██╔══██║              ║")
    print("║       ╚█████╔╝╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝██║  ██║              ║")
    print("║        ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝              ║")
    print("║                                                                                ║")
    print("║                               ██████╗  ██████╗                                 ║")
    print("║                               ██╔══██╗██╔═══██╗                                ║")
    print("║                               ██║  ██║██║   ██║                                ║")
    print("║                               ██║  ██║██║   ██║                                ║")
    print("║                               ██████╔╝╚██████╔╝                                ║")
    print("║                               ╚═════╝  ╚═════╝                                 ║")
    print("║                                                                                ║")
    print("║                    ██╗  ██╗███████╗██████╗  ██████╗ ██╗                        ║")
    print("║                    ██║  ██║██╔════╝██╔══██╗██╔═══██╗██║                        ║")
    print("║                    ███████║█████╗  ██████╔╝██║   ██║██║                        ║")
    print("║                    ██╔══██║██╔══╝  ██╔══██╗██║   ██║██║                        ║")
    print("║                    ██║  ██║███████╗██║  ██║╚██████╔╝██║                        ║")
    print("║                    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝                        ║")
    print("║                                                                                ║")
    print("║                                                                                ║")
    print("║                            ► [1] INICIAR JOGO                                  ║")
    print("║                            ► [2] ENCERRAR                                      ║")
    print("║                                                                                ║")
    print("║                                                                                ║")
    print("╚════════════════════════════════════════════════════════════════════════════════╝")
    iniciar = int(input("Opção: "))
    if iniciar == 1:
        status()
        acoes()


    elif iniciar == 2:
        print("Encerrando jogo...")
        time.sleep(2)
        break
    else:
        print("Opção inválida")




