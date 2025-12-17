select
    ven.cdcli,
    ven.nmcli,
    (select sum(qtd*vrunt) from tbvendas where cdcli = ven.cdcli and status = 'Concluído') as gasto
from tbvendas as ven
order by gasto desc
limit 1;