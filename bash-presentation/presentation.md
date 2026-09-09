# BASH (Bourne-Again Shell) // NVIM - Tips & Tricks
---

## Para usuários de Windows
---

1. Abrir o `cmd`;
2. `wsl.exe --install`;
3. Reiniciar;
4. `wsl --install -d ubuntu`.

> [!NOTE]
> RTJ
> KEYK

## Comandos básicos
---

> [!INFO] Criar diretório
> ```bash
> mkdir teste
> ```

> [!INFO] Criar arquivo
> ```bash
> touch teste.txt
> ```

> [!INFO] Deletar arquivo
> ```bash
> rm teste.txt
> ```

> [!INFO] Deletar diretório vazio
> ```bash
> rmdir teste/
> ```

> [!INFO] Deletar diretório e arquivos/diretórios aninhados
> ```bash
> rm -rf teste/
> ```

## Comandos básicos
---

> [!INFO] Listar arquivos/diretórios
> ```bash
> ls
> ```

> [!INFO] Mover para o diretório
> ```bash
> cd teste/
> ```

> [!INFO] Caminho do diretório atual para stdout
> ```bash
> pwd
> ```

> [!INFO] Caracteres para stdout
> ```bash
> echo "testando..."
> ```

> [!INFO] Conteúdo do arquivo para stdout
> ```bash
> cat teste.txt
> ```

## Comanos básicos
---

> [!INFO] Copiar arquivos
> ```bash
> cp caminho/arquivo.txt caminho/de/destino/
> cp caminho/arquivo.txt caminho/de/destino/novo_nome.txt
> ```

> [!INFO] Mover arquivo/diretório
> ```bash
> mv teste.txt caminho/de/destino/
> mv teste.txt caminho/de/destino/teste2.txt
> ```

> [!INFO] Conteúdo do arquivo para stdout
> ```bash
> cat teste.txt
> ```

## Utilidades
---

> [!INFO] Procurar por caracteres em diversos arquivos
>
> ```bash 
> grep -r "caracter" .
> ```
>
> - grep: comando
> - -r: procura de forma recursiva
> - "caracter": sequencia de caracteres a ser pesquisada
> - .: diretório onde a busca será efetuada

> [!INFO] Redirecionar stdout para stdin 
>
> ```bash 
> tree | wl-copy
> ```

> [!WARNING] sudo apt install tree

> [!INFO] Cria um arquivo a partir do stdout
>
> ```bash 
> echo "testando..." > teste.txt
> ```
>

> [!INFO] Adiciona stdout ao fim de um arquivo
>
> ```bash 
> echo "testando..." >> test.txt
> ```

## Utilidades


> [!INFO] nmap
>
> Mapear endereços de IP presentes na rede

> [!INFO] aria2
>
> Download de arquivos.

> [!INFO] Adiciona stdout ao fim de um arquivo
>
> ```bash 
> echo "testando..." >> test.txt
> ```
