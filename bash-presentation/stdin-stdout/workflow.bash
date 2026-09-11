#!/bin/bash

participantes=("python" "odin" "bash")

for player in "${participantes[@]}"; do
    if [[ "$player" == odin* ]]; then
        odin build -file -out:receiver main.odin
    fi
done

remover_participante() {
    local -n arr=$1
    local alvo=$2
    local novo_arr=()

    for i in "${arr[@]}"; do
        if [[ "$i" != "$alvo" ]]; then
            novo_arr+=("$i")
        fi
    done

    arr=("${novo_arr[@]}")
}

escolher_participante() {
    local -n arr=$1
    printf "%d" $((RANDOM % ${#arr[@]}))
}

verificar_ultimo_participar() {
    local -n arr=$1
    if [ ${#arr[@]} -lt 2 ]; then
        printf "false"
    else
        printf "true"
    fi
}

resgatar_output() {
    local player=$1
    local points=$2
    local challangers_points=$3
    local output
    case $player in
        python*)
            output=$(printf "%d\n%d" "$points" "$challangers_points" | python receiver.py)
            ;;
        odin*)
            output=$(printf "%d\n%d" "$points" "$challangers_points" | ./receiver)
            ;;
        bash*)
            output=$(printf '%d\\n%d' "$points" "$challangers_points" | ./receiver.bash)
            ;;
    esac
    printf "%s" "$output"
}

calcular_resultado() {
    local p1=$1
    local p2=$2

    if [[ "$p1" == "$p2" ]]; then
        printf "draw"
    else
        case $p1 in
            scissor)
                case $p2 in
                    paper) printf "p1" ;;
                    rock) printf "p2" ;;
                esac
                ;;
            paper)
                case $p2 in
                    rock) printf "p1" ;;
                    scissor) printf "p2" ;;
                esac
                ;;
            rock)
                case $p2 in
                    scissor) printf "p1" ;;
                    paper) printf "p2" ;;
                esac
                ;;
        esac
    fi
}

printf "\nJogo Iniciado\n\n"
p1_points=0
p2_points=0

while [[ $(verificar_ultimo_participar participantes) != "false" ]]; do
    player_1=$(escolher_participante participantes)
    player_2=$player_1
    while [[ "$player_1" == "$player_2" ]]; do
        player_2=$(escolher_participante participantes)
    done
    player_1="${participantes[$player_1]}"
    player_2="${participantes[$player_2]}"

    while true; do
        printf "Jogador 1: %s, pontuação: %d\nJogador 2: %s, pontuação: %d\n\n" "$player_1" "$p1_points" "$player_2" "$p2_points"
        sleep 0.5

        escolha_1=$(resgatar_output "$player_1" "$p1_points" "$p2_points")
        escolha_2=$(resgatar_output "$player_2" "$p2_points" "$p1_points")
        if [[ "$escolha_1" == "quit" ]]; then
            printf "player %s desistiu...\n\n" "$player_1"
            sleep 1.5
            remover_participante participantes "$player_1"
            p1_points=0
            p2_points=0
            break
        elif [[ "$escolha_2" == "quit" ]]; then
            printf "player %s desistiu...\n\n" "$player_2"
            sleep 1.5
            remover_participante participantes "$player_2"
            p1_points=0
            p2_points=0
            break
        fi

        printf "player 1 escolheu: %s\n" "$escolha_1"
        sleep 0.5
        printf "player 2 escolheu: %s\n" "$escolha_2"
        sleep 0.5
        resultado=$(calcular_resultado "$escolha_1" "$escolha_2")
        printf "Resultado: %s\n\n" "$resultado"
        sleep 1
        if [[ "$resultado" == "p1" ]]; then
            p1_points=$((p1_points + 1))
        elif [[ "$resultado" == "p2" ]]; then
            p2_points=$((p2_points + 1))
        fi
    done
done

rm receiver
printf "O Vencedor é: %s\n\n" "$participantes"
