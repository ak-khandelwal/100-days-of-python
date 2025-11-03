
import random

difficulty_level = ""
while True:
    difficulty_level = input('please select difficulty easy/medium/hard ')
    if difficulty_level=='easy':
        break
    elif difficulty_level=='medium':
        break
    elif difficulty_level=='hard':
        break
    else:
        continue

if not difficulty_level:
    print('please set the difficulty ')
    exit()

difficulty_level_options = {
    'easy':15,
    'medium':10,
    'hard':5
}
wanna_replay = 'y'
while wanna_replay=='y':
    print('i am thinking of number between 1 to 100')
    print('i am selected the number, please guess the number ')
    actual_number = random.randint(1,100)
    print('acutal_number ',actual_number)
    lifes_rem = difficulty_level_options[difficulty_level]
    while lifes_rem:
        guessed_number = int(input('guess the number!!! '))
        diff = guessed_number - actual_number
        if diff == 0:
            break
        elif diff > 0:
            if diff >=20:
                print('too high')
                lifes_rem-=1
            elif diff >=10:
                print('high')
                lifes_rem-=1
            elif diff >=5:
                print('near')
                lifes_rem-=1
            else:
                print('too close')
                lifes_rem-=1
        else:
            if diff <= -20:
                print('too low')
                lifes_rem-=1
            elif diff <= -10:
                print('low')
                lifes_rem-=1
            elif diff <= -5:
                print('near')
                lifes_rem-=1
            else:
                print('too close')
                lifes_rem-=1
        print('life remaining: ',lifes_rem)
    if not lifes_rem:
        print('better luck next time!!!')
    else:
        # if life is not zero and still manages to reach here then
        # user has successfully guessed the number
        print('wow!! you nailed it')
    while True:
        wanna_replay = input('do you  want to play again? y/n ')
        if wanna_replay == 'y':
            break
        elif wanna_replay == 'n':
            break
        else:
            print('invalid input try again!!!')

    
print('ty for playing!!!')