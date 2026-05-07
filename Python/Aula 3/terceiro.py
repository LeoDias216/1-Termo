#Condições lógicas
# if: "Se" a condição for verdadeira.
# elif: "Senão, se" (usado para múltiplas condições).
# else: "Senão" (executa se nenhuma das anteriores for verdadeira).

# Exemplo 1:

print("Verificar maioridade")
idade = int(input("Digite sua idade"))

if idade >= 18:
    print("Você é adulto")
elif idade >= 16:
    print("Você não é Adulto mas pode votar")
else:
    print("Você é adolescente")

# Sinais de > Maior e >= Maior Igual
# Sinais de < Menor e <= Menor Igual
#Sinais de == Igual

# Exemplo 2:
print("Loja")
print("Bem vindo ao sistema da loja do Carlos Magnum")
print("Opções:")
print(" 1 - Sapatos")
print(" 2 - Roupas")
print(" 3 - Perfumes")

escolha = int(input("Digite sua escolha pelo número da opção:"))
if escolha == 1:
    print("Você quer comprar Sapatos, OK")
    v1 = float(input("Digite o valor do produto: "))
    qt1 = int(input("Digite a quantidade desejada: "))
    total = v1 * qt1
    print("Sua compra de sapatos foi um total de: ", total)
elif escolha == 2:
    print("Você quer comprar Roupas, OK")
    v1 = float(input("Digite o valor do produto: "))
    qt1 = int(input("Digite a quantidade desejada: "))
    total = v1 * qt1
    print("Sua compra de roupas foi um total de: ", total)
elif escolha == 3:
    print("Você quer comprar Perfumes, OK")
    v1 = float(input("Digite o valor do produto: "))
    qt1 = int(input("Digite a quantidade desejada: "))
    total = v1 * qt1
    print("Sua compra de perfumes foi um total de: ", total)
else:
    print("Obrigado por utilizar o sistema do Carlos, agora visite o Instagram dele, Carlos Magnum")

# Exemplo 3
print("Escolha uma opção para iniciar o sistema")
print("Séries = S")
print("Filmes = F")
categoria = input("Digite sua categoria")
if categoria == "S":
    print("Você escolheu por Séries")
elif categoria == "F":
    print("Você escolheu por filmes")
else:
    print("Obrigado por usar o sistema Magnum")

# Exercício 1
# Crie um algoritmo que simule uma calculadora e que por opção de escolha permita calcular os operadores.
# Ex: Ao escolher a opção 1, ele ira calcular a soma e assim por diante

print("Bem vindo a calculadora Magnum, escolha sua operação:")
print("A - Adição")
print("S - Subtração")
print("M - Multiplicação")
print("D - Divisão")

escolha = input("Operação escolhida:")
if escolha == "A":
    print("Você escolheu adição, agora digite os valores")
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Agora digite o segundo valor: "))
    total = n1 + n2
    print("Seu valor total foi de:", total)
elif escolha == "S":
    print("Você escolheu subtração, agora digite os valores")
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Agora digite o segundo valor: "))
    total = n1 - n2
    print("Seu valor total foi de:", total)
elif escolha == "M":
    print("Você escolheu multiplicação, agora digite os valores")
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Agora digite o segundo valor: "))
    total = n1 * n2
    print("Seu valor total foi de:", total)
elif escolha == "D":
    print("Você escolheu divisão, agora digite os valores")
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Agora digite o segundo valor: "))
    total = n1 / n2
    print("Seu valor total foi de:", total)
else:
    print("Obrigado por usar a calculadora Magnum")

# Exercício 2
# Calculo de idade: Deve apresentar o nome, curso, data nascimento(ano) e apresentar a idade sua no final

print("Bem vindo ao cálculo de idade Magnus Enterprise, comece informando seu nome")
nome = input("Seu nome: ")
curso = input("Agora, seu curso: ")
ano = float(input("Por fim, seu ano de nascimento: "))
idade = 2026 - ano
print("Seu nome é", nome, "você está no curso de", curso, "e sua idade é", idade)

# Exercício 3
# Calcular gorjetas: Receba o valor da conta de um restaurante e retorne o valor da gorjeta (Considerando 10% do valor da conta).
# Atendimento em mesa com garçom 10%
# Atendimento em mesa sem garçom 5%

print("Bem vindo ao restaurante Magnum Massas")
print("Você pode optar por atendimento de garçom, sujeito a maior gorjeta na conta final")
print("S - Sim")
print("N - Não")

escolha = input("Deseja atendimento de garçom?")
if escolha == "S":
    n1 = float(input("Agora informe o valor do seu prato: "))
    n2 = n1 + n1/10
    print("O valor total da sua conta será de:", n2,"já incluindo a gorjeta do garçom") 
elif escolha == "N":
    n1 = float(input("Agora informe o valor do seu prato: "))
    n2 = n1 + n1/20
    print("O valor total da sua conta será de:", n2,"sem atendimento a garçom") 

# Exercício 4
# Criar um sistema para calcular o sucessor e antecessor de um valor

print("Bem vindo ao calculador supremo Magnum Enterprises Gold")
n1 = float(input("Comece informando um número para calcularmos seu antecessor e sucessor: "))
n2 = n1 - 1
n3 = n1 + 1
print("Se seu número escolhido foi:", n1,"o antecessor dele é", n2,"e o sucessor é", n3)

# Exercício 5
# Criar um algoritmo para calcular a venda de livros e que toda venda apresente um desconto fixo de 5%

print("Bem vindo a livraria Magnum Read Supreme")
print("Estamos com um desconto semanal de 5% em todos os livros")
n1 = float(input("Por favor, informe o valor do seu livro ou de todos no total: "))
n2 = n1 - n1/20
print("Aplicando o desconto, o preço total será de", n2)

print("Bem vindo a livraria Magnum Read Supreme")
print("Estamos com um desconto semanal de 5% em todos os livros")
print("Por favor, escolha um livro abaixo para comprar:")
print("1 - Harry Potter")
print("2 - O Alquimista")
print("3 - Diário de um banana")
print("4 - Minha mãe é uma peça")

escolha = input("Coloque o número do livro:")
if escolha == "1":
    n1 = 40
    n2 = n1 + n1/20
    print("O livro Harry Potter custa", n1,"reais, aplicando o desconto fica", n2,"reais")
elif escolha == "2":
    n1 = 30
    n2 = n1 + n1/20
    print("O livro O Alquimista custa", n1,"reais, aplicando o desconto fica", n2,"reais")
elif escolha == "3":
    n1 = 25
    n2 = n1 + n1/20
    print("O livro Diário de um banana custa", n1,"reais, aplicando o desconto fica", n2,"reais")
elif escolha == "4":
    n1 = 50
    n2 = n1 + n1/20
    print("O livro Minha mãe é uma peça custa", n1,"reais, aplicando o desconto fica", n2,"reais")
    