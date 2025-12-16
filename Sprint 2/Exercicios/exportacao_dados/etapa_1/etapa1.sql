select
    l.cod as CodLivro,
    l.titulo as Titulo,
    a.codAutor as CodAutor,
    a.nome as NomeAutor,
    l.valor as Valor,
    e.codEditora as CodEditora,
    e.nome as NomeEditora
from livro as l 
left join autor as a 
    on l.autor = a.codAutor
left join editora as e 
    on l.editora = e.codEditora
order by Valor desc
limit 10;