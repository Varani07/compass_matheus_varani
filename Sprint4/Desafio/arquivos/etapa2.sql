create view dim_cliente as
select 
	tc.idCliente,
	tp.nome,
	tc.cidade,
	tp.estado,
	tc.pais
from tb_cliente tc 
left join tb_pessoa tp 
	on tc.idPessoa = tp.idPessoa;

--

create view dim_vendedor as 
select 
	tv.idVendedor,
	tp.nome,
	tp.estado,
	tv.sexo
from tb_vendedor tv  
left join tb_pessoa tp 
	on tv.idPessoa = tp.idPessoa;

--

create view dim_carro as
select 
	tc.idCarro,
	tc.chassi,
	tc.marca,
	tc.modelo,
	tc.ano,
	tcb.tipo as tipoCombustivel
from tb_carro tc 
left join tb_combustivel tcb 
	on tc.idCombustivel = tcb.idCombustivel;

--

create view fato_locacao as
select 
	tlm.idLocacao,
	tlm.dataLocacao,
	tlm.horaLocacao,
	tlm.dataEntrega,
	tlm.horaEntrega,
	tlm.qtdDiaria,
	tlm.vlrDiaria,
	tlm.idCarro,
	tlm.kmCarro,
	tlm.idCliente,
	tlm.idVendedor
from tb_locacao_migracao tlm;