import time
import os

posicao_defesa = False

pocoes = 2
apagadores = 1


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
    print(f"║ Vida do Jogador: {vida_jogador:<2}/15    ║")
    print(f"║ Vida do Inimigo: {vida_inimigo:<2}/20    ║")
    print("╚═══════════════════════════╝")

def acoes():
    global vida_inimigo, vida_jogador, posicao_defesa
    global pocoes, apagadores
    print("ESCOLHA SUA AÇÃO:")
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗")
    print("║ 1. Atacar   ║ ║ 2. Defender ║ ║ 3. Item     ║")
    print("╚═════════════╝ ╚═════════════╝ ╚═════════════╝")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print("Você ataca o Orc com seu canetão!")
        time.sleep(2)
        print("4 de dano causado!")
        vida_inimigo = max(0, vida_inimigo - 4)
    elif opcao == 2:
        print("Você escolheu se defender com seu teclado escudo")
        time.sleep(2)
        print("Em guarda!")
        posicao_defesa = True
    elif opcao == 3:
        print("BOLSA:")
        print("╔═════════════════════╗ ╔════════════════════════════╗ ╔═══════════╗")
        print(f"║ 1. Poção de vida x{pocoes:<2}║ ║ 2. Apagador arremesável x{apagadores:<2}║ ║ 3. Voltar ║")
        print("╚═════════════════════╝ ╚════════════════════════════╝ ╚═══════════╝")
        item_usado = int(input("Opção: "))
        if item_usado == 1:

            if pocoes > 0:
                pocoes -= 1
                print("Você bebe a poção...")
                time.sleep(2)
                print("Recuperou 5 pontos de vida!")
                vida_jogador = min(15, vida_jogador + 5)
            else:
                print("Você não possui mais poções!")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                orc()
                status() 
                acoes()

        if item_usado == 2:
            if apagadores > 0:
                apagadores -= 1
                print("Você epicamente arremessa um apagador no Orc...")
                time.sleep(2)
                print("5 de dano nele!")
                vida_inimigo = max(0, vida_inimigo - 5)
            else:
                print("Você não possui mais apagadores!")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                orc()
                status() 
                acoes()
                
        if item_usado == 3:
            print("Voltando para as ações...")
            time.sleep(2)

            os.system("cls" if os.name == "nt" else "clear")
        
            orc()
            status() 
            acoes()  
            


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

        print("╔════════════════════════════════════╗")
        print("║         HISTÓRIA DO HERÓI          ║")
        print("╚════════════════════════════════════╝")

        print("\nVocê era apenas um professor comum...")
        time.sleep(2)

        print("Até que um Orc invadiu a escola!")
        time.sleep(2)

        print("A princesa foi sequestrada...")
        time.sleep(2)

        print("E agora só você pode salvá-la.")
        time.sleep(2)

        input("\nPressione ENTER para continuar...")

        os.system("cls" if os.name == "nt" else "clear")
                
        vida_jogador = 15
        vida_inimigo= 20
        turno_orc = 0
        pocoes = 2
        apagadores = 1

        while vida_jogador > 0 and vida_inimigo > 0:

            os.system("cls")

            orc()
            status()
            acoes()

            if vida_inimigo > 0:
                turno_orc += 1

                if turno_orc == 1:

                    print("\nO Orc avança furiosamente!")
                    time.sleep(2)

                    if posicao_defesa:
                        dano = 2
                        print("Seu teclado escudo absorveu parte do dano!")
                        time.sleep(2)
                    else:
                        dano = 4

                    vida_jogador = max(0, vida_jogador - dano)

                    print(f"Você recebeu {dano} de dano!")
                    time.sleep(2)
                    posicao_defesa = False
                                                                        
                elif turno_orc == 2:

                    print("\nO Orc ergue sua marreta gigantesca...")
                    time.sleep(2)

                    print("⚠ O Orc está preparando um ataque poderoso!")
                    time.sleep(2)

                # ATAQUE ESPECIAL
                elif turno_orc == 3:

                    print("\n☠ O Orc desfere um golpe devastador!")
                    time.sleep(2)

                    if posicao_defesa:
                        dano = 4
                        print("Você conseguiu bloquear parte do impacto!")
                        time.sleep(2)
                    else:
                        dano = 8

                    vida_jogador = max(0, vida_jogador - dano)

                    print(f"Você recebeu {dano} de dano!")
                    time.sleep(2)
                    posicao_defesa = False

                    turno_orc = 0

        if vida_inimigo <= 0:
            print("╔═════════════════════════════════════════════════════╗")
            print("║  ██╗   ██╗██╗████████╗ ██████╗ ██████╗ ██╗ █████╗   ║")
            print("║  ██║   ██║██║╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗  ║")
            print("║  ██║   ██║██║   ██║   ██║   ██║██████╔╝██║███████║  ║")
            print("║  ╚██╗ ██╔╝██║   ██║   ██║   ██║██╔══██╗██║██╔══██║  ║")
            print("║   ╚████╔╝ ██║   ██║   ╚██████╔╝██║  ██║██║██║  ██║  ║")
            print("║    ╚═══╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝  ║")
            print("║                                                     ║")
            print("║                O ORC FOI DERROTADO!                 ║")
            print("╚═════════════════════════════════════════════════════╝")
            time.sleep(2)

            print("╔═════════════════════════════════════════╗  ")
            print("║                                         ║  ")
            print("║             PRINCESA SALVA!             ║  ")
            print("║           _._                           ║  ")         
            print("║         ,'-._'-.                        ║  ")         
            print("║         ;'-._'-.'-.                     ║  ")         
            print("║         :.   '-.`. \                    ║  ")         
            print("║         (;`-._  `.\ ;                   ║  ")         
            print("║          :_  _'.   \:                   ║  ")         
            print("║          ;o: o` \  \;                   ║  ")         
            print("║          : ;     )-. `.                 ║  ")         
            print("║           ;=-  .:\     '-._             ║  ")         
            print("║           :_.-' ; `.       '-.          ║  ")         
            print("║     _._   ( :   :   '-._      '-.       ║  ")         
            print("║    /   `._.='    \               `.     ║  ")         
            print("║   :    \:         `-.__ _._   '-.  \    ║  ")         
            print("║    \    '.    _      ',' ` ',    \  ;   ║  ")         
            print("║     )-.   `j'^,L_..--'      ; ,-. : :   ║  ")         
            print("║    :   )-._;)(:_           / : ._.' ;   ║  ")         
            print("║    |  :   <_.Y( '-..__ _.+'\ :     /    ║  ")         
            print("║    ;  ;   ;    '      T   \ \ `---'`.   ║  ")
            print("╚═════════════════════════════════════════╝  ")
            time.sleep(3)
            break
                           
        elif vida_jogador <= 0:
            print("╔════════════════════════════════════════════════╗")
            print("║   ██████╗  █████╗ ███╗   ███╗███████╗          ║")
            print("║  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝          ║")
            print("║  ██║  ███╗███████║██╔████╔██║█████╗            ║")
            print("║  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝            ║")
            print("║  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗          ║")
            print("║   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝          ║")
            print("║                                                ║")
            print("║             ██████╗ ██╗   ██╗███████╗██████╗   ║")
            print("║            ██╔═══██╗██║   ██║██╔════╝██╔══██╗  ║")
            print("║            ██║   ██║██║   ██║█████╗  ██████╔╝  ║")
            print("║            ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  ║")
            print("║            ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║  ║")
            print("║             ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝  ║")
            print("║                                                ║")
            print("║             Você foi derrotado...              ║")
            print("╚════════════════════════════════════════════════╝")
            time.sleep(2)
            break
        
    elif iniciar == 2:
        print("Encerrando jogo...")
        time.sleep(2)
        break
    else:
        print("Opção inválida")




