unit = 1
#A:Archer
#S:Soldier
#K:Knight
commander1 = []
commander2 = []
commander1_money = 10
commander2_money = 10
#print(commander1)
import sys



def fight(commander1,commander2):
    #getting the length of the soldiers in each commanders army
    #infinite while loop until the results come in
    print('\n\n')
    while True:
        if(len(commander1) and len(commander2)):
            #calling the 
            fight_result = individual_fight(commander1[0],commander2[0])
            print('#RESULT')
            if(fight_result == 0):
                print('Its a tie')
                commander1.pop(0)
                commander2.pop(0)
            elif(fight_result == -1):
                print('C1 wins this round')
                commander2.pop(0)
            elif(fight_result == 1):
                print('C2 wins this round')
                commander1.pop(0)
            print('\n')
        else:
            break
    if(len(commander1)):
        print('#FINAL RESULT')
        print('C1 Wins the Battle')
    else:
        print('#FINAL RESULT')
        print('C2 Wins the Battle')



def individual_fight(commander1_soldier,commander2_soldier):

    #checking which type of soldier wins
    #return logic
    #return 0 if its a tie
    #return -1 if commander1 wins
    #return 1 if commander2 wins
    print('#FIGHT')
    print('C1:['+commander1_soldier+'] v/s '+'C2:['+commander2_soldier+']')
    if(commander1_soldier == 'Archer' and commander2_soldier == 'Archer'):
        return 0
    elif(commander1_soldier == 'Archer' and commander2_soldier == 'Soldier'):
        return -1
    elif(commander1_soldier == 'Archer' and commander2_soldier == 'Knight'):
        return 1
    elif(commander1_soldier == 'Soldier' and commander2_soldier == 'Archer'):
        return 1
    elif(commander1_soldier == 'Soldier' and commander2_soldier == 'Soldier'):
        return 0
    elif(commander1_soldier == 'Soldier' and commander2_soldier == 'Knight'):
        return -1
    elif(commander1_soldier == 'Knight' and commander2_soldier == 'Archer'):
        return -1
    elif(commander1_soldier == 'Knight' and commander2_soldier == 'Soldier'):
        return 1
    elif(commander1_soldier == 'Knight' and commander2_soldier == 'Knight'):
        return 0


#print('Let the fight begin')
#fight(commander1,commander2)
#query_yes_no("Start the fight?")




#Building a tool here 


def select_army_commander1():
    print('\n\n')
    print('Commander 1 chooses first')
    print('Each commander has $10 with them and each unit costs $1')
    print('A:Archer, S:Soldier, K:Knight, D:Done')
    question = 'Choice'
    prompt = '[A/S/K/D] '
    global commander1_money
    global commander1
    
    while True:
        # converting integer to string
        money = '($'+str(commander1_money)+'): '
        sys.stdout.write(question + prompt + money)
        choice = raw_input()
        valid = {"D": True, "A": True, "S": True, "K": True, "d": True, "a": True, "s": True, "k": True}
        if (choice in valid and commander1_money > 1) :
            if(choice == 'D' or choice == 'd'):
                select_army_commander2()
                return True
            elif(choice == 'A' or choice == 'a'):
                commander1.append('Archer')
                commander1_money = commander1_money - 1
            elif(choice == 'K' or choice == 'k'):
                commander1.append('Knight')
                commander1_money = commander1_money - 1
            elif(choice == 'S' or choice == 's'):
                commander1.append('Soldier')
                commander1_money = commander1_money - 1
        elif (commander1_money == 1):
            print('The Commander is out of money!!')
            select_army_commander2()
            return True
        else:    
            sys.stdout.write("Please respond with [A/S/K/D]\n")


def select_army_commander2():
    print('\n\n')
    print('Commander 2 chooses now')
    print('Each commander has $10 with them and each unit costs $1')
    print('A:Archer, S:Soldier, K:Knight, D:Done')
    question = 'Choice'
    prompt = '[A/S/K/D] '
    global commander2_money
    global commander2
    global commander1
    while True:
        # converting integer to string
        money = '($'+str(commander2_money)+'): '
        sys.stdout.write(question + prompt + money)
        choice = raw_input()
        valid = {"D": True, "A": True, "S": True, "K": True,
                 "d": True, "a": True, "s": True, "k": True}
        if (choice in valid and commander2_money > 1):
            if(choice == 'D' or choice == 'd'):
                start_battle()
                return True
            elif(choice == 'A' or choice == 'a'):
                commander2.append('Archer')
                commander2_money = commander2_money - 1
            elif(choice == 'K' or choice == 'k'):
                commander2.append('Knight')
                commander2_money = commander2_money - 1
            elif(choice == 'S' or choice == 's'):
                commander2.append('Soldier')
                commander2_money = commander2_money - 1
        elif (commander1_money == 1):
            print('The Commander is out of money!!')
            start_battle()
            return True
        else:
            sys.stdout.write("Please respond with [A/S/K/D]\n")


def start_game():
    print('\n')
    print('#COMBAT')
    print('\n')
    print("Each unit has a weakness and a strength.")
    print("Archers are good against Soldiers but are terrible against Knights.")
    print("Soldiers are good against Knights but cant win against Archers.")
    print("Knights beat Archers, but fall short against Soldiers.")
    print("If a unit comes up against a unit of the same type, both lose.")
    print('\n')
    question = 'Do you wish to start the game'
    prompt = '[Y/n]'

    while True:

        sys.stdout.write(question + prompt)
        choice = raw_input()
        valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
        if choice in valid:
            select_army_commander1()
            return True
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
    

def start_battle():
    print('\n')
    print('#BATTLE')
    
    question = 'Do you wish to start the battle'
    prompt = '[Y/n]'

    while True:

        sys.stdout.write(question + prompt)
        choice = raw_input()
        valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
        if choice in valid:
            sys.stdout.write("Let the Battle Begin")
            fight(commander1, commander2)
            return True
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")



start_game()
