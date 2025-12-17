select
    dep.cddep,
    dep.nmdep,
    dep.dtnasc,
    sum(vendas.qtd*vendas.vrunt) as valor_total_vendas
from tbvendedor as vendedor 
left join tbvendas as vendas 
    on vendedor.cdvdd = vendas.cdvdd
left join tbdependente as dep 
    on vendedor.cdvdd = dep.cdvdd
where vendas.status = 'Concluído'
group by 
    dep.cddep,
    dep.nmdep,
    dep.dtnasc
having sum(vendas.qtd*vendas.vrunt) <> 0
order by valor_total_vendas
limit 1;