select 
    cdpro, 
    nmpro
from tbvendas as vendas 
group by cdpro, nmpro
order by (select sum(qtd) from tbvendas where cdpro = vendas.cdpro and ((dtven between '2014-02-03' and '2018-02-02')) and status = 'Concluído') desc
limit 1;