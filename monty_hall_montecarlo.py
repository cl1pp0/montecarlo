#!/usr/bin/python3

import random

i_max = 10000
doors = [1, 2, 3]
wins_stay = 0
wins_change = 0

for i in range(i_max):
    goats = list(doors)
    prize = random.choice(doors)
    goats.remove(prize)
    choice_1 = random.choice(doors)
    master_options = list(goats)
    if (choice_1 != prize):
        master_options.remove(choice_1)
    master_opened = random.choice(master_options)
    closed = list(doors)
    closed.remove(master_opened)

    if choice_1 == prize:
        wins_stay += 1

    choice_2 = list(closed)
    choice_2.remove(choice_1)
    if choice_2.pop() == prize:
        wins_change += 1

print("Stay  : Won %d times of %d (%5.2f %%)" % (wins_stay, i_max, wins_stay/i_max*100))
print("Change: Won %d times of %d (%5.2f %%)" % (wins_change, i_max, wins_change/i_max*100))
