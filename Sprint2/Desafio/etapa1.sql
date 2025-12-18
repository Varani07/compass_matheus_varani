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