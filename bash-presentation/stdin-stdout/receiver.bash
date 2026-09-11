#!/bin/bash

read -r input

arg_1="${input%%\\n*}"
arg_2="${input#*\\n}"

my_points=$((arg_1))
challanger_points=$((arg_2))

if [ $(( $challanger_points - $my_points )) -gt 1 ]; then
    printf "quit"
else
    options=("scissor" "rock" "paper")
    index=$((RANDOM % ${#options[@]}))
    printf "${options[$index]}"
fi
