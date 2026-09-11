import sys
from random import choice

data = sys.stdin.read()
my_points, challanger_points = [int(item) for item in data.split("\n")]

options = ["scissor", "rock", "paper"]
option = choice(options)

if challanger_points - my_points > 1:
    print("quit", end="")
else:
    print(option, end="")
