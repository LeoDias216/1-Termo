# Clean code:

# Sem Clean Code:
nick = input("Digite seu Nick: ")
nivel = int(input("Digite seu nível: "))
print("O jogador", nick,"está no nível", nivel,"e pronto para a partida!")

# # Com Clean Code:
def exibir_status_pre_jogo(nickname: str, nivel_atual: int):
    """Gera a mensagem de saudação baseada no nível do jogador."""
    print(f"O jogador {nickname} está no nível {nivel_atual} e pronto para a partida!")


nome_usuario = input("Digite seu nick: ")
nivel_usuario = int(input("Digite seu nível: "))

exibir_status_pre_jogo(nome_usuario, nivel_usuario)

# Segundo exemplo:

# Sem Clean Code:
mesada = float(input("Quanto você ganha por semana? "))
total = mesada * 4
print("No final do mês, você terá: R$ ",total ,)


# Com Clean Code:
SEMANAS_NO_MES = 4

def calcular_projecao_mensal(valor_semanal: float) -> float:
    return valor_semanal * SEMANAS_NO_MES


valor_recebido = float(input("Quanto você ganha por semana? "))
total_mensal = calcular_projecao_mensal(valor_recebido)

print(f"No final do mês, você terá: R$ {total_mensal:.2f}")
