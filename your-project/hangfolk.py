#######Welcome#########

import random


def welcome():
    '''
    This function welcomes the player asking for her/his name and explain the basic rules.
    It has no return, it just prints
    '''

    player_name =  input("Please, enter your name: ")
    print("Hello,",player_name)
    print("You probably know the game... In can you don't, I will quickly explain how it works...")
    print("You will have to guess the choosen word, picking in each turn a letter from the alphabet.If you fail, you will loose one of the 11 lives you have")
    print("If you fail too much, you will be hanged")



###############Chossing a topic############
def choose_a_topic():
    '''
    This function is for choosing a topic from the provided ones.
    The player inputs the topic. The functions makes sures the topic is one of the given ones.
    It returns the topic chosen by the player
    '''

    print("Now I will display a list of topics and you will have to pick one:")
    list_topics = ["sports", "medicine", "nature"]

    for topics in list_topics:
        print(topics)

    player_topic = input("Please, enter the topic you have choosen:")

    check_topic = True

    while check_topic:
        if player_topic in list_topics:
            print("Great! You have choosen: ", player_topic)
            check_topic = False
        else:
            player_topic = input("Please, enter the topic you have choosen correctly/from the list before:")

    return player_topic



###################Providing a word###############

def clean_list(list1, drop="\n"):
    '''
    This function cleans a list from escape sequences and transforms the elements/strings
    in lower case.
    The input is a list and drop can be modified with more special characters.
    A new clean list is returned.
    '''

    clean_list = []
    for element in list1:
        element = element.lower()
        element = element.replace(drop, "")
        clean_list.append(element)
    return clean_list



def choose_word(list1):
    '''
    This function selects randomly an element.
    The input must be a list and the output is the selected element
    '''
    chosen_word = random.choice(list1)
    return chosen_word


#######Player inputs letters####################

def player_input_letter(letters) :
    '''
    This function ask the player for the letter to play. It also
    makes sures that is not a repeated letter and is not a digit. It will ask untill
    it get the right input.
    The input must be a list and the output is the output a single character.
    In this case the list of used letters.
    '''

    while True:
        input_letter = input("Please,enter a letter: ")
        if input_letter not in letters and input_letter.isdigit() == False:
            break
        elif input_letter in letters:
            print("Please,enter another letter. This one you have already used")
        elif input_letter.isdigit():
            print("Please, enter a letter, not a digit")

    return input_letter

######Displa

def generate_word_display(hidden_word, list_letters):
    '''
    This function generates a display of the encrypted word. It creates
    an empty string where the letters present on the list are concatenated with *,
    for the letters that are not present in the list but in the word.
    In this way, we just show the played letters.
    the inputs are a string (the word) and a list (the used_letters)
    '''
    result = str()
    for character in hidden_word:
        if character in list_letters:
            result = result + character
        else:
            result = result + "*"
    return result

def print_current_game(list_letters,hidden_word):
    '''
    This function prints the list of used letters and the encrypted word.
    It will be print every turn, so it will show the advances on the game.
    The inputs are a list of letter(the used letters) and a string (encrypted word)
    '''
    print("Those are the letters you have used:", list_letters)
    print("This is the word:", hidden_word)



def main():
    '''
    This function is the one who is gonna make run the game as many times as the player wants
    '''
    print("Welcome to the hangfolk game version lau.0")
    while True:
        welcome()

        player_topic = choose_a_topic()

        sports_file = open("/Users/lauratll/Documents/Data_Analysis/IronHack/Week_1/Project_week1/Project-Week-1-Build-Your-Own-Game/your-project/sports_list.txt")
        medicine_file = open("/Users/lauratll/Documents/Data_Analysis/IronHack/Week_1/Project_week1/Project-Week-1-Build-Your-Own-Game/your-project/medicine_list.txt")
        nature_file = open("/Users/lauratll/Documents/Data_Analysis/IronHack/Week_1/Project_week1/Project-Week-1-Build-Your-Own-Game/your-project/nature_list.txt")
        sports_list = clean_list(sports_file)
        medicine_list = clean_list(medicine_file)
        nature_list = clean_list(nature_file)

        dic_words = {}
        dic_words["sports"] = sports_list
        dic_words["medicine"] = medicine_list
        dic_words["nature"] = nature_list
        word = choose_word(dic_words[player_topic])

        ongoing = True
        used_letters = []
        lives = 11
        player_wins = False

        while ongoing:
            player_letter = player_input_letter(used_letters)
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
            print(f"Sorry! You are hanged! The word was: {word}")

        play_again = input("Would you like to play again?(Yes/No)")
        if play_again == "No":
            break
main()