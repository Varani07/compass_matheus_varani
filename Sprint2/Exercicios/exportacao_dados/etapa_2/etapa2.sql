select
    e.codEditora as CodEditora,
    e.nome as NomeEditora,
    (select count(*) from livro where e.codEditora = editora) as QuantidadeLivros
from editora as e
order by QuantidadeLivros desc
limit 5;