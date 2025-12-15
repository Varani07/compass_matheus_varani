select
    codAutor,
    nome,
    (select count(*) from livro where codAutor = autor) as quantidade_publicacoes
from autor
group by codAutor, nome
order by quantidade_publicacoes desc
limit 1;