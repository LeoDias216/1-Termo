-- COMANDOS PARA CRIAR BD
-- 1
Create Database Clinica_Medica_Keynan;
Create Database If Not Exists Clinica_Medica_Keynan;

Create Database Banco_dados;

-- ATIVAR BD E ATUALIZAR SCHEMAS
-- 2
Use Clinica_Medica_Keynan;

-- CRIAR TABELAS
-- 3
Create Table If Not Exists Pacientes (
Id_paciente Int Auto_increment Primary key,
Nome_paciente Varchar(60) Not null,
CPF Varchar(14) Not null Unique,
Data_nascimento Date Not null,
Email Varchar(100),
Telefone Varchar(15),
Convenio Enum ('Sim', 'Não') Not null
);

Create Table If Not Exists Funcionarios (
Id_funcionario Int Primary key,
Nome_funcionario Varchar(60) Not null,
CPF Varchar(14) Not null Unique,
Telefone Varchar(15),
Salario Decimal(5,2) Default 0.00
);

-- ALTERAR INFORMAÇÕES DA TABELA
-- ALTER TABLE
-- ADICIONAR UM CAMPO (ATRIBUTO) OU COLUNA NA TABELA
Alter Table Funcionarios Add Email Varchar(100) Not null;

-- ALTERAR TIPO DE DADOS DE CAMPO (ATRIBUTO) OU COLUNA NA TABELA
Alter Table Funcionarios Modify Email Varchar(50) Not null;

-- APAGAR O CAMPO (ATRIBUTO) OU COLUNA NA TABELA
Alter Table Funcionarios Drop Column Email;

-- RENOMEAR TABELAS
Rename Table Funcionarios To Funcionarioss;
Rename Table Funcionarioss To Funcionarios;

-- ---------------------------------------------------------------

-- USAR COM RESPONSABILIDADE !
-- APAGAR DADOS DA TABELA
Truncate Table Funcionarios;

-- APAGAR BD
Drop Database Clinica_Medica_Keynan;

-- APAGAR TABELAS
Drop Tables Funcionarios;

-- MOSTRAR TABELAS NO BD
Show Tables;

-- ---------------------------------------------------------------

-- INSERIR DADOS NO BD
Insert Into Funcionarios (Id_funcionario,Nome_funcionario,CPF,Telefone,Salario)
Values (2,'Carlos Magnum','125.436.781-92','(19)92220-2220','999');

Insert Into Pacientes (Id_paciente,Nome_paciente,CPF,Data_nascimento,Email,Telefone,Convenio)
Values (Default,'Jessica Cruz','123.321.331.35','1990-10-30','jesscruz@lj.br','(19)98711-6163',Default);
-- PADRÃO PARA DATA: ANO-MÊS-DIA

-- MOSTRAR TODOS OS BD
Show Databases;

-- CONSULTAR DADOS NO BD
Select * From Funcionarios,Pacientes

