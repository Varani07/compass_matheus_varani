select
    (select count(*) from livro where editora = edi.codEditora) as quantidade,
    edi.nome,
    ende.estado,
    ende.cidade
from editora as edi
left join endereco as ende
    on edi.endereco = ende.codEndereco
where quantidade > 0
order by quantidade desc
limit 5;