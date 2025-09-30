import random

def generate_round():
    index = random.randint(0, 16)
    right_answer = random.randint(0, 2)

    if right_answer == 0:
        ans1 = index
        ans2 = random.randint(0,16)
        if ans2 == ans1:
            while(ans2 == ans1):
                ans2 = random.randint(0, 16)
        ans3 = random.randint(0, 16)
        if ans3 == ans1:
            while(ans3 == ans1):
                ans3 = random.randint(0, 16)
        if ans3 == ans2:
            while(ans2 == ans3):
                ans2 = random.randint(0, 16)

    if right_answer == 1:
        ans2 = index
        ans1 = random.randint(0,16)
        if ans1 == ans2:
            while(ans1 == ans2):
                ans1 = random.randint(0, 16)
        ans3 = random.randint(0, 16)
        if ans3 == ans2:
            while(ans3 == ans2):
                ans3 = random.randint(0, 16)
        if ans3 == ans1:
            while(ans1 == ans3):
                ans1 = random.randint(0, 16)

    if right_answer == 2:
        ans3 = index
        ans1 = random.randint(0,16)
        if ans1 == ans3:
            while(ans1 == ans3):
                ans1 = random.randint(0, 16)
        ans2 = random.randint(0, 16)
        if ans2 == ans3:
            while(ans2 == ans3):
                ans2 = random.randint(0, 16)
        if ans2 == ans1:
            while(ans2 == ans1):
                ans1 = random.randint(0, 16)
                
    return index, ans1, ans2, ans3, right_answer

player_list = ["xootynator", "Rafis", "FlyingTuna", "mrekk",
               "Chicony", "Nirux", "BTMC", "WhiteCat", "NINERIK",
               "MrDinklepuss", "ALEPH", "Lifeline", "Spazza17", "Lemuze",
               "Zylice", "ryuk", "sst3w"]

