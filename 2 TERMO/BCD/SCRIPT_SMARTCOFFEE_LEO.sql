-- PROJETO SMARTCOFFEE LEONARDO

-- CRIAR BANCO DE DADOS
-- ATIVAR BANCO DE DADOS
-- CRIAR TABELAS

-- OPCIONAIS NO DIA 21/08/2026
-- INSERIR DADOS
-- CONSULTAR DADOS

Create Database SmartCoffee_Leonardo;

Use SmartCoffee_Leonardo;

Create Table If Not Exists Clientes (
Id_cliente
Nome
Numero
CPF
Endereço
Data_nascimento
Email
Status_cliente
);

Create Table If Not Exists Pedidos (
Id_pedido
Nome
Produtos
Preço
Data_realização
Quantidade
Status_pedido
);

Create Table If Not Exists Pagamento (
Id_pagamento
Valor
CPF
Data_pagamento
Status_pagamento
Forma_pagamento
);

Create Table If Not Exists Produtos (
Id_produto
Produto
Tipo
Preço
Quantidade
Validade
);

Create Table If Not Exists Funcionarios (
Id_funcionario
Nome
Data_nascimento
Numero
Endereço
Cargo
Salario
);

Create Table If Not Exists Programa_fidelidade (
Id_cliente
Nome
CPF
Pontos
Hist_compras
Validade
);

Create Table If Not Exists Delivery (
Id_delivery
Nome
CPF
Produto
Quantidade
Preço
Data_delivery
Status_delivery
);

Create Table If Not Exists Estoque (
Id_estoque
Produto
Tipo
Quantidade
Hist_entrada_saida
Localização
);

Create Table If Not Exists Categoria (
Id_categoria
Nome
Produtos
Quantidade
Preço
Validade
);

Create Table If Not Exists Fornecedor (
Id_fornecedor
Empresa
Produto
Quantidade
Preço
Localização
);