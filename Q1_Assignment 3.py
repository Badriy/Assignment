import random
def Roll_dice():
    return random.randint(1,6)
def play_craps():
    point=0
    while True:
        dic1 = Roll_dice()
        dic2 = Roll_dice()
        t1 = dic1 + dic2
        print("You rolled", dic1,"+", dic2, "=", t1)
       
        if t1 == 7 or t1 == 11:
            print("You win!")
            break
        elif t1 ==2 or t1 ==3 or t1 ==12:
            print("You Lose!")
            break
        elif point ==0:
            point = t1
            print("Point is: ", point)
        elif t1 == point:
            print("You Win!")
            break
        elif t1 ==7:
            print("You lose!")
            break
play_craps()