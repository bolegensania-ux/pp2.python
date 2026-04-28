from db import *
from game import run_game

username = input("Enter username: ")

create_tables()
best = get_personal_best(username)

score, level = run_game(best)

save_game(username, score, level)

print("Top 10:")
for row in get_top_scores():
    print(row)