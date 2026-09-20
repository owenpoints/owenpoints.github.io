import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'assets'))
from assets import *
import random

def wheel_output(store):

    file = better_open('./wheel/README.md', 'w')

    output_str = "# Global Wheel Points Rankings\n\n|Ranking|Name|Wheel Points|\n| ----------- | ----------- | ----------- |\n"
    
    store = dict(sorted(store.items(), key=lambda item: item[1]))
    store = {k: store[k] for k in reversed(store)}

    for i, item in enumerate(store):
        output_str += f"|{i + 1}.|{list(store)[i]}|{pretty_num(store[item])}|\n"

    output_str += "\n## 10 Wheel Points can be exchanged for 1 Owen Point\n"
    output_str += "\n## [Back](../) to Owen Points Leaderboard"

    file.write(output_str)
    file.close()

def quick_spin(num_spins):
    possible_outcomes = [-1, -1, -1, 3, 7, 8, 10, 15, 20]

    total = 0
    for _ in range(num_spins):
        total += random.choice(possible_outcomes)

    return total
