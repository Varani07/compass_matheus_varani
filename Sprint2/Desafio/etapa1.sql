create table 
    combustivel (
        idCombustivel int primary key, tipo varchar
        );

insert into 
    combustivel (idCombustivel, tipo) 
select 
    distinct idcombustivel, tipoCombustivel 
from tb_locacao tl;