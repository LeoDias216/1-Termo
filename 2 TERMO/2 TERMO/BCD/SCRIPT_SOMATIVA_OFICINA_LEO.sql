Create database if not exists Somativa_Oficina_Leo;
Use Somativa_Oficina_Leo;

Create Table if not exists Clientes (
Id_cliente Int auto_increment primary key,
Nome varchar(60) not null,
CPF varchar(14) not null unique,
Data_nasc date not null,
Endereco varchar(60) not null,
Numero varchar(12) not null
);

Create Table if not exists Veiculos (
Id_veiculo int auto_increment primary key,
Tipo enum("Carro", "Moto") not null,
Marca varchar(30) not null,
Modelo varchar(30) not null,
Peso float not null,
Status_veiculo enum("Ativo", "Inativo") default "Ativo"
);

Create Table if not exists Marcas (
Id_marca int auto_increment primary key,
Nome varchar(30) not null,
Fabricante varchar(30) not null,
Ano_lancamento char(4),
Localizacao char(30) not null,
Modelo_mais_famoso varchar(60) not null
);

Create Table if not exists Modelos (
Id_modelo int auto_increment primary key,
Nome varchar(30) not null,
Tipo enum("Carro", "Moto") not null,
Maior_fabricante varchar(30) not null,
Peso float not null,
Ano_lancamento char(4) not null
);

Create Table if not exists Funcionarios (
Id_funcionario int auto_increment primary key,
Nome varchar(60) not null,
Data_nasc date not null,
CPF varchar(14) not null unique,
Salario decimal(5,2) not null,
Cargo varchar(30) not null
);

Create Table if not exists Servicos (
Id_servico int auto_increment primary key,
Tipo varchar(60) not null,
Preco decimal(4,2) not null,
Tempo_estimado date not null,
Peca_utilizada varchar(60) not null,
Garantia date not null
);

Create Table if not exists Ordens_de_servico (
Id_ordem int auto_increment primary key,
Nome varchar(60) not null,
Veiculo varchar(30) not null,
Servico varchar(80) not null,
Preco decimal(4,2) not null,
Tempo_estimado date not null
);

Create Table if not exists Pecas (
Id_peca int auto_increment primary key,
Nome varchar(30) not null,
Peso float not null,
Tipo varchar(30) not null,
Material varchar(30) not null,
Carro_mais_usado varchar(60)
);

Create Table if not exists Pagamentos (
Id_pagamento int auto_increment primary key,
Nome varchar(60) not null,
CPF varchar(14) not null,
Valor decimal(5,2) not null,
Desconto varchar(10),
Tipo enum("Debito", "Credito", "Pix") default "Credito"
);

Create Table if not exists Fornecedores (
Id_fornecedor int auto_increment primary key,
Nome varchar(30) not null,
Peca_entregue varchar(30) not null,
Preco decimal(5,2) not null,
Tempo_entrega date not null,
Localizacao char(30) not null
);

-- Parte 03: 

Alter Table Clientes Add teste Varchar(100);
Alter Table Clientes Drop Column teste;

Alter Table Veiculos Add teste Varchar(100);
Alter Table Veiculos Drop Column teste;

Alter Table Marcas Add teste Varchar(100);
Alter Table Marcas Drop Column teste;

Alter Table Modelos Add teste Varchar(100);
Alter Table Modelos Drop Column teste;

Alter Table Funcionarios Add teste Varchar(100);
Alter Table Funcionarios Drop Column teste;

Alter Table Servicos Add teste Varchar(100);
Alter Table Servicos Drop Column teste;

Alter Table Ordens_de_servico Add teste Varchar(100);
Alter Table Ordens_de_servico Drop Column teste;

Alter Table Pecas Add teste Varchar(100);
Alter Table Pecas Drop Column teste;

Alter Table Pagamentos Add teste Varchar(100);
Alter Table Pagamentos Drop Column teste;

Alter Table Fornecedores Add teste Varchar(100);
Alter Table Fornecedores Drop Column teste;

rename table Modelos to Modelos_fab