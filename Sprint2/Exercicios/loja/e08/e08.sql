select
    cdvdd,
    nmvdd
from tbvendedor as vendedor
order by (select count(*) from tbvendas where cdvdd = vendedor.cdvdd and status = 'Concluído') desc
limit 1;