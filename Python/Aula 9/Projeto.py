# 1: O estacionamento possui um total de 500 vagas.
# 2: O sistema deve manter um contador de vagas ocupadas. Se o estacionamento estiver lotado, a
# cancela de entrada não deve abrir para novos clientes (exceto para quem possui Tag de Acesso
# Rápido, pois estes têm vagas reservadas).
# 3: Ao chegar na cancela, o sistema deve verificar o tipo de acesso:
# 3.1: Via TAG (Sem Parar/ConectCar): * Verifique se a Tag está ativa. Se ativa, a cancela abre automaticamente e registra o horário de entrada vinculado ao ID
# da Tag.
# 3.2: Via Ticket (Botão): O cliente pressiona o botão, o sistema verifica se há vagas comuns disponíveis, se houver, imprime o ticket com a hora de entrada e abre a cancela.
# 4: O cálculo do valor a ser pago na saída segue as seguintes regras: Até 15 minutos: Grátis (Tolerância). Até 3 horas: Valor fixo de R$ 15,00. Hora adicional: R$ 3,00 por hora extra (ou fração). Clientes com TAG: Possuem 10% de desconto sobre o valor total.
# 5: Seu programa deve ser capaz de responder logicamente a estas perguntas: 1. Vaga Especial: Se o estacionamento comum lotar, como o sistema impede a entrada de novos
# tickets, mas permite a entrada de Tags? 2. Perca de Ticket: Se o cliente não tiver o ticket/registro, o sistema deve cobrar uma taxa fixa de R$
# 50,00. 3. Pagamento: A cancela de saída só abre se o status do ticket constar como "Pago".

# Sistema de estacionamento de shopping:
#RF - O sistema suporta 500 vagas.
#RNF - Contador de vagas ocupadas (verde é vazia e vermelho é ocupada)
#RF - Se estiver lotado, não abre (mensagem avisando que está lotado)
#RF - Vagas reservadas para Tag de acesso rápido
#RF - Verificar os tipos de acesso: TAG e Ticket
#RF - Calcular o valor pago na saída (Calcular o tempo)
#RF - Vaga especial
#RF - Em caso de perda, cobrar 50,00 (Dinheiro, cartão ou pix)
#RF - Cancela de saída só abre se o status do ticket constar como "Pago" (Dinheiro, cartão ou pix)