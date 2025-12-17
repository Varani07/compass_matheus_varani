select
    vdd.nmvdd as vendedor,
    (select sum(qtd*vrunt) from tbvendas where status = 'Concluído' and cdvdd = vdd.cdvdd) as valor_total_vendas,
    round(((select sum(qtd*vrunt) from tbvendas where status = 'Concluído' and cdvdd = vdd.cdvdd)*vdd.perccomissao)/100, 2) as comissao
from tbvendedor as vdd
order by comissao desc;