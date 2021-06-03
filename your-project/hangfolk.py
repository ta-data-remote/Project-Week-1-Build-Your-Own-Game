



def generate_word_display(hidden_word, used_letters):
    result = str()
    for character in hidden_word:
        if character in used_letters:
            result = result + character
        else:
            result = result + "*"
    return result

def print_current_game(used_letters,encrypted_word):
    print("Those are the letters you have used:", used_letters)
    print("This is the word:", encrypted_word)

def player_input_letter():
    input_letter = input("Please,enter a letter: ")
    return input_letter

def player_win(word,used_letters):
    for character in word:
        if character not in used_letters:
            return False
    return True

def player_loose(lives):
    if lives == 0:
        return True
    else:
        False


def print_result(player_won, word):
    if player_won:
        print(f"Cool! You have won! The word was: {word}")
    else:
        print("Sorry, you have used all your lives. You are hanged!")

ongoing = True
used_letters = []
lives = 11
player_won= False
word = "terrible"
while ongoing:
    word_display = generate_word_display(word,used_letters)
    print_current_game(used_letters, word_display)
    player_letter = player_input_letter()
    used_letters.append(player_letter)
    if player_letter in word:
        if player_win(word, used_letters): #a letter from the word is not in the list of letters
            ongoing = False
            player_won = True
    else:
        lives -= 1
        if player_loose(lives):
            ongoing = False
print_result(player_won,word)
