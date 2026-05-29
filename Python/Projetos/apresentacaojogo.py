import time
vida_jogador = 15
vida_inimigo= 20

def orc():
    print("╔════════════════════════════╗  ")
    print("║          ,      ,          ║  ")
    print("║         /(.-''-.)\         ║  ")
    print("║     |\  \/      \/  /|     ║  ")
    print("║     | \ / =.  .= \ / |     ║  ")
    print("║     \( \   o\/o   / )/     ║  ")
    print("║      \_, '-/  \-' ,_/      ║  ")
    print("║        /   \__/   \        ║  ")
    print("║        \ \__/\__/ /        ║  ")
    print("║      ___\ \|--|/ /___      ║  ")
    print("║    /`    \      /    `\    ║  ")  
    print("╚════════════════════════════╝  ")    
     
  
def status():
    print("╔═══════════════════════════╗")
    print("║   == STATUS DE JOGO  ==   ║")
    print("║═══════════════════════════║")
    print(f"║ Vida do Jogador: {vida_jogador:02}/15    ║")
    print(f"║ Vida do Inimigo: {vida_inimigo:02}/20    ║")
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
        max(0, vida_inimigo - 4)
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
            vida_jogador = min(15, vida_jogador + 5)


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
        while vida_jogador > 0 and vida_inimigo > 0:
            orc()
            status()
            acoes()

        if vida_inimigo <= 0:
            print("\n🎉 Vitória! Você derrotou o Orc e salvou a princesa!\n")
        elif vida_jogador <= 0:
            print("")
        time.sleep(2)
        
    elif iniciar == 2:
        print("Encerrando jogo...")
        time.sleep(2)
        break
    else:
        print("Opção inválida")




