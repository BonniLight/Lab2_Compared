import random
from difflib import SequenceMatcher

def dice_player_picks():
    inputed_user_list = []
    for i in range(5):
        temporary_user_list = int(input("Enter five of your guess: "))
        inputed_user_list.append(temporary_user_list)
    return inputed_user_list

def count_amount(random_dice_numbers):
    count_amount = {}
    for element in random_dice_numbers:
        if element in count_amount:
            count_amount[element] += 1
        else:
            count_amount[element] = 1    
    return count_amount

def count_amount_output(count_amount):
    for element, count in count_amount.items():
        print(f"Number {element} rolled {count} times ")

def similarity_check(random_dice_numbers, inputed_user_list):
    similarity = SequenceMatcher(None, random_dice_numbers, inputed_user_list).ratio() * 100
    print(f"Similarity between rolls: {similarity}%")
    return similarity

def results_output(similarity):
    if 0 <= similarity <= 25:
        print("You shouldn't go to Vegas")
    elif 26 <= similarity <= 50:
        print("Go to Vegas but don't bet big")
    elif 51 <= similarity <= 100:
        print("Forget Vegas, go buy a lottery ticket")
    else:
        print("The Game Broke")

# Main code
random_dice_numbers = [random.randint(1, 6) for _ in range(5)]
inputed_user_list = dice_player_picks()
count_amount_dict = count_amount(random_dice_numbers)
count_amount_output(count_amount_dict)
similarity = similarity_check(random_dice_numbers, inputed_user_list)
results_output(similarity)
