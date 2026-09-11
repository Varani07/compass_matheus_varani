# BASH (Bourne-Again Shell) // NVIM - Tips & Tricks
---

## Para usuários de Windows
---

1. Abrir o `cmd`;
2. `wsl.exe --install`;
3. Reiniciar;
4. `wsl --install -d ubuntu`.

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

## Comandos básicos
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
---

> [!INFO] nmap
>
> Mapear endereços de IP presentes na rede

> [!INFO] aria2
>
> Download de arquivos.

> [!INFO] Linkar arquivos/diretórios
>
> ```bash 
> ln -s ~/repos/dotfiles/nvim ~/.config/nvim
> ```

## .bashrc
---

> [!INFO] Atualiza a sessão
>
> ```bash 
> source ~/.bashrc
> ```

> [!INFO] Alias
>
> ```bash 
> alias ll='ls -alF'
> alias la='ls -A'
> alias l='ls -CF'
> ```

## Scripts
---

> [!INFO] Loopings
>
> ```bash 
> while read -r path; do
>   path_completo="${path%%:*}"
>   clean_path="${path//:/}"
>   if [[ ${path_completo##*/} = "$repo" ]]; then
>       if [ $(( ${#path} - ${#clean_path} )) -eq 1 ]; then
>           linguagem="${path##*:}"
>       else
>           local resto="${path#*:}"
>           linguagem="${resto%%:*}"
>           ambiente="${resto##*:}"
>       fi
>       break
>   fi
> done < "$file"
> ```

> [!INFO] Condições
>
> ```bash
> if [ -d "$path_completo" ]; then
> ```


> [!INFO] Switch
>
> ```bash
> case $p2 in
>   rock) printf "p1" ;;
>   scissor) printf "p2" ;;
> esac
> ```

## Temas para explorar
---

- Variáveis do Shell
- Extensão de parâmetros
- Operadores Aritméticos/Teste/Redirecionamento
- Funções
- Autocomplete

## NVIM
---

- Modos
- Atalhos
- Plugins

## Modos
---

- Normal: Foco na utilização de atalhos e locomoção
- Inserção: Para preencher o arquivo
- Visual: Seleciona partes do arquivo
- Linha de comando: Interagir diretamente com o editor

## Atalhos
---

```lua
vim.g.mapleader = " "

vim.keymap.set("n", "<leader>tn", ":tabnew<CR>")
vim.keymap.set("n", "<leader>1", "1gt")
vim.keymap.set("n", "<leader>2", "2gt")

vim.keymap.set("n", "<leader>w", vim.cmd.w)
vim.keymap.set("n", "qq", vim.cmd.q)
vim.keymap.set("n", "<leader>qq", vim.cmd.qa)
```

## Plugins
---

```lua
{
    "mbbill/undotree",
    "archibate/lualine-time",
    "numToStr/Comment.nvim",
}
```
