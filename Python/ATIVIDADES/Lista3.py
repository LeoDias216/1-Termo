# Atividade 1:

# Jeito errado:

# idade = input("Digite sua idade: ")
# if idade >= 18:
#     print("Você é maior de idade.")

# Jeito correto:

# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")
# Antes do input eu coloquei int, porque idade é um número inteiro

# Jeito melhorado:

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
elif idade <= 17:
    print("Você é menor de idade")

# Atividade 2:

# Jeito errado:

# nome = "Mariana"
# print("Seja bem-vinda,nome!")

# Jeito correto:

# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")
# Coloquei um f no começo para chamar a variável e coloquei o nome na chave para demonstrar que é a variável

# Jeito melhorado:

nome = input("Qual o seu nome? \n ")
print(f"Seja bem-vinda, {nome}!")

# Atividade 3:

# Jeito errado:

# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# Jeito correto:

# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")
# Coloquei espaços na frente dos prints, sinalizando que eles estão dentro de outros comandos, como o if e o else

# Jeito melhorado:

numero = float(input("Digite um número: "))
if numero > 5:
    print("O número é maior que cinco.")
elif numero <= 5:
    print("O número é menor ou igual a cinco.")

# Atividade 4:

# Jeito errado:

# usuario = "aluno123"
# if usuario == "aluno123"
#     print("Login realizado com sucesso.")

# Jeito correto:

usuario = "aluno123"
if usuario == "aluno123":
    print("Login realizado com sucesso.")
# Faltou os dois pontos no final da segunda linha, indicando que continua no print de baixo

# Atividade 5:

# Jeito errado:

# clima = "ensolarado"
# if clima = "chuvoso":
#     print("Leve um guarda-chuva!")


# Jeito correto:

clima = "ensolarado"
if clima == "chuvoso":
    print("Leve um guarda-chuva!")
# Coloquei mais um sinal de igual (=) na segunda linha, para indicar a igualdade entre textos

# Atividade 6:

# Jeito errado:

# pontos = 50
# print("Parabèns! Você fez " + pontos + "pontos.")

# Jeito correto:

pontos = 50
print(f"Parabéns! Você fez", pontos,"pontos")
# Substitui os sinais de adição por vírgulas, para assim chamar a variável

# Atividade 7:

# Jeito errado:

# nota = 9.5
# if nota >= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

# Jeito correto:

nota = 9.5
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado")
# Inverti a ordem e coloquei a nota >= 9 como a prioridade

# Atividade 8:

# Jeito errado:

# for i in range(5):
#     print(i)

# Jeito correto:

for i in range(1, 6):
    print(i)
# Coloquei dentro do parentese o número 1, para a contagem não iniciar do zero e o 6 porque ele sempre conta até o anterior do segundo número no parentese

# Atividade 9:

# Jeito errado:

# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")

# Jeito correto:

tentativas = 1
while tentativas <= 3:
    print("Tentando conectar...")
    tentativas += 1
# Adicionei "tentativas += 1" no final, para limitar em 3 tentativas e depois parar

# Atividade 10:

# Jeito errado:

# senha = ""
# while senha == "python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Jeito correto:

senha = ""
while senha != "python123":
    senha = input("Digite a senha secreta: ")
print("Acesso concedido!")
# Ao invés do "==", coloquei o "!=", sinalizando que ele deve digitar novamente se a senha for diferente de python123, e não igual
