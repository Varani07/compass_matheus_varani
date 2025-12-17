select
    cod,
    titulo,
    autor,
    editora,
    valor,
    publicacao,
    edicao,
    idioma
from livro
where publicacao >= '2015-01-01'
order by cod;