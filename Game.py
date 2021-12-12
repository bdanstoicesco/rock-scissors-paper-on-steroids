import random
import sys

player_name = input("Enter your name: ")
player_rating, player_points = 0, 0
options, dict_list = list(), list()
list_x, plays = list(), dict()
print(f'Hello, {player_name}')
player_game_type = input().split(",")


def dict_play():
    my_input = player_game_type
    global list_x
    list_x = list()
    for j in range(len(my_input)):
        a, b = 1, (len(my_input) // 2 + 1)
        for x in my_input[a:b]:
            my_dict2 = dict.fromkeys([x], my_input[0])
            list_x.append(my_dict2)
        for y in my_input[b:]:
            my_dict1 = dict.fromkeys([my_input[0]], y)
            list_x.append(my_dict1)
        z = my_input.pop(my_input.index(my_input[0]))
        my_input.append(z)
    return list_x


def get_rating():
    global player_rating
    with open('rating.txt', 'r') as file:
        for line in file:
            if player_name in line:
                player_rating = int(line.lstrip(player_name))
    file.close()
    return player_rating


def update_rating():
    get_rating()
    global player_name
    global player_rating
    global player_points
    old_file = open('rating.txt', 'r')
    lines = old_file.readlines()
    old_file.close()
    new_file = open('rating.txt', 'w')
    for line in lines:
        if player_name in line:
            lines[lines.index(line)] = line.replace(f'{player_name} {player_rating}\n', f'{player_name} {player_rating + player_points}\n')
    new_file.writelines(lines)
    new_file.close()


def classic_game():
    while True:
        plays_ = ['rock', 'scissors', 'paper']
        user_plays_ = input()
        if user_plays_ == "!exit":
            print('Bye!')
            sys.exit()
        elif user_plays_ == '!rating':
            get_rating()
            print(f'Your rating: {player_rating}')
            continue
        elif user_plays_ not in plays:
            print('Invalid input')
            continue
        computer_plays_ = random.choice(plays_)
        if plays[user_plays_] == computer_plays_:
            print(f'Well done. The computer chose {computer_plays_} and failed')
            global player_points
            player_points = 100
            update_rating()
        if plays[computer_plays_] == user_plays_:
            print(f'Sorry, but the computer chose {computer_plays_}')
        if plays[computer_plays_] == plays[user_plays_]:
            print(f'There is a draw ({computer_plays_})')
            player_points = 50
            update_rating()


if player_game_type != ['']:
    dict_play()
    plays = list_x
    print("Okay, let's start")
else:
    plays = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    classic_game()


while True:
    user_plays = input()
    if user_plays == "!exit":
        print('Bye!')
        sys.exit()
    elif user_plays == '!rating':
        get_rating()
        print(f'Your rating: {player_rating}')
        continue
    elif user_plays not in player_game_type:
        print('Invalid input')
        continue
    computer_plays = random.choice(player_game_type)
    for i in range(len(list_x)):
        try:
            if list_x[i][user_plays] == computer_plays:
                print(f'Well done. The computer chose {computer_plays} and failed')
                player_points = 100
                update_rating()
                break
        except KeyError:
            pass
        try:
            if list_x[i][computer_plays] == user_plays:
                print(f'Sorry, but the computer chose {computer_plays}')
                break
        except KeyError:
            pass
        try:
            if computer_plays == user_plays:
                print(f'There is a draw ({computer_plays})')
                player_points = 50
                update_rating()
                break
        except KeyError:
            pass
