import os
import ast
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'assets'))
from assets import *
from wheel.wheel_assets import *

def save(store):
    
    file = better_open('./points/store.txt', 'w')

    file.write(str(store))

    file.close()

store = better_open('./points/store.txt', 'r')
scores = ast.literal_eval(store.read())
store.close()

wheel_store = better_open('./wheel/store.txt', 'r')
wheel_scores = ast.literal_eval(wheel_store.read())
wheel_store.close()


while True:
    
    name, owenpoints = input("Input name:::owenpoints").split(":::")
    owenpoints = int(owenpoints)
    
    if name == "break123":
        break

    scores[name] -= owenpoints
    wheel_scores[name] += owenpoints



save(scores)

wheel_save(wheel_scores)
