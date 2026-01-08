idCliente
nomeCliente 
cidadeCliente
estadoCliente
paisCliente

idCarro
kmCarro
chassiCarro
marcaCarro
modeloCarro
anoCarro

idcombustivel
tipoCombustivel

idLocacao
dataLocacao
horaLocacao
qtdDiaria
vlrDiaria
dataEntrega
horaEntrega

idVendedor
nomeVendedor 
sexoVendedor
estadoVendedor

-- relacional

-- pessoa
idPessoa::int
nome::varchar(60)
estado::varchar(45)

-- cliente
idCliente::int
idPessoa::int (pessoa)
cidade::varchar(45)
pais::varchar(45)

-- vendedor
idVendedor::int
idPessoa::int (pessoa)
sexo::char

-- combustivel
idCombustivel::int 
tipo::varchar(20)

-- carro
idCarro::int 
chassi::varchar(45)
marca::varchar(45)
modelo::varchar(45)
ano::int
idCombustivel::int (carro)

-- locacao
idLocacao::int
dataLocacao::datetime
horaLocacao::time
dataEntrega::datetime
horaEntrega::time
qtdDiaria::int
vlrDiaria::decimal
idCarro::int (carro)
kmCarro::int
idCliente::int (cliente)
idVendedor::int (vendedor)


-- dimensional

-- cliente
idCliente::int
nomeCliente::varchar(60)
cidade::varchar(45)
estadoCliente::varchar(45)
pais::varchar(45)

-- vendedor
idVendedor::int
nomeVendedor::varchar(60)
sexo::char
estadoVendedor::varchar(45)

-- carro
idCarro::int 
chassi::varchar(45)
marca::varchar(45)
modelo::varchar(45)
ano::int
tipoCombustivel::varchar(20)

-- locacao
idLocacao::int
dataLocacao::datetime
horaLocacao::time
dataEntrega::datetime
horaEntrega::time
qtdDiaria::int
vlrDiaria::decimal
idCarro::int (carro)
kmCarro::int
idCliente::int (cliente)
idVendedor::int (vendedor)