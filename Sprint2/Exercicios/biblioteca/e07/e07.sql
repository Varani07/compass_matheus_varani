select
    nome
from autor
where (select count(*) from livro where autor = codAutor) = 0
order by nome;