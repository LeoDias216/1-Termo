# Desafio 1:

print("Bem-vindo ao Magnum Cars")
dias_alugado = int(input("Por quantos dias seu veículo foi alugado? "))
km_rodados = float(input("Quantos quilômetros ele rodou? "))

pagamento_dias = dias_alugado * 90

if km_rodados <= 100:
    total_menor = km_rodados * 0.20
    valor_total = pagamento_dias + total_menor
    print(f"O valor total a ser pago será de {valor_total:.2f} reais.")
elif km_rodados > 100:
    total_maior = km_rodados * 0.15
    valor_total = pagamento_dias + total_maior
    print(f"O valor total a ser pago será de {valor_total:.2f} reais.")

# Desafio 2:

numeros = [12, 5, 8, 21, 14, 3, 10, 7]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

media = sum(pares) / len(pares)
print(f"Pares: {pares}")
print(f"Média dos pares: {media:.2f}")

# Desafio 3:

produto = {"nome": "Teclado Mecânico", "preco": 200.0, "estoque": 15, "categoria": "Perifericos" }

def aplicar_desconto(item, porcentagem):
    item["preco"] -= item["preco"] * (porcentagem / 100)
    print(f"O produto {item['nome']} agora custa R$ {item['preco']:.2f}!")

aplicar_desconto(produto, 10)