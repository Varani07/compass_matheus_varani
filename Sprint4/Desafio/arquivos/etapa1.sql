create table tb_combustivel (
	idCombustivel int primary key,
	tipo text(20) not null
);

--

create table tb_carro (
	idCarro int primary key,
	chassi text,
	marca text,
	modelo text,
	ano int,
	idCombustivel int,

	foreign key (idCombustivel) references tb_combustivel (idCombustivel) 
);

--

create table tb_pessoa (
	idPessoa int primary key auto_increment,
	nome text(60),
	estado text(45)
);

--

create table cliente (
	idCliente int primary key,
	idPessoa int,
	cidade text(45),
	pais text(45),

	foreign key (idPessoa) references tb_pessoa (idPessoa)
)

--

create table vendedor (
	idVendedor int primary key,
	idPessoa int,
	sexo smallint,

	foreign key (idPessoa) references tb_pessoa (idPessoa)
)

--

create table tb_locacao_migracao (
	idLocacao int primary key,
	dataLocacao datetime not null,
	horaLocacao time not null,
	dataEntrega datetime not null,
	horaEntrega time not null,
	qtdDiaria int,
	vlrDiaria decimal,
	idCarro int,
	kmCarro int,
	idCliente,
	idVendedor,

	foreign key (idCarro) references tb_carro (idCarro),
	foreign key (idCliente) references tb_cliente (idCliente),
	foreign key (idVendedor) references tb_vendedor (idVendedor)
)

--

insert into 
    tb_combustivel (idCombustivel, tipo) 
select 
    distinct tl.idcombustivel, tl.tipoCombustivel 
from tb_locacao tl;

--

insert into
    tb_carro (idCarro, chassi, marca, modelo, ano, idCombustivel)
select
    distinct tl.idCarro,
    tl.chassiCarro,
    tl.marcaCarro,
    tl.modeloCarro,
    tl.anoCarro,
    tl.idcombustivel
from tb_locacao tl;

--

insert into
    tb_pessoa (nome, estado)
select
    distinct nome,
    estado
from (
    select 
        tl_c.nomeCliente as nome,
        tl_c.estadoCliente as estado
    from tb_locacao as tl_c
    union all
    select
        tl_v.nomeVendedor as nome,
        tl_v.estadoVendedor as estado
    from tb_locacao as tl_v
);

--

insert into 
	tb_cliente (idCliente, idPessoa, cidade, pais)
select distinct
	tl.idCliente,
	tp.idPessoa,
	tl.cidadeCliente,
	tl.paisCliente
from tb_locacao tl
left join tb_pessoa tp 
	on tl.nomeCliente = tp.nome and tl.estadoCliente = tp.estado;

--

insert into 
	tb_vendedor (idVendedor, idPessoa, sexo)
select distinct
	tl.idVendedor,
	tp.idPessoa,
	tl.sexoVendedor
from tb_locacao tl 
left join tb_pessoa tp 
	on tl.nomeVendedor = tp.nome and tl.estadoVendedor = tp.estado;

--

insert into 
	tb_locacao_migracao (idLocacao, dataLocacao, horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria, idCarro, kmCarro, idCliente, idVendedor)
select 
	tl.idLocacao,
	tl.dataLocacao,
	tl.horaLocacao,
	tl.dataEntrega,
	tl.horaEntrega,
	tl.qtdDiaria,
	tl.vlrDiaria,
	tl.idCarro,
	tl.kmCarro,
	tl.idCliente,
	tl.idVendedor
from tb_locacao tl;