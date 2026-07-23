# Tipos de dados
# int
# float

x = 10
y = 5.15

#Números e valores
print("10")
print("5.15")

#Textos e String
print("Meu nome é leonardo")

#Concatenar
print("Eu gosto de programar \n" + "Python")

#Contas
n1 = 10
n2 = 5
print("Os valores são", n1 + n2)

#Operadores matemáticos
# + = soma
# - = subtração
# * = multiplicação
# / = divisão
# ^ = expoente

# Exemplo 2
n1 = 20
n2 = 10
print("Os valores", n1 * n2)

# Exemplo 3
n2 = input("Digite o seu primeiro número: \n")
print("Seu primeiro foi: \n", n2)

# Exemplo 4
nome = input("Qual é seu nome? \n")
print("Seu nome é: \n", nome) #Aqui ficaria mais completo
print(nome) #Aqui mais simples

# Exemplo 5
# Duas perguntas
# 1-Qual é seu curso
# 2-Qual é sua idade

curso = input("Qual é seu curso? \n")
print("Seu curso é: \n", curso)

idade = input("Qual é sua idade? \n")
print("Sua idade é: \n", idade)

# Exemplo 6 A
base = 10
altura = 5
area = (base * altura) / 2
print(area)

# Exemplo 6 B
base =int (input("Qual é a base da figura? \n "))
altura =int (input("Qual é a altura da figura? \n"))
area = (base * altura) / 2
print("A area da figura é: \n", int (area))

# Exercício 1
# Criar uma calculadora com soma e subtração

n1 = float (input("Bem vindo a calculadora, digite o primeiro valor para somar: \n"))
n2 = float (input("Agora digite o segundo: \n"))
resultado = (n1 + n2)
print("O resultado final é: \n", float (resultado))

n3 = float (input("Agora indo para subtração, digite o primeiro valor: \n"))
n4 = float (input("Digite o segundo valor: \n"))
resultado = (n3 - n4)
print("O resultado final é: \n", float (resultado))

# Exercício 2
# Calculadora de IMC (Potencia e divisão)
# O índice de massa corporal (IMC) é calculado dividindo o peso pela altura ao quadrado ($altura^2$)

peso = float (input("Bem vindo a calculadora de IMC, informe o peso: \n"))
altura = float (input("Agora informe a altura \n"))
alturareal = (altura * altura)
resultado = (peso / alturareal)
print("O IMC final é: \n", float (resultado))

# Exercício 3: O crachá (Variáveis e Strings)
# Crie 3 variáveis
# Uma chamada nome com o seu nome (String)
# Uma chamada idade com a sua idade (int)
# Uma chamada profissão com sua profissão ou "Estudante" (string)
# Tarefa: Imprima uma única frase concatenando essas variáveis, no formato:
# "Olá, meu nome é [nome], tenho [idade] anos e sou [profissão]."
# Para converter o número inteiro da idade para string, usa-se str(idade) para poder somar com textos

nome = input("Agora, para criarmos seu crachá, informe seu nome: \n")
idade = int(input("Agora, informe sua idade: \n"))
profissão = input("Por fim, sua proffisão, ou se é estudante: \n")
print("Seu crachá final é: ", nome, idade, profissão)

print("teste", nome + "ola", idade)