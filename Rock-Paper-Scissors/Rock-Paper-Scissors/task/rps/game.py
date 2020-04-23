# Write your code here
import random

classic_options = ['rock', 'scissors', 'paper']
options_5 = ['rock', 'paper', 'scissors', 'lizard', 'spock']
options_15 = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge',
              'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']

classic_bits = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
bits_5 = {'rock': ['lizard', 'scissors'], 'paper': ['rock', 'spock'],
          'scissors': ['lizard', 'paper'], 'lizard': ['paper', 'spock'],
          'spock': ['scissors', 'rock']}
bits_15 = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
           'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
           'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
           'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
           'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
           'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
           'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
           'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
           'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
           'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
           'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
           'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
           'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
           'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
           'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}
bits = {}
rating_file = open('rating.txt')
rating_mas = rating_file.read().split()
people_rating = {}
for i in range(0, len(rating_mas), 2):
    people_rating[rating_mas[i]] = rating_mas[i + 1]

name = input('Enter your name:')
print('Hello,', name)

if name in people_rating:
    rating = int(people_rating[name])
else:
    rating = 0

options = input().split(',')
print("Okay, let's start")
options.sort()
options_5.sort()
options_15.sort()
classic_options.sort()
if options == [''] or options == classic_options:
    options = classic_options
    bits = classic_bits
elif options == options_5:
    bits = bits_5
elif options == options_15:
    bits = bits_15
else:
    for i in options:
        bits[i] = []
    quantity_elem = int(len(options) / 2)
    for i in range(1, quantity_elem + 1):
        for j in range(len(options)):
            bits[options[j]].append(options[(j + i + quantity_elem) % len(options)])

while True:
    player_choice = input()
    robot_choice = random.choice(options)
    if player_choice == '!exit':
        print('Bye!')
        break
    elif player_choice == '!rating':
        print('Your rating:', rating)
    elif player_choice not in options:
        print('Invalid input')
    elif player_choice == robot_choice:
        print('There is a draw ({})'.format(robot_choice))
        rating += 50
    elif robot_choice in bits[player_choice]:
        print('Well done. Computer chose', robot_choice, 'and failed')
        rating += 100
    elif player_choice in bits[robot_choice]:
        print('Sorry, but computer chose', robot_choice)
