# Explicação de def: A palavra-chave "def" é usada para definir uma função em python. Uma função é um bloco de código reutilizável que realiza uma tarefa específica.
# return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a função foi chamada. O valor retornado pode ser usado posteriormente no código

# def nome_da_funcao(parametro1, parametro2):
#     # Corpo da função (código que será executado)
#     resultado = parametro1 + parametro2
#     return resultado

def saudacao(nome):
    return f"Olá, {nome}!"

def nome():
    nome = input("Digite seu nome: ")
    return nome
print(f"Olá, {nome()}!")

def valores():
    print("Digite 3 valores: ")
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    return a, b, c
print(f"O maior valor é: {max(valores())}")
# # Reutilizando funções
nome()
valores()

## Conceitos Chave:
# def: Indica o início da definição da função.
# Nome: Identifica a função para você chamá-la depois.
# Parâmetros: Dados que a função recebe (opcional).
# return: Envia o resultado de volta para quem chamou a função (opcional).
# def calcular_dobro(numero):
#     return numero * 2
# # Como usar:resultado = calcular_dobro(5)
# print(calcular_dobro(5))

def calcular_dobro():
    numero_escolhido = float(input("Digite um valor: "))
    
    return numero_escolhido * 2
print(calcular_dobro())