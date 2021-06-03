
def player_input_letter(letters) : #list of letters
    while True:
        input_letter = input("Please,enter a letter: ")
        if input_letter not in letters and input_letter.isdigit() == False:
            print("Hola")
            break
        elif input_letter in letters:
            print("Please,.....")
        elif input_letter.isdigit():
            print("Please....")

    return input_letter



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



def main():
    ongoing = True
    used_letters = []
    lives = 11
    word = "terrible"
    player_wins = False

    while ongoing:
        player_letter = player_input_letter()
        used_letters.append(player_letter)
        word_display = generate_word_display(word, used_letters)
        if player_letter not in word:
            lives -= 1
            if lives == 0:
                ongoing = False

        if "*" not in word_display:
            ongoing= False
            player_wins= True

        print_current_game(used_letters, word_display)

    if player_wins:
        print(f"Cool! You have won! The word was: {word}")
    else:
        print("Sorry, you have used all your lives. You are hanged!")
