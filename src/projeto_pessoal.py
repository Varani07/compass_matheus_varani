import os

from .validacao import Validacao, ValidationError
from .util import ToolBox as tb
from ..service import Service
from .livro import Livro
from .calendario import Calendario

from datetime import datetime, date
from zoneinfo import ZoneInfo

from collections import Counter
from decimal import Decimal

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.box import ASCII

from ..jogos import JogoTeste

class Interface():
    def __init__(self, tipo_interface: str, titulo: str, alvo: str = "geral", acao: str = "", db_info: list = [], id: int = 0, dia_diario: str = ''): 

        self.console = Console()     

        self.db_info = db_info
        self.acao = acao
        self.alvo = alvo
        self.tipo_interface = tipo_interface

        self.titulo = titulo.upper()
        
        self.respostas = {}
        self.lista_de_opcoes = []
        self.ids_disponiveis = set()

        self.info = ""
        self.selected_info_answer = ""
        self.id = int(id)
        self.running = True
        self.retornar = False
        self.livro = None

        self.validator = Validacao().validar

        if self.alvo == 'diario':
            self.calendario = Calendario('dia')
            if dia_diario != '':
                self.calendario.mudar_data(dia_diario)

            self.calendario.atualizar

        if acao != "" and acao != 'freeway':
            self.lista_de_opcoes = self.montar_opcoes(acao=acao, alvo=alvo)

        self.db_tags = {
            "pessoa": {
                "Nome": "nome",
                "Sobrenome": "sobrenome",
                "Apelido": "apelido",
                "Data de nascimento": "data_nascimento",
                "Nos conhecemos quando": "primeiro_dia",
                "Parentesco": "parentesco",
                "Proximidade": "proximidade",
                "Descricao": "descricao",
                "ID": "id"
            },
            "nota": {
                "Conteudo": "nota",
                "ID": "id"
            },
            "manga": {
                "ID": "id",
                "Nome": "nome",
                "Status": "status_atual",
                "Capitulo": "capitulo",
                "Pagina": "pagina",
                "Avaliacao": "avaliacao"
            },
            "jogo": {
                "ID": "id",
                "Nome": "nome",
                "Status": "status_atual",
                "Avaliacao": "avaliacao"
            },
            "serie": {
                "ID": "id",
                "Nome": "nome",
                "Status": "status_atual",
                "Temporada": "temporada",
                "Episodio": "episodio",
                "Tempo": "tempo",
                "Avaliacao": "avaliacao"
            },
            "filme": {
                "ID": "id",
                "Nome": "nome",
                "Status": "status_atual",
                "Tempo": "tempo",
                "Avaliacao": "avaliacao"
            },
            "anime": {
                "ID": "id",
                "Nome": "nome",
                "Status": "status_atual",
                "Temporada": "temporada",
                "Episodio": "episodio",
                "Tempo": "tempo",
                "Avaliacao": "avaliacao"
            },
            "contato": {
                "Contato": "contato",
                "Tipo": "tipo",
                "Pessoa": "pessoa"
            },
            "gosto": {
                "Gosto": "gosto",
                "Pessoa": "pessoa"
            },
            "afazer": {
                "Atividade": "atividade",
                "Data": "data_da_atividade",
                "Data final": "data_fim_atividade",
                "Tempo": "tempo_da_atividade",
                "ID": "id",
                "Repetir": "repetir",
                "Status": "ativa"
            },
            "banda": {
                "ID": "id",
                "Nome": "nome",
                "Status": "status_atual"
            },
            "album": {
                "ID": "id",
                "Nome": "nome",
                "Tipo": "formato",
                "Banda": "banda",
                "Ano de lancamento": "ano_lancamento"
            },
            "musica": {
                "ID": "id",
                "Nome": "nome",
                "Album": "album",
                "Pessoa que recomendou": "pessoa",
                "Status": "status_atual",
                "Letra": "letra"
            }
        }

        self.requisitos_dados = {
            "pessoa": {
                "nome": "Não deve ser vazio, máximo 50 caracteres.",
                "sobrenome": "Não deve ser vazio, máximo 50 caracteres.",
                "apelido": "Não deve ser vazio, máximo 40 caracteres.",
                "data de nascimento": "07092001 ou 07/09/2001.",
                "nos conhecemos quando": "07092001 ou 07/09/2001.",
                "descricao": "Não deve ser vazio.",
                "id": "Deve ser um ID válido.",
                "idade": "Não deve ser vazio, precisa ser um número inteiro positivo."
            },
            "nota": {
                "conteudo": "Não deve ser vazio.",
                "id": "Deve ser um ID válido."
            },
            "manga": {
                "id": "Deve ser um ID válido.",
                "nome": "Não deve ser vazio, máximo 40 caracteres.",
                "capitulo": "Deve ser um número positivo maior que zero com no máximo uma casa decimal depois do ponto.",
                "pagina": "Deve ser um número inteiro positivo maior que zero.",
                "avaliacao": "Deve ser um número de 0 até 10."
            },
            "jogo": {
                "id": "Deve ser um ID válido.",
                "nome": "Não deve ser vazio, máximo 50 caracteres.",
                "avaliacao": "Deve ser um número de 0 até 10."
            },
            "serie": {
                "id": "Deve ser um ID válido.",
                "nome": "Não deve ser vazio, máximo 40 caracteres.",
                "temporada": "Deve ser um número inteiro positivo maior que zero.",
                "episodio": "Deve ser um número inteiro positivo maior que zero.",
                "tempo": "Deve estar neste formato 07:17:20 (H:M:S).",
                "avaliacao": "Deve ser um número de 0 até 10."
            },
            "filme": {
                "id": "Deve ser um ID válido.",
                "nome": "Não deve ser vazio, máximo 40 caracteres.",
                "tempo": "Deve estar neste formato 07:17:20 (H:M:S).",
                "avaliacao": "Deve ser um número de 0 até 10."
            },
            "anime": {
                "id": "Deve ser um ID válido.",
                "nome": "Não deve ser vazio, máximo 40 caracteres.",
                "temporada": "Deve ser um número inteiro positivo maior que zero.",
                "episodio": "Deve ser um número inteiro positivo maior que zero.",
                "tempo": "Deve estar neste formato 07:17:20 (H:M:S).",
                "avaliacao": "Deve ser um número de 0 até 10."
            },
            "contato": {
                "contato": "Não deve ser vazio, máximo 40 caracteres."
            },
            "gosto": {
                "gosto": "Não deve ser vazio, máximo 100 caracteres."
            },
            "afazer": {
                "id": "Deve ser um ID válido.",
                "atividade": "Não deve ser vazio, máximo 100 caracteres.",
                "data": "07092001 ou 07/09/2001.",
                "data final": "07092001 ou 07/09/2001.",
                "tempo": "Deve estar neste formato 07:17 (H:M)."
            },
            "calendario": {
                "data": "Deve estar no seguinte formato: mes/ano | 07/2025"
            },
            "banda": {
                "id": "Deve ser um ID válido.",
                "nome": "Não deve ser vazio, máximo 50 caracteres."
            },
            "album": {
                "id": "Deve ser um ID válido.",
                "nome": "Não deve ser vazio, máximo 50 caracteres.",
                "ano de lancamento": "Deve estar entre 1901 e o ano atual."
            },
            "musica": {
                "id": "Deve ser um ID válido.",
                "nome": "Não deve ser vazio, máximo 50 caracteres.",
                "letra": "Não deve ser vazio."
            }
        }

        self.indice_da_avaliacao = {
            "manga": 5,
            "jogo": 3,
            "serie": 6,
            "anime": 6,
            "filme": 4,
            "album": 4
        }
        
        self.tabelas = {
            "pessoa": "pessoas",
            "nota": "notas",
            "manga": "mangas",
            "jogo": "jogos",
            "serie": "series",
            "anime": "animes",
            "filme": "filmes",
            "contato": "contatos",
            "gosto": "gostos",
            "afazer": "afazeres",
            "banda": "bandas",
            "album": "albuns",
            "musica": "musicas"
        }

        self.tabelas_alternativas = {
            "nota": "pessoas_notas",
            "afazer": "pessoas_afazeres"
        }

    @property
    def repassar_respostas(self):
        if len(self.db_info) > 0:
            self.respostas = {key: [None, i] for i, key in enumerate(self.lista_de_opcoes, 1)}
            self.id = int(self.db_info[0])

            match self.alvo:
                case 'nota':
                    for key in self.respostas.keys():
                        if key == 'Conteudo*':
                            self.respostas[key][0] = self.db_info[1]
                        elif key == 'Pessoas citadas*':
                            self.respostas[key][0] = self.db_info[3][:]

                case _:
                    for i, key in enumerate(self.respostas.keys(), 1):
                        if isinstance(self.db_info[i], list):
                            self.respostas[key] = [self.db_info[i][:], i]
                        else:
                            self.respostas[key] = [self.db_info[i], i]
                        if len(self.db_info)-1 == i:
                            break

    def montar_opcoes(self, alvo: str, acao: str) -> list:
        opcoes = []

        dicionario = {
            "pessoa": {
                "pesquisar": ['ID', 'Nome', 'Sobrenome', 'Apelido', 'Idade', 'Parentesco', 'Proximidade'],
                "gerenciar": ['Notas', 'Contatos', 'Afazeres', 'Gostos', 'Recomendacoes de musicas'],
                "adicionar": ["Nome*", "Sobrenome", "Apelido*", "Data de nascimento*", "Nos conhecemos quando", "Parentesco*", "Proximidade*", "Descricao*"]
            },
            "nota": {
                "pesquisar": ['ID', 'Conteudo'],
                "gerenciar": [],
                "adicionar": ["Conteudo*", "Pessoas citadas*", "Remover pessoa"]
            },
            "manga": {
                "pesquisar": ['ID', 'Nome', 'Status', 'Avaliacao', 'Avaliacao Crescente', 'Avaliacao Decrescente', 'Nao avaliados'],
                "gerenciar": [],
                "adicionar": ["Nome*", "Status*", "Capitulo", "Pagina", "Avaliacao"]
            },
            "jogo": {
                "pesquisar": ['ID', 'Nome', 'Status', 'Avaliacao', 'Avaliacao Crescente', 'Avaliacao Decrescente', 'Nao avaliados'],
                "gerenciar": [],
                "adicionar": ["Nome*", "Status*", "Avaliacao"]
            },
            "filme": {
                "pesquisar": ['ID', 'Nome', 'Status', 'Avaliacao', 'Avaliacao Crescente', 'Avaliacao Decrescente', 'Nao avaliados'],
                "gerenciar": [],
                "adicionar": ["Nome*", "Status*", "Tempo", "Avaliacao"]
            },
            "serie": {
                "pesquisar": ['ID', 'Nome', 'Status', 'Temporada', 'Episodio', 'Avaliacao', 'Avaliacao Crescente', 'Avaliacao Decrescente', 'Nao avaliados'],
                "gerenciar": [],
                "adicionar": ["Nome*", "Status*", "Temporada", "Episodio", "Tempo", "Avaliacao"]
            },
            "anime": {
                "pesquisar": ['ID', 'Nome', 'Status', 'Temporada', 'Episodio', 'Avaliacao', 'Avaliacao Crescente', 'Avaliacao Decrescente', 'Nao avaliados'],
                "gerenciar": [],
                "adicionar": ["Nome*", "Status*", "Temporada", "Episodio", "Tempo", "Avaliacao"]
            },
            "contato": {
                "pesquisar": ['Tipo', 'Contato'],
                "gerenciar": [],
                "adicionar": ["Tipo*", "Contato*", "Pessoa*"]
            },
            "gosto": {
                "pesquisar": ['Gosto'],
                "gerenciar": [],
                "adicionar": ["Gosto*", "Pessoa*"]
            },
            "afazer": {
                "pesquisar": ['ID', 'Atividade', 'Repetir', 'Status'],
                "gerenciar": [],
                "adicionar": ["Atividade*", "Data", "Data final", "Tempo", "Repetir", "Status*", "Pessoas citadas*", "Remover pessoa"]
            },
            "banda": {
                "pesquisar": ['ID', 'Nome', 'Status'],
                "gerenciar": ['Albuns'],
                "adicionar": ["Nome*", "Status*"]
            },
            "album": {
                "pesquisar": ['ID', 'Nome', 'Tipo', 'Banda', 'Ano de lancamento', 'Ano Crescente', 'Ano Decrescente'],
                "gerenciar": ['Musicas'],
                "adicionar": ["Nome*", "Tipo*", "Banda*", "Ano de lancamento*"]
            },
            "musica": {
                "pesquisar": ['ID', 'Nome', 'Album', 'Pessoa que recomendou', 'Status'],
                "gerenciar": ['Letra'],
                "adicionar": ["Nome*", "Album*", "Pessoa que recomendou", "Status*", "Letra"]
            }
        }
        # "pesquisar": [],
        # "gerenciar": [],
        # "adicionar": []

        if acao == "pesquisar" or acao == "pescar":
            opcoes += ['Ver Tudo']
        elif acao == "gerenciar":
            opcoes += ['Alterar', 'Deletar']

        if acao == 'adicionar' or acao == 'alterar':
            opcoes += dicionario[alvo]['adicionar']
            opcoes += [f"{acao.capitalize()} {self.alvo.capitalize()}"]
        elif acao == 'pesquisar' or acao == 'pescar':
            opcoes += dicionario[alvo]['pesquisar']
        elif acao != 'deletar':
            opcoes += dicionario[alvo][acao]

        return opcoes
    
    def inserir_opcoes(self, opcoes: list) -> None:
        self.lista_de_opcoes = opcoes
        
    def montar(self) -> int | str | None:
        os.system('cls')

        while self.running:
            if self.tipo_interface == "op_num":
                info = self.opcoes_numericas()

            elif self.tipo_interface == "preencher":
                info = self.preencher()

            elif self.tipo_interface == "get_info":
                info = self.get_info()
            
            elif self.tipo_interface == "get_info_op":
                info = self.get_info_op()
            
            elif self.tipo_interface == "ver_info":
                info = self.ver_info()

            elif self.tipo_interface == "selected_info":
                info = self.get_selected_info()

            elif self.tipo_interface == "escolhas":
                info = self.escolhas()

            elif self.tipo_interface == "ver_calendario":
                info = self.ver_calendario()

            elif self.tipo_interface == "ver_diario":
                info = self.ver_diario()

            if self.retornar:
                return info

