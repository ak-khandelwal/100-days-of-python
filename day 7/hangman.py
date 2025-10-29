import random
import sys
word_list = ["aardvark", "baboon", "camel"]

original_word = random.choice(word_list)
print(original_word)
chosen_word = list(original_word)
question_word = []
question_word_len = 0
for curr in chosen_word:
    question_word.append('_')
    question_word_len+=1

# print(question_word_len,question_word)
total_life = 6
rem_life = 6

guessed_chars = set()
while rem_life:
    user_input = input('guess a character...').lower()
    if user_input < 'a' or user_input > 'z' or len(user_input)>1:
        print('not expected input, sorry, please try again !!!')
        continue
    if user_input in guessed_chars:
        print('you already guesses that character !!!')
        continue
    guessed_chars.add(user_input)
    is_char_found = False
    for idx, char in enumerate(chosen_word):
        if chosen_word[idx] == user_input:
            question_word[idx] = user_input
            is_char_found = True
            question_word_len-=1
    if not is_char_found:
        print("oops you lost a life here !!! ")
        rem_life-=1
        print(f'life remaining {rem_life}/{total_life}')
    else:
        # reset the variable
        print('you guessed it!!!')
        print(''.join(question_word))
    if question_word_len == 0:
        print('you won the game. Congo 🥳🥳')
        break

if rem_life == 0:
    print(f'😩😩 sorry you lost!! it was "{original_word}", better luck next time !!!')