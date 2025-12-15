with estado_editora as (
    select
        edi.codEditora as id_editora,
        case
            when ende.estado in ('RIO GRANDE DO SUL', 'PARANÁ') then false
            else true end as regiao_certa
    from editora as edi
    left join endereco as ende
        on edi.endereco = ende.codEndereco
)

select
    distinct aut.nome
from livro as liv
left join autor as aut
    on liv.autor = aut.codAutor
left join estado_editora as es_edi 
    on liv.editora = id_editora 
where es_edi.regiao_certa
order by aut.nome;