# ------------------
 
    def opcoes_numericas(self) -> None:
        print(f"\n{self.titulo}\n{self.info}\n")
        count = 1
        choices = []

        if len(self.db_info) > 0 and self.livro == None:
            self.livro = Livro(self.tabelas[self.alvo].capitalize())
            self.livro.adicionar_conteudo([tb.montar_info(tuple(self.db_info), self.alvo)])
        
        if self.livro is not None:
            self.livro.mostrar_pagina

        for opcao in self.lista_de_opcoes:
            print(f"[{count}] {opcao}")
            count += 1
            choices.append(opcao)

        answer = input("\n\nEscolha: ")
        os.system('cls')

        try:
            num = int(answer)

            if num in range(1, len(self.lista_de_opcoes)+1):
                if self.acao != "":
                    if self.acao == 'pesquisar':
                        Interface(tipo_interface='ver_info', titulo=choices[num - 1], alvo=self.alvo, id=self.id).montar()

                    elif self.acao == 'pescar':
                        tupla_com_id = Interface(tipo_interface='ver_info', titulo=choices[num - 1], alvo=self.alvo, acao=self.acao).montar()
                        self.retornar = True
                        return tupla_com_id
                    
                    elif self.acao == 'gerenciar':
                        match choices[num - 1]:
                            case 'Alterar':
                                nova_interface = Interface(tipo_interface='preencher', titulo=f"alterar {self.alvo}", alvo=self.alvo, acao='alterar', db_info=self.db_info)
                                nova_interface.repassar_respostas
                                nova_interface.montar()
                                self.running = False

                            case 'Deletar':
                                match self.alvo:
                                    case 'pessoa':
                                        if self.db_info[1] is not None:
                                            item_deletado = self.db_info[1]
                                        else:
                                            item_deletado = self.db_info[3]

                                    case 'nota' | 'afazer' | 'gosto':
                                        item_deletado = f"{self.alvo} {str(self.db_info[0])}"

                                    case 'manga' | 'jogo' | 'anime' | 'serie' | 'filme' | 'banda' | 'album' | 'musica':
                                        item_deletado = self.db_info[1]

                                    case 'contato':
                                        item_deletado = self.db_info[2]

                                delete = input(f"Tem certeza de que deseja deletar '{item_deletado}'? [y/n]: ")
                                os.system('cls')
                                if delete == 'y' or delete == 'yes':
                                    ids_musicas = [] 

                                    if self.alvo == 'banda':
                                        info_albuns = Service().buscar_info_por_um_campo_generico('id', 'albuns', 'banda', (self.db_info[0],))
                                        
                                        for info_album in info_albuns:
                                            info_musicas = Service().buscar_info_por_um_campo_generico('id', 'musicas', 'album', (info_album[0],))

                                            for info_musica in info_musicas:
                                                ids_musicas.append(info_musica[0])

                                            Service().deletar_pelo_id("albuns", info_album[0])

                                    elif self.alvo == 'album':
                                        info_musicas = Service().buscar_info_por_um_campo_generico('id', 'musicas', 'album', (self.db_info[0],))
                                        for info_musica in info_musicas:
                                                ids_musicas.append(info_musica[0])

                                    if self.alvo == 'banda' or self.alvo == 'album':
                                        for id_musica in ids_musicas:
                                            Service().deletar_pelo_id("musicas", id_musica)

                                    Service().deletar_pelo_id(self.tabelas[self.alvo], self.db_info[0])

                                    if self.alvo == 'nota' or self.alvo == 'afazer':
                                        Service().deletar_por_campo_generico(self.tabelas_alternativas[self.alvo], f'id_{self.alvo}', (self.db_info[0],))

                                    print(f"- - {item_deletado} Deletado(a) Com Sucesso! - -")
                                    input()
                                    os.system('cls')
                                    self.running = False

                            case 'Notas':
                                if len(self.db_info) < 1:
                                    nova_interface = Interface(tipo_interface='op_num', titulo='notas', alvo='nota')
                                else:
                                    nova_interface = Interface(tipo_interface='op_num', titulo='notas', alvo='nota', id=self.db_info[0])

                                nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])
                                nova_interface.montar()

                            case 'Gostos':
                                if len(self.db_info) < 1:
                                    nova_interface = Interface(tipo_interface='op_num', titulo='gostos', alvo='gosto')
                                else:
                                    nova_interface = Interface(tipo_interface='op_num', titulo='gostos', alvo='gosto', id=self.db_info[0])

                                nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])
                                nova_interface.montar()

                            case 'Afazeres':
                                if len(self.db_info) < 1:
                                    nova_interface = Interface(tipo_interface='op_num', titulo='afazeres', alvo='afazer')
                                else:
                                    nova_interface = Interface(tipo_interface='op_num', titulo='afazeres', alvo='afazer', id=self.db_info[0])

                                nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])
                                nova_interface.montar()

                            case 'Contatos':
                                if len(self.db_info) < 1:
                                    nova_interface = Interface(tipo_interface='op_num', titulo='contatos', alvo='contato')
                                else:
                                    nova_interface = Interface(tipo_interface='op_num', titulo='contatos', alvo='contato', id=self.db_info[0])

                                nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])
                                nova_interface.montar()
                                
                            case 'Recomendacoes de musicas':
                                ids_recomendacoes = Service().buscar_info_por_um_campo_generico('id', 'musicas', 'pessoa', (self.db_info[0],))
                                if len(ids_recomendacoes) == 0:
                                    print('Nenhuma recomendação encontrada!')
                                    input()
                                    os.system('cls')
                                else:
                                    ids_recomendacoes = [item[0] for item in ids_recomendacoes]
                                    nova_interface = self.build_get_info('recomendacoes', 'musica', set(ids_recomendacoes))
                                    nova_interface.montar()

                            case 'Albuns':
                                nova_interface = Interface(tipo_interface='op_num', titulo='albuns', alvo='album', id=self.db_info[0])

                                nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])
                                nova_interface.montar()

                            case 'Musicas':
                                nova_interface = Interface(tipo_interface='op_num', titulo='musicas', alvo='musica', id=self.db_info[0])

                                nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])
                                nova_interface.montar()

                            case 'Letra':
                                if self.db_info[5] is not None:
                                    print(self.db_info[5])
                                else:
                                    print('Letra ainda não foi registrada.')
                                input()
                                os.system('cls')

                    elif self.acao == 'adicionar':
                        pass

                elif self.alvo == 'calendario':
                    nova_interface = Interface(tipo_interface='ver_calendario', titulo=choices[num - 1], alvo='calendario')
                    nova_interface.montar()

                else:
                    match choices[num -1]:
                        case 'My Info':
                            nova_interface = Interface(tipo_interface='op_num', titulo='my info', alvo='me')
                            nova_interface.inserir_opcoes(['Notas', 'Gostos', 'Mangas', 'Animes', 'Series', 'Filmes', 'Jogos', 'Afazeres', 'Diario'])

                        case 'Pessoas':
                            nova_interface = Interface(tipo_interface='op_num', titulo='pessoas', alvo='pessoa')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Notas':
                            nova_interface = Interface(tipo_interface='op_num', titulo='notas', alvo='nota') if self.alvo != 'me' else Interface(tipo_interface='op_num', titulo='notas', alvo='nota', id=2)
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Gostos':
                            nova_interface = Interface(tipo_interface='op_num', titulo='gostos', alvo='gosto') if self.alvo != 'me' else Interface(tipo_interface='op_num', titulo='gostos', alvo='gosto', id=2)
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Afazeres':
                            nova_interface = Interface(tipo_interface='op_num', titulo='afazeres', alvo='afazer') if self.alvo != 'me' else Interface(tipo_interface='op_num', titulo='afazeres', alvo='afazer', id=2)
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Contatos':
                            nova_interface = Interface(tipo_interface='op_num', titulo='contatos', alvo='contato')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Mangas':
                            nova_interface = Interface(tipo_interface='op_num', titulo='mangas', alvo='manga')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Jogos':
                            nova_interface = Interface(tipo_interface='op_num', titulo='jogos', alvo='jogo')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Filmes':
                            nova_interface = Interface(tipo_interface='op_num', titulo='filmes', alvo='filme')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Animes':
                            nova_interface = Interface(tipo_interface='op_num', titulo='animes', alvo='anime')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Series':
                            nova_interface = Interface(tipo_interface='op_num', titulo='series', alvo='serie')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Calendario':
                            nova_interface = Interface('op_num', '', 'calendario')
                            nova_interface.inserir_opcoes(['Mes', 'Semana', 'Dia'])

                        case 'Do-Re-Mi':
                            nova_interface = Interface('op_num', '', '')
                            nova_interface.inserir_opcoes(['Bandas', 'Albuns', 'Musicas'])

                        case 'Bandas':
                            nova_interface = Interface(tipo_interface='op_num', titulo='bandas', alvo='banda')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Albuns':
                            nova_interface = Interface(tipo_interface='op_num', titulo='albuns', alvo='album')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Musicas':
                            nova_interface = Interface(tipo_interface='op_num', titulo='musicas', alvo='musica')
                            nova_interface.inserir_opcoes(['Pesquisar', 'Adicionar'])

                        case 'Diario':
                            complemento = input("Especificar dia? (y/[n]) ")
                            os.system('cls')
                            
                            if complemento.lower() in ['y', 'yes']:
                                interface_data = self.build_get_info('data de nascimento', 'pessoa')
                                info_ano = interface_data.montar()

                                if info_ano is not None:
                                    nova_interface = Interface(tipo_interface='ver_diario', titulo='Diario', alvo='diario', dia_diario=info_ano)

                            elif complemento == "" or complemento.lower() in ["n", "no", "nao", "não"]:
                                nova_interface = Interface(tipo_interface='ver_diario', titulo='Diario', alvo='diario')

                        case 'Jogar':
                                JogoTeste().game_loop
                                os.system('cls')

                        case 'Pesquisar':
                            nova_interface = Interface(tipo_interface='op_num', titulo=f'pesquisar ({self.alvo})', alvo=self.alvo, acao='pesquisar', id=self.id)
                            if self.id > 0 and self.alvo == 'album':
                                nova_interface.lista_de_opcoes.remove('Banda')
                            elif self.id and self.alvo == 'musica':
                                nova_interface.lista_de_opcoes.remove('Album')

                        case 'Adicionar':
                            nova_interface = Interface(tipo_interface='preencher', titulo=f"adicionar {self.alvo}", alvo=self.alvo, acao='adicionar', id=self.id)
                    
                    try:
                        nova_interface.montar()
                    except:
                        pass

            else:
                print("- - Número inválido! - -")

        except ValueError:
            if answer == "":
                if self.titulo.lower() == "inicio":
                    sair = input("Tem certeza de que deseja sair do sistema? (y/[n])")
                    os.system('cls')
                    if sair.lower() == 'y' or sair.lower() == 'yes':
                        self.running = False
                else:
                    self.running = False
            else:
                print("- - Valor inválido! - -")

    def preencher(self) -> None:
        count = 1
        choices = []

        self.info = 'Digite "#txt" para abrir o bloco de notas\ncom o conteúdo, # sendo o número da opção.\n'

        if self.alvo == 'manga' and self.acao == 'alterar':
            self.info += 'Digite "a" para capitulo anterior e "p" para o próximo.\n'

        elif (self.alvo == 'serie' or self.alvo == 'anime') and self.acao == 'alterar':
            self.info += 'Digite "a" para episodio anterior e "p" para o próximo\n"ta" para temporada anterior e "pt" para a próxima.\n'

        elif self.alvo == 'afazer':
            self.info += 'Digite "a" para alterar o campo "Status".\n'

        if self.respostas == {}:
            self.respostas = {key: [None, i] for i, key in enumerate(self.lista_de_opcoes, 1)}
            if self.alvo == 'afazer':
                self.respostas['Status*'][0] = 'Ativo'

        if self.titulo.lower() == "adicionar pessoa" or self.titulo.lower() == "alterar pessoa":
            self.lista_de_opcoes, self.respostas = tb.um_ou_outro(self.lista_de_opcoes, self.respostas, "Nome", "Apelido")

            for item in ["Data de nascimento*", "Nos conhecemos quando"]:
                if self.respostas[item][0] is not None:
                    self.respostas[item][0] = tb.retirar_informacoes_adicionais(self.respostas[item][0])

            if self.respostas['Descricao*'][0] is not None:
                    if '\n' not in self.respostas['Descricao*'][0]:
                        self.respostas['Descricao*'][0] = tb.ajeitar_texto(self.respostas['Descricao*'][0])

        elif (self.titulo.lower() == "adicionar nota" or self.titulo.lower() == "alterar nota") or (self.titulo.lower() == "adicionar afazer" or self.titulo.lower() == "alterar afazer"):
            if self.id != 0 and len(self.db_info) == 0:
                nome_ou_apelido = Service().nome_ou_apelido(self.id)

                id_pessoa = tb.montar_id_pessoa(id=self.id, nome_ou_apelido=nome_ou_apelido)

                if self.respostas['Pessoas citadas*'][0] is None:
                    self.respostas['Pessoas citadas*'][0] = [id_pessoa]
                else:
                    if id_pessoa not in self.respostas['Pessoas citadas*'][0]:
                        self.respostas['Pessoas citadas*'][0].append(id_pessoa)
            else:
                if self.respostas['Pessoas citadas*'][0] is not None:
                    for item in self.respostas['Pessoas citadas*'][0]:
                        self.ids_disponiveis.add(item[1])

            if self.alvo == 'nota':
                if self.respostas['Conteudo*'][0] is not None:
                    if '\n' not in self.respostas['Conteudo*'][0]:
                        self.respostas['Conteudo*'][0] = tb.ajeitar_texto(self.respostas['Conteudo*'][0])

        elif (self.titulo.lower() == "adicionar contato" or self.titulo.lower() == "alterar contato") or (self.titulo.lower() == "adicionar gosto" or self.titulo.lower() == "alterar gosto"):
            if self.id != 0 and len(self.db_info) == 0:
                nome_ou_apelido = Service().nome_ou_apelido(self.id)

                id_pessoa = tb.montar_id_pessoa(id=self.id, nome_ou_apelido=nome_ou_apelido)

                if self.respostas['Pessoa*'][0] is None:
                    self.respostas['Pessoa*'][0] = id_pessoa
                else:
                    if id_pessoa not in self.respostas['Pessoa*'][0]:
                        self.respostas['Pessoa*'][0] = id_pessoa

        elif self.alvo == 'musica':
            if self.respostas['Album*'][0] is not None:
                    self.respostas['Album*'][0] = list(self.respostas['Album*'][0])
                    self.respostas['Album*'][0][0] = tb.retirar_informacoes_adicionais(self.respostas['Album*'][0][0])
                    self.respostas['Album*'][0] = tuple(self.respostas['Album*'][0])

            if self.respostas['Album*'][0] is None and self.id > 0:
                nome_album = Service().buscar_info_por_um_campo_generico('nome', 'albuns', 'id', (self.id,))
                self.respostas['Album*'][0] = (nome_album[0][0], self.id) 

        elif self.alvo == 'album' and self.id > 0:
            if self.respostas['Banda*'][0] is None:
                nome_banda = Service().buscar_info_por_um_campo_generico('nome', 'bandas', 'id', (self.id,))
                self.respostas['Banda*'][0] = (nome_banda[0][0], self.id)

        print(f"\n{self.titulo}\n\n{self.info}\n")

        for opcao in self.lista_de_opcoes:

            if count != len(self.lista_de_opcoes):

                if isinstance(self.respostas[opcao][0], list):

                    if self.alvo == 'nota' or self.alvo == 'afazer':
                        conteudo_concatenado = ", ".join([item[0] for item in self.respostas[opcao][0]])
                    print(f"[{count}] {opcao}: {conteudo_concatenado}")

                elif isinstance(self.respostas[opcao][0], tuple):
                    print(f"[{count}] {opcao}: {self.respostas[opcao][0][0]}")

                else:
                    if opcao == 'Remover pessoa':
                        print(f"[{count}] {opcao}")

                    elif opcao == 'Letra' and self.respostas[opcao][0] is not None:
                        print(f"[{count}] {opcao}: \n\n{self.respostas[opcao][0]}\n")
                    
                    else:
                        print(f"[{count}] {opcao}: {self.respostas[opcao][0]}")

            else:
                print(f"\n[{count}] {opcao}")

            count += 1
            choices.append(opcao)

        answer = input("\n\nEscolha: ")
        os.system('cls')

        try:
            num = int(answer)

            if num in range(1, len(self.lista_de_opcoes)+1):
                if num != len(self.lista_de_opcoes):
                    if ((self.alvo == 'nota' or self.alvo == 'afazer') and choices[num - 1] == 'Remover pessoa') and len(self.ids_disponiveis) < 1:
                        print("- - Nenhuma pessoa disponível para remover! - -")
                    elif ((self.id != 0 and len(self.db_info) == 0) and (((self.alvo in ['contato', 'gosto', 'album', 'musica']) and choices[num - 1] in ['Pessoa*', 'Banda*', 'Album*'])) or (self.alvo == 'afazer' and choices[num - 1] == "Status*")):
                        print("- - Campo não pode ser alterado! - -")

                    else:
                        nova_interface = self.build_get_info(info=choices[num - 1] if "*" not in choices[num - 1] else choices[num - 1].split("*")[0], tipo=self.alvo, ids_disponiveis=self.ids_disponiveis)
                        info = nova_interface.montar()

                        if (self.alvo == 'nota' or self.alvo == 'afazer') and choices[num -1] == 'Pessoas citadas*':
                            if info is not None and self.respostas[choices[num - 1]][0] is not None:
                                if info in self.respostas[choices[num - 1]][0]:
                                    print("- - Pessoa já foi escolhida. - -")
                                else:
                                    self.respostas[choices[num - 1]][0].append(info)
                                    self.ids_disponiveis.add(info[1])

                            elif info is not None:
                                self.respostas[choices[num - 1]][0] = [info]
                                self.ids_disponiveis.add(info[1])

                        elif (self.alvo == 'nota' or self.alvo == 'afazer') and choices[num - 1] == 'Remover pessoa':
                            if info is not None:
                                self.respostas['Pessoas citadas*'][0].remove(info)
                                self.ids_disponiveis.remove(info[1])
                                if len(self.respostas['Pessoas citadas*'][0]) == 0:
                                    self.respostas['Pessoas citadas*'][0] = None

                        elif self.alvo == 'afazer' and choices[num - 1] == 'Repetir':
                            if info is not None:
                                if info not in ['diariamente', 'semanalmente', 'mensalmente', 'anualmente']:
                                    self.respostas['Data'][0] = None
                                    self.respostas[choices[num - 1]][0] = info
                                else:
                                    if self.respostas['Data'][0] is not None:
                                        self.respostas[choices[num - 1]][0] = info
                                    else:
                                        print("- - Primeiro preencha o campo 'Data'. - -")
                            else:
                                self.respostas[choices[num - 1]][0] = info
                                if self.respostas['Data'][0] is None and self.respostas['Data final'][0] is not None:
                                    self.respostas['Data final'][0] = None

                        elif self.alvo == 'afazer' and choices[num - 1] == 'Data':
                            if info is not None:
                                if self.respostas['Data final'][0] is not None:
                                    if tb.converter_para_date(self.respostas['Data final'][0]) > tb.converter_para_date(info):
                                        self.respostas[choices[num - 1]][0] = info

                                        if self.respostas['Repetir'][0] not in ['diariamente', 'semanalmente', 'mensalmente', 'anualmente']:
                                            self.respostas['Repetir'][0] = None
                                    else:
                                        print('- - "Data" deve ser anterior a "Data final". - -')
                                else:
                                    self.respostas[choices[num - 1]][0] = info

                                    if self.respostas['Repetir'][0] not in ['diariamente', 'semanalmente', 'mensalmente', 'anualmente']:
                                        self.respostas['Repetir'][0] = None

                            else:
                                self.respostas[choices[num - 1]][0] = info
                                if self.respostas['Repetir'][0] is None and self.respostas['Data final'][0] is not None:
                                    self.respostas['Data final'][0] = None

                        elif self.alvo == 'afazer' and choices[num - 1] == 'Data final':
                            if self.respostas['Data'][0] is None and self.respostas['Repetir'][0] is None:
                                print('- - Primeiro preencha o campo "Data" ou o campo "Repetir". - -')
                            else:
                                if info is not None:
                                    if self.respostas['Data'][0] is not None:
                                        if tb.converter_para_date(self.respostas['Data'][0]) < tb.converter_para_date(info):
                                            self.respostas[choices[num - 1]][0] = info
                                        else:
                                            print('- - "Data final" deve ser posterior a "Data". - -')
                                    else:
                                        self.respostas[choices[num - 1]][0] = info
                                else:
                                    self.respostas[choices[num - 1]][0] = info
                        
                        else:
                            self.respostas[choices[num - 1]][0] = info

                else:
                    self.validator("respostas", self.respostas, self.alvo)
                    tabela = self.tabelas[self.alvo]
                    lista_para_preparar = []
                    lista_de_chaves = []

                    lista_de_chaves += ["data_nascimento:data", "primeiro_dia:data", "capitulo:decimal", "pagina:int", "avaliacao:int", "temporada:int", "episodio:int", "tempo:tempo", "data_da_atividade:data", "data_fim_atividade:data", "tempo_da_atividade:tempo_parcial", "ativa:bool", "nota:n", "descricao:n"]

                    match self.acao:
                        case "adicionar":
                            if self.alvo == 'nota' or self.alvo == 'afazer':
                                tupla_chaves_valores = [(self.db_tags[self.alvo][key] if "*" not in key else self.db_tags[self.alvo][key.split("*")[0]], value[0]) for key, value in self.respostas.items() if value[0] is not None and key != 'Pessoas citadas*']
                                if self.alvo == 'nota':
                                    tupla_chaves_valores.append(('data_nota', datetime.now(ZoneInfo("America/Sao_Paulo"))))
                            else:
                                tupla_chaves_valores = [(self.db_tags[self.alvo][key] if "*" not in key else self.db_tags[self.alvo][key.split("*")[0]], value[0]) for key, value in self.respostas.items() if value[0] is not None]
                            chaves = ", ".join([chave[0] for chave in tupla_chaves_valores])
                            valores = [valor[1] for valor in tupla_chaves_valores]
                            quantidade = ", ".join(["%s" for _ in tupla_chaves_valores])
                            
                        
                        case "alterar":
                            Validacao().validar_se_existe_alteracao(self.respostas, self.db_info)
                            tupla_chaves_valores = []
                            for key, value in self.respostas.items():
                                i = value[1]
                                if key.split(" ")[0] in ['Alterar', 'Adicionar', 'Remover']:
                                    pass
                                elif not isinstance(value[0], list):
                                        if value[0] != self.db_info[i]:
                                            if not isinstance(value[0], tuple):
                                                tupla_chaves_valores.append((self.db_tags[self.alvo][key] if "*" not in key else self.db_tags[self.alvo][key.split("*")[0]], value[0]))
                                            else:
                                                tupla_chaves_valores.append((self.db_tags[self.alvo][key] if "*" not in key else self.db_tags[self.alvo][key.split("*")[0]], value[0][1]))
                                else:
                                    if Counter(value[0]) != Counter(self.db_info[i]):
                                        for item in value[0]:
                                            lista_para_preparar.append(item[1])

                            if len(tupla_chaves_valores) != 0:
                                chaves = ", ".join([f"{chave[0]} = %s" for chave in tupla_chaves_valores])
                                valores = [valor[1] for valor in tupla_chaves_valores]
                                valores.append(self.id)
                                lista_de_chaves = [chave.split(':')[0] + ' = %s:' + chave.split(':')[1] for chave in lista_de_chaves]
                    
                    match self.acao:
                        case "adicionar" | "alterar":
                            if len(tupla_chaves_valores) != 0:
                                chaves_repartidas = chaves.split(", ")

                                for chave_tipo in lista_de_chaves:
                                    chave, tipo = chave_tipo.split(':')
                                    valores = tb.formatar_chave(chaves_repartidas, chave, valores, tipo)

                                if 'pessoa' in chaves_repartidas:
                                    valores[chaves_repartidas.index('pessoa')] = valores[chaves_repartidas.index('pessoa')][1]
                                
                                if 'banda' in chaves_repartidas:
                                    valores[chaves_repartidas.index('banda')] = valores[chaves_repartidas.index('banda')][1]

                                if 'album' in chaves_repartidas:
                                    valores[chaves_repartidas.index('album')] = valores[chaves_repartidas.index('album')][1] 

                                valores = tuple(valores)

                            match self.alvo:
                                case 'nota':
                                    nome_dados = 'id_pessoa, id_nota'
                                case 'afazer':
                                    nome_dados = 'id_pessoa, id_afazer'

                            if self.acao == "adicionar":
                                Service().cadastrar(tabela, chaves, quantidade, valores)

                                if self.alvo == 'nota' or self.alvo == 'afazer':
                                    identificador = Service().resgatar_ultimo_id(tabela)
                                    identificador = identificador[0]

                                    for id in self.respostas['Pessoas citadas*'][0]:
                                        Service().cadastrar(self.tabelas_alternativas[self.alvo], nome_dados, '%s, %s', (id[1], identificador))

                                print(f"- - {self.alvo.capitalize()} Cadastrada(o) Com Sucesso! - -")
                            else:
                                if len(tupla_chaves_valores) != 0:
                                    Service().atualizar_pelo_id(tabela, chaves, valores)
                                if len(lista_para_preparar) > 0:
                                    Service().deletar_por_campo_generico(self.tabelas_alternativas[self.alvo], nome_dados.split(', ')[1], (self.id,))
                                    for id_pessoa in lista_para_preparar:
                                        Service().cadastrar(self.tabelas_alternativas[self.alvo], nome_dados, '%s, %s', (id_pessoa, self.id))

                                print(f"- - {self.alvo.capitalize()} Alterada(o) Com Sucesso! - -")

                    input()
                    os.system('cls')
                    self.running = False

            else:
                print("- - Número inválido! - -")

        except ValueError:
            if answer == "":
                self.running = False

            elif tb.apenas_numeros(answer[0]) and answer[1:] == "txt":
                numero = int(answer[0])
                escolha = choices[numero - 1]

                if numero in range(1, len(self.lista_de_opcoes)+1) and numero != len(self.lista_de_opcoes):

                    if (self.alvo == 'pessoa' and escolha == 'Descricao*') or (self.alvo == 'nota' and escolha == 'Conteudo*'):

                        if self.respostas[escolha][0] is not None:
                            tb.abrir_notepad(self.respostas[escolha][0], True)

                        else:
                            print(f"- - Primeiro preencha o campo '{escolha}'. - -")

                    else:
                        if self.respostas[escolha][0] is not None:
                            if escolha == 'Letra':
                                self.respostas[escolha][0] = self.respostas[escolha][0].replace('\n', '@')
                            tb.abrir_notepad(self.respostas[escolha][0])

                        else:
                            print(f"- - Primeiro preencha o campo '{escolha}'. - -")

            elif answer.lower() == 'a' and (self.alvo in ['manga', 'serie', 'anime']) and self.acao == 'alterar':
                if self.alvo == "manga":
                    if self.respostas['Capitulo'][0] is not None:
                        if int(self.respostas['Capitulo'][0]) != 1:
                            capitulo_atual = Decimal(self.respostas['Capitulo'][0])
                            self.respostas['Capitulo'][0] = tb.arredondar_decimal(capitulo_atual, False)

                    else:
                        print("- - Primeiro preencha o campo 'Capitulo'. - -")
                else:
                    if self.respostas['Episodio'][0] is not None:
                        if int(self.respostas['Episodio'][0]) != 1:
                            self.respostas['Episodio'][0] = str(int(self.respostas['Episodio'][0])-1)
                    else:
                        print("- - Primeiro preencha o campo 'Episodio'. - -")

            elif answer.lower() == 'p' and (self.alvo in ['manga', 'serie', 'anime']) and self.acao == 'alterar':
                if self.alvo == "manga":
                    if self.respostas['Capitulo'][0] is not None:
                        capitulo_atual = Decimal(self.respostas['Capitulo'][0])
                        self.respostas['Capitulo'][0] = tb.arredondar_decimal(capitulo_atual, True)
                    else:
                        print("- - Primeiro preencha o campo 'Capitulo'. - -")
                else:
                    if self.respostas['Episodio'][0] is not None:
                        self.respostas['Episodio'][0] = str(int(self.respostas['Episodio'][0])+1)
                    else:
                        print("- - Primeiro preencha o campo 'Episodio'. - -")

            elif answer.lower() == 'ta' and ((self.alvo == 'serie' or self.alvo == 'anime') and self.acao == 'alterar'):
                if self.respostas['Temporada'][0] is not None:
                    if int(self.respostas['Temporada'][0]) != 1:
                        self.respostas['Temporada'][0] = str(int(self.respostas['Temporada'][0])-1)
                else:
                    print("- - Primeiro preencha o campo 'Temporada'. - -")

            elif answer.lower() == 'pt' and ((self.alvo == 'serie' or self.alvo == 'anime') and self.acao == 'alterar'):
                if self.respostas['Temporada'][0] is not None:
                    self.respostas['Temporada'][0] = str(int(self.respostas['Temporada'][0])+1)
                else:
                    print("- - Primeiro preencha o campo 'Temporada'. - -")

            elif answer.lower() == 'a' and self.alvo == 'afazer':
                self.respostas['Status*'][0] = 'Ativo' if self.respostas['Status*'][0] != 'Ativo' else 'Desativado'

            else:
                print("- - Valor inválido! - -")

        except ValidationError as e:
            print(f"- - {e.mensagem} - -")

    def get_info(self) -> str | int | None:
        tipo = self.titulo.split(":")[0].lower()

        if self.requisitos_dados[self.alvo][tipo] != "":
            req = f"Atencao: {self.requisitos_dados[self.alvo][tipo]}\n\n"
        else:
            req = ""

        info = input(f"{req}{self.titulo}")
        os.system('cls')
        try:
            self.validator(tipo, info, self.alvo)

            match tipo:
                case "idade":
                    info = int(info)
                case "capitulo":
                    if '.0' in info:
                        info = info.split('.')[0]
                case "data final" | "data de nascimento" | "nos conhecemos quando" | "data":
                    info = tb.formatar_data(info)
                case "letra":
                    info = info.replace('@', '\n')
            
            self.running = False
            self.retornar = True
            return info

        except ValidationError as e:
            if info == "":
                self.running = False
            else:
                print(f"- - {e.mensagem} - -")

    def get_selected_info(self) -> str | None:
        print(f"\n{self.titulo}\n{self.info}\n")
        count = 1
        choices = []

        for opcao in self.lista_de_opcoes:
            if opcao == self.lista_de_opcoes[-1]:
                print(f"\n[{count}] {opcao}")
            else:
                print(f"[{count}] {opcao}")
            count += 1
            choices.append(opcao)

        print(f"\nRetorno Atual: {self.selected_info_answer}\n")

        answer = input("\n\nEscolha: ")
        os.system('cls')
        
        try:
            num = int(answer)

            if num in range(1, len(self.lista_de_opcoes)+1):

                if num == len(self.lista_de_opcoes):
                    if self.selected_info_answer != "":
                        self.retornar = True
                        return self.selected_info_answer
                    else:
                        print("- - Impossivel retornar, valor não selecionado! - -")

                elif choices[num - 1] in ['diariamente', 'semanalmente', 'mensalmente', 'anualmente']:
                    self.selected_info_answer = choices[num - 1]

                else:
                    if (self.selected_info_answer in ['diariamente', 'semanalmente', 'mensalmente', 'anualmente']) or self.selected_info_answer == "":
                        self.selected_info_answer = choices[num - 1]
                    else:
                        if choices[num - 1] not in self.selected_info_answer:
                            self.selected_info_answer += ", " + choices[num - 1]
                        else:
                            print("- - Opção já foi escolhida! - -")
            else:
                print("- - Número inválido! - -")

        except ValueError:
            if answer == "":
                self.running = False
            else:
                print("- - Valor inválido! - -")

    def get_info_op(self) -> str | None:
        print(f"\n{self.titulo}\n{self.info}\n")
        count = 1
        choices = []

        for opcao in self.lista_de_opcoes:
            print(f"[{count}] {opcao}")
            count += 1
            choices.append(opcao)

        answer = input("\n\nEscolha: ")
        os.system('cls')
        
        try:
            num = int(answer)

            if num in range(1, len(self.lista_de_opcoes)+1):
                self.retornar = True
                return choices[num - 1]

            else:
                print("- - Número inválido! - -")

        except ValueError:
            if answer == "":
                self.running = False
            else:
                print("- - Valor inválido! - -")

    def escolhas(self) -> bool | None:
        print(f"\n{self.titulo}\n{self.info}\n")
        count = 1
        choices = []

        for opcao in self.lista_de_opcoes:
            print(f"[{count}] {opcao[0]}")
            count += 1
            choices.append(opcao)

        answer = input("\n\nEscolha: ")
        os.system('cls')
        
        try:
            num = int(answer)

            if num in range(1, len(self.lista_de_opcoes)+1):
                self.retornar = True
                return choices[num - 1][1]

            else:
                print("- - Número inválido! - -")

        except ValueError:
            if answer == "":
                self.running = False
            else:
                print("- - Valor inválido! - -")

    def ver_info(self) -> tuple | None:
            tipo_de_pesquisa = self.titulo.lower()
            infos = None
            self.running = False
            running = True
            db_tag = ""
            tabela = self.tabelas[self.alvo]

            try:
                if tipo_de_pesquisa == 'ids_especificos':
                    infos = []
                    for id in self.ids_disponiveis:
                        infos.append(Service().verificar_id(id=id, tabela=tabela))

                elif tipo_de_pesquisa != "ver tudo":
                    if tipo_de_pesquisa not in ['avaliacao crescente', 'avaliacao decrescente', 'nao avaliados', 'ano crescente', 'ano decrescente'] and self.acao != "freeway":
                        info = self.build_get_info(info=tipo_de_pesquisa, tipo=self.alvo).montar()

                    if tipo_de_pesquisa not in ['idade', 'avaliacao crescente', 'avaliacao decrescente', 'nao avaliados', 'ano crescente', 'ano decrescente']:
                        db_tag = self.db_tags[self.alvo][tipo_de_pesquisa.capitalize() if tipo_de_pesquisa != 'id' else tipo_de_pesquisa.upper()]
                    else:
                        db_tag = tipo_de_pesquisa

                    match db_tag:
                        case "id":
                            if self.acao != 'freeway':
                                infos = Service().verificar_id(info, tabela)
                            else:
                                infos = Service().verificar_id(self.id, tabela)

                            if ((self.alvo == 'nota' or self.alvo == 'afazer') and self.id != 0) and self.acao != 'freeway':

                                match self.alvo:
                                    case 'nota':
                                        nome_dados = 'id_pessoa, id_nota'
                                    case 'afazer':
                                        nome_dados = 'id_pessoa, id_afazer'

                                ids_pessoas_da_nota = Service().buscar_info_por_um_campo_generico(nome_dados.split(', ')[0], self.tabelas_alternativas[self.alvo], nome_dados.split(', ')[1], (info,))
                                for id_pessoa_da_nota in ids_pessoas_da_nota:
                                    if id_pessoa_da_nota[0] == self.id:
                                        break
                                    else:
                                        if id_pessoa_da_nota[0] == ids_pessoas_da_nota[-1][0]:
                                            infos = None
                                            raise ValidationError(f"{self.alvo.capitalize()} existe, porém não é referente a banda especificada.")
                                        
                            elif self.alvo == 'album' and self.id != 0:
                                if infos[3] != self.id:
                                    infos = None
                                    raise ValidationError(f"{self.alvo.capitalize()} existe, porém não é referente a pessoa especificada.")
                                
                            elif self.alvo == 'musica' and self.id != 0:
                                if infos[2] != self.id:
                                    infos = None
                                    raise ValidationError(f"{self.alvo.capitalize()} existe, porém não é referente a pessoa especificada.")

                        case "atividade" | "repetir" | "ativa":
                            if db_tag == "atividade":
                                infos = Service().verificar_string(db_tag=db_tag, valor=info, tabela=tabela)
                            elif db_tag == "repetir":
                                if info is not None:
                                    infos = Service().ver_tudo(tabela=tabela)
                                    if len(infos) > 0:
                                        if info in ['semanalmente', 'mensalmente', 'anualmente']:
                                            infos = [valor for valor in infos if info == valor[4]]
                                        else:
                                            dias_da_semana = info.split(', ')
                                            infos = [valor for valor in infos if set(dias_da_semana).issubset(valor[4].split(', '))]
                                        
                                    if len(infos) == 0:
                                        infos = None
                                else:
                                    infos = None
                            
                            elif db_tag == "ativa":
                                infos = Service().ver_tudo(tabela=tabela)
                                if len(infos) > 0:
                                    infos = [valor for valor in infos if info == valor[6]]

                                if len(infos) == 0:
                                    infos = None

                            if self.alvo == 'afazer' and self.id != 0:
                                if infos is not None:
                                    for info in infos:
                                        ids_pessoas_do_afazer = Service().buscar_info_por_um_campo_generico('id_pessoa', self.tabelas_alternativas[self.alvo], 'id_afazer', (info[0],))
                                        for id_pessoa_afazer in ids_pessoas_do_afazer:
                                            if id_pessoa_afazer[0] == self.id:
                                                break
                                            else:
                                                if id_pessoa_afazer[0] == ids_pessoas_do_afazer[-1][0]:
                                                    infos.remove(info)
                                    if len(infos) == 0:
                                        infos = None
                                        raise ValidationError(f"{self.alvo.capitalize()} existe, porém não é referente a pessoa especificada.")
                                        
                        case "nome" | "sobrenome" | "apelido":
                            infos = Service().verificar_string(db_tag=db_tag, valor=info, tabela=tabela)

                        case "parentesco" | "proximidade" | "status_atual":
                            infos = Service().verificar_string_exata(db_tag=db_tag, valor=info, tabela=tabela)

                            if self.alvo == 'album':
                                if self.id > 0 and infos is not None:
                                    infos = [inf for inf in infos if self.id == inf[3]]

                            elif self.alvo == 'musica':
                                if self.id > 0 and infos is not None:
                                    infos = [inf for inf in infos if self.id == inf[2]]

                        case "formato" | "ano_lancamento":
                            infos = Service().verificar_string(db_tag=db_tag, valor=info, tabela=tabela)
                            
                            if self.id > 0 and infos is not None:
                                infos = [inf for inf in infos if self.id == inf[3]]

                        case "nota":
                            infos = Service().verificar_string(db_tag=db_tag, valor=info, tabela=tabela)

                            if self.id > 0 and infos is not None:
                                remover_ids = []

                                for inf in infos:
                                    ids_pessoas_da_nota = Service().buscar_info_por_um_campo_generico('id_pessoa', self.tabelas_alternativas[self.alvo], 'id_nota', (inf[0],))
                                    for id_pessoa_da_nota in ids_pessoas_da_nota:
                                        if id_pessoa_da_nota[0] == self.id:
                                            break
                                        else:
                                            if ids_pessoas_da_nota[-1] == id_pessoa_da_nota:
                                                remover_ids.append(inf[0])

                                infos = [inf for inf in infos if inf[0] not in remover_ids]

                        case "idade" | "avaliacao" | "temporada" | "episodio":
                            infos = Service().ver_tudo(tabela=tabela)
                            infos = [valores for valores in infos if tb.calcular_idade(valores[4]) == info] if db_tag == 'idade' else [valores for valores in infos if valores[self.indice_da_avaliacao[self.alvo]] == int(info)]
                            if len(infos) < 1:
                                infos = None
                        
                        case "avaliacao decrescente" | "avaliacao crescente" | "ano crescente" | "ano decrescente":
                            infos = Service().ver_tudo(tabela)
                            infos = [valores for valores in infos if valores[self.indice_da_avaliacao[self.alvo]] is not None]

                            if (self.id > 0 and infos is not None) and self.alvo == 'album':
                                infos = [inf for inf in infos if self.id == inf[3]]
                            
                            if db_tag == "avaliacao decrescente" or db_tag == "ano decrescente":
                                infos = sorted(infos, key=lambda x: x[self.indice_da_avaliacao[self.alvo]], reverse=True)

                            else:
                                infos = sorted(infos, key=lambda x: x[self.indice_da_avaliacao[self.alvo]])

                            if len(infos) < 1:
                                infos = None

                        case "nao avaliados":
                            infos = Service().ver_tudo(tabela)
                            infos = [valores for valores in infos if valores[self.indice_da_avaliacao[self.alvo]] is None]
                            if len(infos) < 1:
                                infos = None

                        case "tipo" | "contato" | "gosto":
                            if (self.alvo == 'contato' or self.alvo == 'gosto') and self.id != 0:
                                infos = Service().verificar_string_mais_de_um_campo(where=f"{db_tag} LIKE %s AND pessoa = %s", valores=(f"%{info}%", self.id), tabela=tabela)
                            elif self.alvo == 'contato' or self.alvo == 'gosto':
                                infos = Service().verificar_string(db_tag=db_tag, valor=info, tabela=tabela)

                        case "banda":
                            if info is not None:
                                infos = Service().buscar_info_por_um_campo_generico('*', 'albuns', 'banda', (info[1],))

                        case "album":
                            if info is not None:
                                infos = Service().buscar_info_por_um_campo_generico('*', 'musicas', 'album', (info[1],))

                        case "pessoa":
                            if info is not None:
                                infos = Service().buscar_info_por_um_campo_generico('*', 'musicas', 'pessoa', (info[1],))
                                infos = [inf for inf in infos if info[1] == inf[3]]


                    if (infos is None or len(infos) == 0) and db_tag != "id":
                        raise ValidationError("Informacao não encontrada.")
                else:
                    if (self.alvo == 'nota' or self.alvo == 'afazer') and self.id > 0:
                        id_das_notas = Service().buscar_info_por_um_campo_generico(f'id_{self.alvo}', self.tabelas_alternativas[self.alvo], 'id_pessoa', (self.id,))
                        infos = []
                        for id in id_das_notas:
                            info_nota = Service().verificar_id(id[0], tabela)
                            if info_nota is not None:
                                infos.append(info_nota)

                    elif (self.alvo == 'contato' or self.alvo == 'gosto') and self.id > 0:
                        infos = Service().buscar_info_por_um_campo_generico('*', tabela, 'pessoa', (self.id,))

                    elif self.alvo == 'album' and self.id > 0:
                        infos = Service().buscar_info_por_um_campo_generico('*', tabela, 'banda', (self.id,))

                    elif self.alvo == 'musica' and self.id > 0:
                        infos = Service().buscar_info_por_um_campo_generico('*', tabela, 'album', (self.id,))

                    else:
                        infos = Service().ver_tudo(self.tabelas[self.alvo])

                    if len(infos) < 1:
                        raise ValidationError("Informacões não encontradas.")

                if infos is not None:
                    livro = Livro(self.tabelas[self.alvo].capitalize())
                    indices = {}
                    conteudo = []
                    
                    if isinstance(infos, list):
                        for info in infos:
                            info = tb.ajeitar_info_mysql(info, self.alvo)
                            indices[str(info[0])] = info
                            conteudo.append(tb.montar_info(info, self.alvo))
                    elif isinstance(infos, tuple):
                        infos = tb.ajeitar_info_mysql(infos, self.alvo)
                        indices[str(infos[0])] = infos
                        conteudo.append(tb.montar_info(infos, self.alvo))

                    livro.adicionar_conteudo(conteudo)

                    while running:
                        if db_tag == "id":
                            answer = infos[0]

                        else:
                            print("- - Avisos:\n | '<' Pág. Anterior\n | '>' Próx. Página\n | 'pn' Com n sendo o número da página - -\n")

                            livro.mostrar_pagina

                            paginas = f"{livro.pagina_atual}/{livro.numero_de_paginas}"
                            print(f"Página Atual: {paginas}\n")
                            answer = input("ID: ")

                            os.system('cls')

                        try:
                            int(answer)

                            if answer in indices.keys():
                                if self.acao == "" or self.acao == "freeway":
                                    nova_interface = Interface(tipo_interface='op_num', titulo=f"gerenciar ({self.alvo})", alvo=self.alvo, acao='gerenciar', db_info=list(indices[answer]))
                                    nova_interface.montar()
                                    running = False
                                    
                                elif self.acao == "pescar":
                                    match self.alvo:
                                        case 'pessoa':
                                            nome_ou_apelido = Service().nome_ou_apelido(int(answer))
                                            info_pescar = tb.montar_id_pessoa(int(answer), nome_ou_apelido)
                                        
                                        case 'album':
                                            info_album = Service().verificar_id(int(answer), "albuns")
                                            info_pescar = (info_album[1], int(answer))

                                        case 'banda':
                                            info_banda = Service().verificar_id(int(answer), "bandas")
                                            info_pescar = (info_banda[1], int(answer))

                                    self.retornar = True
                                    return info_pescar
                                
                            else:
                                print("- - ID inválido! - -\n")

                        except:
                            if answer == "":
                                running = False

                            elif answer == "<":
                                livro.pagina_anterior

                            elif answer == ">":
                                livro.proxima_pagina

                            elif answer[0] == "p" and tb.apenas_numeros(answer[1:]):
                                livro.mudar_pagina(int(answer[1:]))

                            else:
                                print("- - Valor inválido! - -\n")

            except ValidationError as e:
                print(f"- - {e.mensagem} - -")

    def ver_calendario(self) -> None:
        tipo_calendario = self.titulo.lower()
        self.running = False
        running = True

        match tipo_calendario:
            case 'mes':
                info_adicional = '\n- - "c" para escolher mes/ano'

            case 'dia':
                info_adicional = '\n- - "c" para escolher dia/mes/ano'

            case _:
                info_adicional = ''
        
        calendario = Calendario(tipo_calendario)
        
        while running:
            avisos = (
                f'- - Aviso: {calendario.info} | "0" para acessar afazeres não agendados\n'
                + '- - "n#" para acessar as notas do dia #, "a#" para acessar os afazeres\n'
                + f'- - "b#" para acessar as informações do(s) aniversariante(s){info_adicional}\n'
                + '- - Digite apenas o dia para acessar o diario - -\n\n'
            )
            print(avisos)
            calendario.mostrar
            
            answer = input('\n\nEscolha: ')
            os.system('cls')

            try:
                try:
                    dia = int(answer)

                    if dia == 0:
                        raise Exception
                    
                    if dia in calendario.indices:
                        diario = Interface(tipo_interface='ver_diario', titulo='Diario', alvo='diario', dia_diario=tb.mysql_date_para_data(date(calendario.data.year, calendario.data.month, dia)))
                        diario.montar()

                    else:
                        print("- - Escolha um dia presente no calendário. - -\n")
                        
                except:
                    tipo_selecao = ''

                    if answer != '0':
                        if (answer[0] == 'a' or answer[0] == 'n' or answer[0] == 'b') and tb.apenas_numeros(answer[1:]):
                            num = answer[1:]
                            if answer[0] == 'a':
                                tipo_selecao = 'afazer:afazeres'
                            elif answer[0] == 'b':
                                tipo_selecao = 'pessoa:aniversario'
                            else:
                                tipo_selecao = 'nota:notas'
                        else:
                            num = answer
                    else:
                        num = answer
                        tipo_selecao = 'afazer:afazeres'

                    num = int(num)

                    if num in calendario.indices and tipo_selecao != '':
                        if len(calendario.conteudo_dias[num][tipo_selecao.split(':')[1]]) > 0:
                            if tipo_selecao.split(':')[0] != 'pessoa':
                                nova_interface = self.build_get_info(info='calendario', tipo=tipo_selecao.split(':')[0], ids_disponiveis=set(calendario.conteudo_dias[num][tipo_selecao.split(':')[1]]))
                            else:
                                nova_interface = self.build_get_info(info='calendario', tipo=tipo_selecao.split(':')[0], ids_disponiveis=set([tupla[0] for tupla in calendario.conteudo_dias[num][tipo_selecao.split(':')[1]]]))
                            nova_interface.montar()
                        
                        else:
                            match tipo_selecao.split(':')[0]:
                                case 'nota':
                                    print(f"- - Dia escolhido não possue nenhuma nota! - -\n")
                                
                                case 'afazer':
                                    print(f"- - Dia escolhido não possue nenhum afazer! - -\n")
                                
                                case 'pessoa':
                                    print(f"- - Dia escolhido não possue nenhum aniversário! - -\n")

                    else:
                        print("- - Escolha um dia presente no calendário ou 0 se houver algum afazer não agendado! - -\n")

            except:
                if answer == '':
                    running = False

                elif answer == '<':
                    calendario.anterior

                elif answer == '>':
                    calendario.proximo

                elif answer == 'c' and (calendario.tipo == 'mes' or calendario.tipo == 'dia'):
                    if calendario.tipo == 'mes':
                        interface = self.build_get_info('data', 'calendario')
                    else:
                        interface = self.build_get_info('data de nascimento', 'pessoa')

                    info = interface.montar()

                    if calendario.tipo == 'dia' and info is not None:
                        info = tb.formatar_data(info)

                    if info is not None:
                        calendario.mudar_data(info)

                else:
                    print("- - Valor inválido! - -\n")

    def ver_diario(self) -> None:
        pagina_diario = "\n"
        indices = {
            'pessoa': [],
            'nota': [],
            'afazer': []
        }

        for value in self.calendario.conteudo_dias.values():
            if len(value['aniversario']) != 0:
                pagina_diario += 'Aniversariantes:\n'
                for aniversario in value['aniversario']:
                    info_pessoa = Service().verificar_id(aniversario[0], 'pessoas')
                    pagina_diario += f"- (ID:{info_pessoa[0]}) {tb.montar_nome(info_pessoa[1], info_pessoa[2], info_pessoa[3])}\n"
                    indices['pessoa'].append(info_pessoa[0])

                pagina_diario += '\n'

            if len(value['afazeres']) != 0:
                afazer_nao_agendado = []
                afazer_agendado = []

                for afazer in value['afazeres']:
                    info_afazer = Service().verificar_id(afazer, 'afazeres')
                    
                    if info_afazer[4] is None:
                        afazer_nao_agendado.append(info_afazer)
                    else:
                        afazer_agendado.append(info_afazer)

                afazer_agendado = sorted(afazer_agendado, key=lambda x: x[4])

                for afazer in afazer_agendado:
                    pagina_diario += (
                        f"(ID:{afazer[0]}) {afazer[1]}\n"
                        + (f"Data Final: {tb.mysql_date_para_data(afazer[3])}\n" if afazer[3] is not None else "")
                        + f"Horário: {afazer[4]}\n"
                        + (f"Repete: {afazer[5]}\n" if afazer[5] is not None else "")
                        + "Integrantes:\n"
                    )
                    indices['afazer'].append(afazer[0])
                    ids_pessoas = Service().buscar_info_por_um_campo_generico('id_pessoa', 'pessoas_afazeres', 'id_afazer', (afazer[0],))
                    for id_pessoa in ids_pessoas:
                        info_pessoa = Service().verificar_id(id_pessoa[0], 'pessoas')
                        pagina_diario += f"- {tb.montar_nome(info_pessoa[1], info_pessoa[2], info_pessoa[3])}\n"

                    if afazer != afazer_agendado[-1] or (afazer == afazer_agendado[-1] and (len(afazer_nao_agendado) > 0 or len(value['notas'])) > 0):
                        pagina_diario += "\n"

                for afazer in afazer_nao_agendado:
                    pagina_diario += (
                        f"(ID:{afazer[0]}) {afazer[1]}\n"
                        + (f"Data Final: {tb.mysql_date_para_data(afazer[3])}\n" if afazer[3] is not None else "")
                        + (f"Repete: {afazer[5]}\n" if afazer[5] is not None else "")
                        + "Integrantes:\n"
                    )
                    indices['afazer'].append(afazer[0])
                    ids_pessoas = Service().buscar_info_por_um_campo_generico('id_pessoa', 'pessoas_afazeres', 'id_afazer', (afazer[0],))
                    for id_pessoa in ids_pessoas:
                        info_pessoa = Service().verificar_id(id_pessoa[0], 'pessoas')
                        pagina_diario += f"- {tb.montar_nome(info_pessoa[1], info_pessoa[2], info_pessoa[3])}\n"

                    if afazer != afazer_nao_agendado[-1] or (afazer == afazer_nao_agendado[-1] and len(value['notas']) > 0):
                        pagina_diario += "\n"

            if len(value['notas']) != 0:
                for nota in value['notas']:
                    info_nota = Service().verificar_id(nota, 'notas') 

                    pagina_diario += f"(ID:{nota}) {tb.mysql_datetime_para_data(info_nota[2])}\n"
                    indices['nota'].append(nota)
                    pagina_diario += f"Pessoas Citadas:\n"
                    
                    ids_pessoas = Service().buscar_info_por_um_campo_generico('id_pessoa', 'pessoas_notas', 'id_nota', (nota,))
                    for id_pessoa in ids_pessoas:
                        info_pessoa = Service().verificar_id(id_pessoa[0], 'pessoas')
                        pagina_diario += f"- {tb.montar_nome(info_pessoa[1], info_pessoa[2], info_pessoa[3])}\n"

                    pagina_diario += f"{info_nota[1]}\n"

                    if nota != value['notas'][-1]:
                        pagina_diario += "\n"

            if tb.listas_de_dicionario_sem_itens(value):
                pagina_diario += "Nenhum evento registrado nesse dia."

            break

        painel = Panel(pagina_diario, title=self.calendario.data_formatada, border_style="yellow on black", style="yellow on black", box=ASCII, width=90)
        self.console.print(Align.center(painel))

        instrucoes = (
            '- - "<" | Página anterior\n'
            + '- - ">" | Próxima pagina\n'
            + '- - "a#" | Acessar afazer #\n'
            + '- - "n#" | Acessar nota #\n'
            + '- - "b#" | Acessar aniversariante #\n'
        )
        
        print(instrucoes)

        answer = input()
        os.system('cls')

        try:
            int(answer)

        except:
            if answer == '':
                self.running = False

            elif answer[0] in ['a', 'b', 'n'] and tb.apenas_numeros(answer[1:]):
                indice = int(answer[1:])

                def verificar_indice(tipo: str):
                    if indice in indices[tipo]:
                        nova_interface = Interface(tipo_interface='ver_info', titulo='id', alvo=tipo, acao='freeway', id=indice)
                        nova_interface.montar()

                    else:
                        print("- - ID não existe ou não está presente nessa página! - -\n")
                        input()
                        os.system('cls')

                if answer[0] == 'a':
                    verificar_indice('afazer')

                elif answer[0] == 'n':
                    verificar_indice('nota')

                elif answer[0] == 'b':
                    verificar_indice('pessoa')

                self.calendario.atualizar

            elif answer == '<':
                retornando = True
                while retornando:
                    self.calendario.anterior
                    self.calendario.atualizar
                    for value in self.calendario.conteudo_dias.values():
                        if not tb.listas_de_dicionario_sem_itens(value):
                            retornando = False
                        break

            elif answer == '>':
                prosseguindo = True
                while prosseguindo:
                    self.calendario.proximo
                    self.calendario.atualizar
                    for value in self.calendario.conteudo_dias.values():
                        if not tb.listas_de_dicionario_sem_itens(value):
                            prosseguindo = False
                        break

            else:
                print("- - Valor inválido! - -\n")
                input()
                os.system('cls')

