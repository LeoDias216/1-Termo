-- PROJETO SMARTCOFFEE LEONARDO

-- CRIAR BANCO DE DADOS
-- ATIVAR BANCO DE DADOS
-- CRIAR TABELAS

-- OPCIONAIS NO DIA 21/08/2026
-- INSERIR DADOS
-- CONSULTAR DADOS

Create Database if not exists SmartCoffee_Leonardo;

Use SmartCoffee_Leonardo;

Create Table If Not Exists Clientes (
Id_cliente int auto_increment primary key,
Nome varchar(60) not null,
Numero varchar(12) not null,
CPF varchar(14) not null unique,
Endereço varchar(80) not null,
Data_nascimento date not null,
Email varchar(30),
Status_cliente enum("Ativo", "Inativo") default "Ativo"
);

Create Table If Not Exists Pedidos (
Id_pedido int auto_increment primary key,
Nome varchar(60) not null,
Produtos varchar(80) not null,
Preço decimal(4,2) not null,
Data_realização timestamp default current_timestamp,
Quantidade int not null,
Status_pedido enum("Ativo", "Inativo") default "Inativo"
);

Create Table If Not Exists Pagamento (
Id_pagamento int auto_increment primary key,
Valor decimal(4,2) not null,
CPF varchar(14) not null unique,
Data_pagamento timestamp default current_timestamp,
Status_pagamento enum ("Ativo", "Inativo") default "Inativo",
Forma_pagamento enum ("Debito", "Credito", "Pix") default "Credito"
);

Create Table If Not Exists Produtos (
Id_produto int auto_increment primary key,
Nome_produto varchar(60) not null,
Tipo varchar(30) not null,
Preço decimal(3,2) not null,
Quantidade int not null,
Validade date not null
);

Create Table If Not Exists Funcionarios (
Id_funcionario int auto_increment primary key,
Nome varchar(60) not null,
Data_nascimento date not null,
Numero varchar(12) not null,
Endereço varchar(80) not null,
Cargo varchar(20) not null,
Salario decimal(5,2) not null
);

Create Table If Not Exists Programa_fidelidade (
Id_programa_fidelidade int auto_increment primary key,
Nome varchar(60) not null,
CPF varchar(14),
Pontos int not null,
Hist_compras timestamp default current_timestamp,
Validade date not null
);

Create Table If Not Exists Delivery (
Id_delivery int auto_increment primary key,
Nome varchar(60) not null,
CPF varchar(14) not null unique,
Produtos varchar(80) not null,
Quantidade int not null,
Preço decimal(5,2) not null,
Data_delivery date not null,
Status_delivery enum ("Ativo", "Inativo")
);

Create Table If Not Exists Estoque (
Id_estoque int auto_increment primary key,
Nome_produto varchar(60) not null,
Tipo varchar(30) not null,
Quantidade int not null,
Hist_entrada_saida timestamp default current_timestamp,
Fornecedor varchar(60) not null
);

Create Table If Not Exists Categoria (
Id_categoria int auto_increment primary key,
Nome_produto varchar(60) not null,
Produtos varchar(80) not null,
Quantidade int not null,
Preço decimal(3,2) not null,
Validade date not null
);

Create Table If Not Exists Fornecedor (
Id_fornecedor int auto_increment primary key,
Empresa varchar(60) not null,
Produto varchar(80) not null,
Quantidade int not null,
Preço decimal(5,2) not null,
Localização varchar(80) not null
);