# Atividade 1:
print("Bem vindo ao mundo da programação em Python!")

# Atividade 2:
nome = input("Bem vindo ao cadastro Magnum.com, digite seu nome completo: ")
idade = int(input("Agora, insira sua idade: "))
print("No seu cadastro final, aparecera como Sr./Sra.", nome, "de", idade, "anos")

# Atividade 3:
print("Bem vindo a calculadora Magnum Enterprises, o último usuário pediu a resolução da conta 135 + 246, que será", (135 + 246))
print("Também foi pedido a resolução da conta 512 - 128, que será", (512 - 128))
print("Agora, faça seus próprios cálculos na calculadora Magnum")

n1 = float(input("Para começarmos na soma, escreva seu primeiro valor:"))
n2 = float(input("Agora, o segundo valor:"))
total = n1 + n2
print("O valor final da sua soma será", total)

n3 = float(input("Indo para subtração, digite seu primeiro valor:"))
n4 = float(input("Agora, o segundo valor:"))
total = n3 - n4
print("O valor final de sua subtração será", total)

# Atividade 4:
print("Bem vindo a calculadora Magnum Enterprises Supreme de multiplicação e divisão, o último usuário pediu a resolução da conta 15 * 8, que será", (15 * 8))
print("Também foi pedido a resolução da conta 78 / 3, que será", (78 / 3))

# Atividade 5:
print("Bem vindo a calculadora Magnum Enterprises Supreme Gold de potenciação, o último usuário pediu a resolução da conta 5 elevado à 3 potência, que será", (5 ** 3))

# Atividade 6:
print("Gostariamos de parabenizar o funcionário do mês da Magnum Enterprises, Leo" + " " + "Dias")

# Atividade 7:
print("Bem vindo ao calculador de aproveitamento de peças Magnum CIA")
boas = int(input("Digite a quantidade de peças boas que encontrou: "))
ruins = int(input("Agora, a quantidade de peças ruins que encontrou: "))
total = boas + ruins
aproveitamento = boas / total
valor = aproveitamento * 100
print("Sendo assim, seu aproveitamento foi de", valor,"%")

# Atividade 8:
print("Eu tenho 16 anos e, em 10 anos, terei", 16 + 10, "anos")
idade = int(input("Qual a sua idade? "))
real = idade + 10
print("Você tem", idade,"anos e daqui 10 ano, terá", real,"anos")

# Atividade 9:
print("Bem vindo aos Hotéis Magnum Confort, o preço da passagem até aqui é R$ 420,00 e o por noite passada é R$ 250,50")
noites = int(input("Quantas noites você gostaria de reservar? "))
total = noites * 250,50
pagar = total + 420
print("Se você vai passar", noites, "noites, terá que pagar", pagar, "reais, incluindo a passagem")

# Atividade 10:
produto = input("Bem vindo aos relatórios Magnum Enterprises, por favor, diga o nome do seu produto: ")
quantidade = int(input("Agora, informe a quantidade vendida do produto: "))
preço = float(input("Por fim, informe o preço unitário do produto: "))
total = quantidade * preço
print("===================================")
print("                                   ")
print("        Relatório de vendas:       ")
print("                                   ")
print("===================================")
print("                                   ")
print("Produto:", produto)
print("Quantidade vendida:", quantidade)
print("Preço unitário: R$ ", preço)
print("Total de vendas: R$ ", total)
print("                                   ")
print("===================================")