# ------------------

    @classmethod
    def inicio(cls):
        instancia = cls(tipo_interface="op_num", titulo="inicio", alvo="geral")
        instancia.inserir_opcoes(["My Info", "Pessoas", "Notas", "Contatos", "Gostos", "Afazeres", "Calendario", "Do-Re-Mi", "Jogar"])
        return instancia

    @classmethod
    def build_get_info(cls, info: str, tipo: str, ids_disponiveis: set = set()):
        opcoes = []
        info = info.lower()
        acao = ""

        match info:
            case "status":
                if tipo == 'musica' or tipo == 'banda':
                    interface = "get_info_op"
                    opcoes += ['Muito interessante', 'Interessante', 'Pouco interessante', 'Hype', 'Veury Good', 'Boa', 'Mais ou menos', 'Menos', 'Não curti', 'Enjoei', 'Ainda nao sei dizer']

                elif tipo != 'afazer':
                    interface = "get_info_op"

                    opcoes += ['Interesse', 'Terminei']

                    match tipo:
                        case 'manga':
                            opcoes += ['Pausado', 'Lendo']
                        case 'anime' | 'serie':
                            opcoes += ['Pausado', 'Assistindo']
                        case 'filme':
                            opcoes += ['Assistindo']
                        case 'jogo':
                            opcoes += ['Pausado', 'Jogo as vezes', 'Jogo regularmente']
                else:
                    interface = "escolhas"
                    opcoes += [("Ativo", True), ("Desativado", False)]

            case "tipo":
                interface = "get_info_op"
                if tipo == 'album':
                    opcoes += ['Album', 'EP', 'Single', 'Soundtrack']
                else:
                    opcoes += ['Numero', 'Discord', 'Instagram', 'Email', 'Github']

            case "parentesco":
                interface = "get_info_op"
                opcoes += ["Minha pessoa", "Pai", "Mãe", "Avo", "Tio", "Tia", "Dindo", "Dinda", "Primo", "Prima", "Irmão", "Irmã", "Amigo", "Amiga", "Conhecido", "Amigo de um amigo"]

            case "proximidade":
                interface = "get_info_op"
                opcoes += ["Proximos", "Distantes", "Conversando", "Rotina"]

            case "pessoa" | "pessoa que recomendou":
                interface = "op_num"
                acao = "pescar"
                tipo = "pessoa"

            case "banda":
                interface = "op_num"
                acao = "pescar"
                tipo = "banda"

            case "album":
                interface = "op_num"
                acao = "pescar"
                tipo = "album"

            case "pessoas citadas":
                interface = "op_num"
                acao = "pescar"
                tipo = "pessoa"

            case "remover pessoa":
                interface = 'ver_info'
                acao = 'pescar'
                tipo = 'pessoa'

            case "calendario" | "recomendacoes":
                interface = 'ver_info'

            case "repetir":
                interface = "selected_info"
                opcoes += ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'diariamente', 'semanalmente', 'mensalmente', 'anualmente', 'Registrar Mudanças']

            case _:
                interface = "get_info"

        if info not in ['pessoas citadas', 'remover pessoa', 'pessoa', 'calendario', 'recomendacoes', 'album', 'banda', 'pessoa que recomendou']:
            instancia = cls(tipo_interface=interface, titulo=f"{info}: ", alvo=tipo, acao=acao)
            instancia.inserir_opcoes(opcoes=opcoes)
        elif info in ['pessoa', 'pessoas citadas', 'album', 'banda', 'pessoa que recomendou']:
            instancia = cls(tipo_interface=interface, titulo=f"pescar ({tipo})", alvo=tipo, acao=acao)
        elif info in ['remover pessoa', 'calendario', 'recomendacoes']:
            instancia = cls(tipo_interface=interface, titulo='ids_especificos', alvo=tipo, acao=acao)
            instancia.ids_disponiveis = ids_disponiveis

        return instancia