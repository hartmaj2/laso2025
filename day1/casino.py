"""
Reimplementation of casino game but using queue instead of recursion
"""

from typing import Callable


num_slots = 6
start_config = tuple(num_slots * [1])

# start_config = tuple([3,0,0])
best_config = start_config

prevs : dict[tuple,None|tuple] = {}
prevs[start_config] = None

"""
Problem: https://youtu.be/YdpFPHFE60w?si=PmiYPguzid2Qjn2u&t=823
(13:43)

For every slot:
- perform duplicate rule
- perform switch rule

Algoritmus:

1. updatuj max
2. pro vsechny validni pozice: (validni = neprazdna prihradka & neni moc vpravo)
3.  zkus hodit dva kaminky do nasledujici
4.  zkus prohodit dve nasledujici prihrady

"""

def print_info(slots: tuple):
    print(f"slots: {slots}, sum: {sum(slots)}")

def update_best(slots: tuple):
    global best_config
    if sum(slots) > sum(best_config):
        print_info(slots)
        best_config = slots

def test_range_with_func(slots : tuple, func : Callable, end_offset : int, configs : list[tuple]):
    global prevs
    for i in range(len(slots)-end_offset):
        if slots[i] == 0:
            continue
        new_slots = func(slots,i)
        if new_slots in prevs:
            continue
        prevs[new_slots] = slots
        configs.append(new_slots)


def run_sim(start_config : tuple):
    global prevs

    configs : list[tuple] = []

    configs.append(start_config)

    while configs:
        slots = configs.pop()
        update_best(slots)
        test_range_with_func(slots,duplicate,1,configs)
        test_range_with_func(slots,switch_slots,2,configs)
       
def duplicate(slots : tuple[int], i : int) -> tuple:
    new_slots = list(slots)
    new_slots[i] -= 1
    new_slots[i+1] += 2
    return tuple(new_slots)

def switch_slots(slots : tuple[int], i : int) -> tuple:
    new_slots = list(slots)
    new_slots[i] -= 1
    new_slots[i+1], new_slots[i+2] = new_slots[i+2], new_slots[i+1]
    return tuple(new_slots)

def print_path(config : tuple|None, prevs : dict[tuple,tuple|None]):
    while config != None:
        print(f" -> {config}")
        config = prevs[config]
    print()

try:
    run_sim(start_config)
except:
    print("Interrupted")
finally:
    print_info(best_config)
    print_path(best_config,prevs)
    


