unit = 1
#A:Archer
#S:Soldier
#K:Knight
commander1 = []
commander2 = []
commander1_money = 10
commander2_money = 10
commander1_medics = 0
commander2_medics = 0

#print(commander1)
import sys



def fight(commander1,commander2,commander1_medics,commander2_medics):
    #getting the length of the soldiers in each commanders army
    #infinite while loop until the results come in
    print('\n\n')
    print(commander1)
    print(commander2)
    
    while True:
        if(len(commander1) and len(commander2)):
            #calling the 
            fight_result = individual_fight(commander1[0],commander2[0])
            print('#RESULT')
            if(fight_result == 0):
                print('Its a tie')
                if(commander1_medics > 0):
                    print("Commander1's medic healed its " + commander1[0] + ", Medics remaining:"+str(commander1_medics))
                    commander1.append(commander1[0])
                    commander1_medics = commander1_medics - 1
                if(commander2_medics > 0):
                    print("Commander2's medic healed its " + commander2[0] + ", Medics remaining:"+str(commander2_medics))
                    commander2.append(commander2[0])
                    commander2_medics = commander2_medics - 1
                commander1.pop(0)
                commander2.pop(0)
            elif(fight_result == -1):
                print('C1 wins this round')
                if(commander2_medics > 0):
                    print("Commander2's medic healed its " + commander2[0] + ", Medics remaining:"+str(commander2_medics))
                    commander2_medics = commander2_medics - 1
                    commander2.append(commander2[0])
                commander2.pop(0)
            elif(fight_result == 1):
                print('C2 wins this round')
                if(commander1_medics > 0):
                    print("Commander1's medic healed its " + commander1[0] + ", Medics remaining:"+str(commander1_medics))
                    commander1_medics = commander1_medics - 1
                    commander1.append(commander1[0])
                commander1.pop(0)
            print('\n')
        else:
            break
    if(len(commander1)):
        print('#FINAL RESULT')
        print('C1 Wins the Battle')
    elif(len(commander2)):
        print('#FINAL RESULT')
        print('C2 Wins the Battle')
    else:
        print('#FINAL RESULT')
        print('Its a TIE')


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
    elif(commander1_soldier == 'Archer' and commander2_soldier == 'Seige Equipment'):
        return 1
    elif(commander1_soldier == 'Archer' and commander2_soldier == 'Wizard'):
        return -1
    elif(commander1_soldier == 'Soldier' and commander2_soldier == 'Archer'):
        return 1
    elif(commander1_soldier == 'Soldier' and commander2_soldier == 'Soldier'):
        return 0
    elif(commander1_soldier == 'Soldier' and commander2_soldier == 'Knight'):
        return -1
    elif(commander1_soldier == 'Soldier' and commander2_soldier == 'Seige Equipment'):
        return 1
    elif(commander1_soldier == 'Soldier' and commander2_soldier == 'Wizard'):
        return 1
    elif(commander1_soldier == 'Knight' and commander2_soldier == 'Archer'):
        return -1
    elif(commander1_soldier == 'Knight' and commander2_soldier == 'Soldier'):
        return 1
    elif(commander1_soldier == 'Knight' and commander2_soldier == 'Knight'):
        return 0
    elif(commander1_soldier == 'Knight' and commander2_soldier == 'Seige Equipment'):
        return 1
    elif(commander1_soldier == 'Knight' and commander2_soldier == 'Wizard'):
        return 1
    elif(commander1_soldier == 'Seige Equipment' and commander2_soldier == 'Archer'):
        return -1
    elif(commander1_soldier == 'Seige Equipment' and commander2_soldier == 'Soldier'):
        return -1
    elif(commander1_soldier == 'Seige Equipment' and commander2_soldier == 'Knight'):
        return 1
    elif(commander1_soldier == 'Seige Equipment' and commander2_soldier == 'Seige Equipment'):
        return 0
    elif(commander1_soldier == 'Seige Equipment' and commander2_soldier == 'Wizard'):
        return 1
    elif(commander1_soldier == 'Wizard' and commander2_soldier == 'Archer'):
        return -1
    elif(commander1_soldier == 'Wizard' and commander2_soldier == 'Soldier'):
        return -1
    elif(commander1_soldier == 'Wizard' and commander2_soldier == 'Knight'):
        return -1
    elif(commander1_soldier == 'Wizard' and commander2_soldier == 'Seige Equipment'):
        return -1
    elif(commander1_soldier == 'Wizard' and commander2_soldier == 'Wizard'):
        return 0
    


