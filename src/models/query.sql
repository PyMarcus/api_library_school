
-- criacao do banco
create database Biblio;

-- selecao do banco
use Biblio;


-- criação de tabelas

create table Aluno(
	matricula integer auto_increment not null unique,
    nome varchar(60) not null,
    email varchar(60),
    data_nascimento date not null,
    primary key (matricula)
) default charset=utf8;

describe Aluno;

create table Livros(
	registro integer not null auto_increment unique,
    matricula_aluno integer,
    status enum('Disponível', 'Indisponível') not null,

    foreign key(matricula_aluno) references Aluno (matricula),
    primary key(registro)
) default charset=utf8;


describe Livros;
alter table Livros add column nome varchar(30) not null;

-- populando a tabela

insert into
	Aluno
values
 (default, 'Aluno1', 'aluno1@gmail.com', '2000-02-01');

insert into
	Aluno
values
 (default, 'Aluno2', 'aluno1@gmail.com', '2000-02-01'),
 (default, 'Aluno3', 'aluno3@gmail.com', '2001-02-01'),
 (default, 'Aluno4', 'aluno4@gmail.com', '2002-02-01'),
 (default, 'Aluno5', 'aluno5@gmail.com', '2003-02-01'),
 (default, 'Aluno6', 'aluno6@gmail.com', '2004-02-01');

-- checando os dados:
select * from Aluno;


-- Populando livro
insert into
	Livros
values
	(default, 1, 'Indisponível', 'Os 3 porquinhos');

insert into
	Livros
values
	(default, 1, 'Indisponível', 'Os 2 porquinhos'),
    (default, 2, 'Indisponível', 'Os 44 porquinhos'),
    (default, 3, 'Indisponível', 'Os 25 porquinhos'),
    (default, null, 'Disponível', 'Os 232 porquinhos'),
    (default, null, 'Disponível', 'Os 251 porquinhos');

-- checando os dados:
select * from Livros order by matricula_aluno, nome;


select * from Aluno as A left join Livros as L on L.matricula_aluno = A.matricula;