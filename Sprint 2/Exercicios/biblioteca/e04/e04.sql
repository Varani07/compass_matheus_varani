select
    nome,
    codAutor,
    nascimento,
    (select count(*) from livro where autor = codAutor) as quantidade
from autor
order by replace(nome, 'Á', 'A');