#print('Let the fight begin')
#fight(commander1,commander2)
#query_yes_no("Start the fight?")




#Building a tool here 


def select_army_commander1(commander1,commander2,commander1_money,commander2_money,commander1_medics,commander2_medics):
    print('\n\n')
    print('Commander 1 chooses first')
    print('Each commander has $10 with them and each unit costs $1')
    print('A:Archer, S:Soldier, K:Knight, M:Medics, E:Seige Equipment, W:Wizard, D:Done')
    question = 'Choice'
    prompt = '[A/S/K/M/E/W/D] '
    
    
    while True:
        # converting integer to string
        if(commander1_money == 0):
            print('The Commander is out of money!!')
            print('Commander1 has '+ str(commander1_medics) + ' medics!')
            select_army_commander2(commander1, commander2, commander1_money, commander2_money, commander1_medics, commander2_medics)
            return True
        else:
            money = '($'+str(commander1_money)+'): '
            sys.stdout.write(question + prompt + money)
            choice = raw_input()
            valid = {"D": True, "A": True, "S": True, "K": True, "d": True, "a": True, "s": True, "k": True, "M": True, "m": True, "E": True, "e": True, "W": True, "w": True}
            if (choice in valid and commander1_money > 0) :
                if(choice == 'D' or choice == 'd'):
                    commander1_medics = commander1_medics + commander1_money
                    print('Commander1 has ' + str(commander1_medics) + ' medics!')
                    select_army_commander2(commander1,commander2,commander1_money,commander2_money,commander1_medics,commander2_medics)
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
                elif(choice == 'E' or choice == 'e'):
                    commander2.append('Seige Equipment')
                    commander2_money = commander2_money - 1
                elif(choice == 'W' or choice == 'w'):
                    commander2.append('Wizard')
                    commander2_money = commander2_money - 1
                elif(choice == 'M' or choice == 'm'):
                    commander1_medics = commander1_medics + 1
                    commander1_money = commander1_money - 1
            else:    
                sys.stdout.write("Please respond with [A/S/K/M/D]\n")


def select_army_commander2(commander1,commander2,commander1_money,commander2_money,commander1_medics,commander2_medics):
    print('\n\n')
    print('Commander 2 chooses now')
    print('Each commander has $10 with them and each unit costs $1')
    print('A:Archer, S:Soldier, K:Knight, M:Medics, E:Seige Equipment, W:Wizard, D:Done')
    question = 'Choice'
    prompt = '[A/S/K/M/E/W/D] '
    
    while True:
        # converting integer to string
        if(commander2_money == 0):
            print('The Commander is out of money!!')
            print('Commander2 has ' + str(commander2_medics) + ' medics!')
            start_battle(commander1, commander2, commander1_money, commander2_money, commander1_medics, commander2_medics)
            return True
        else:
            money = '($'+str(commander2_money)+'): '
            sys.stdout.write(question + prompt + money)
            choice = raw_input()
            valid = {"D": True, "A": True, "S": True, "K": True, "d": True, "a": True, "s": True, "k": True, "M": True, "m": True, "E": True, "e": True, "W": True, "w": True}
            if (choice in valid and commander2_money > 0):
                if(choice == 'D' or choice == 'd'):
                    commander2_medics = commander2_medics + commander2_money
                    print('Commander2 has ' + str(commander2_medics) + ' medics!')
                    start_battle(commander1,commander2,commander1_money,commander2_money,commander1_medics,commander2_medics)
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
                elif(choice == 'E' or choice == 'e'):
                    commander2.append('Seige Equipment')
                    commander2_money = commander2_money - 1
                elif(choice == 'W' or choice == 'w'):
                    commander2.append('Wizard')
                    commander2_money = commander2_money - 1
                elif(choice == 'M' or choice == 'm'):
                    commander2_medics = commander2_medics + 1
                    commander2_money = commander2_money - 1
            else:
                sys.stdout.write("Please respond with [A/S/K/M/D]\n")


def start_game(commander1,commander2,commander1_money,commander2_money,commander1_medics,commander2_medics):
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
            select_army_commander1(commander1,commander2,commander1_money,commander2_money,commander1_medics,commander2_medics)
            return True
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
    

def start_battle(commander1,commander2,commander1_money,commander2_money,commander1_medics,commander2_medics):
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
            fight(commander1, commander2, commander1_medics, commander2_medics)
            return True
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")



start_game(commander1,commander2,commander1_money,commander2_money,commander1_medics,commander2_medics)
