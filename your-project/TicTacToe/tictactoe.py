import time
import sys

def graph(state_dict):

#
# Checks the keys 1, 2, 3, 4, 5, 6, 7, 8 and 9 (that correspond to positions of the game) and prints their values
# together with the board graphics. The values of the dictionary should be O or X.
#
# 
# INPUT:  state_dict (dict): Dictionary with the symbols (X for player, O for computer or " " if not played yet) 
#                            placed in each position.
# 
# OUTPUT: None
#
    
    print("\n")
    print(" "+state_dict["1"]+" | "+state_dict["2"]+" | "+state_dict["3"]+" ")
    print("---·---·---")
    print(" "+state_dict["4"]+" | "+state_dict["5"]+" | "+state_dict["6"]+" ")
    print("---·---·---")
    print(" "+state_dict["7"]+" | "+state_dict["8"]+" | "+state_dict["9"]+" ")

    return


def find_best_move(free_pos,my_wincons,player_wincons,my_wincons_dict,player_wincons_dict):

#
# Finds the best move for the computer. It's a badass function
#
#
# INPUT:  free_pos (list): list that includes all the available positions in the board as strings (e.g. ["1","3"]
#                          if only positions 1 and 3 are free)
#
#         my_wincons (list): list that includes all the possible 3-in-a-row combinations for the computer given
#                            the current state of the game (e.g ["123","159","369"])
#
#         my_wincons_dict (dict): a dictionary that, for every possible 3-in-a-row combination (key), gives the
#                                 number of positions already occupied by the computer (value). If the player is
#                                 occupying one of those positions, the value is automatically switched to "-1"
#
#         player_wincons (list): list that includes all the possible 3-in-a-row combinations for the player
#                                given the current state of the game (e.g ["123","159","369"])
#
#         player_wincons_dict (dict): a dictionary that, for every possible 3-in-a-row combination (key), gives
#                                     the number of positions already occupied by the player (value). If the
#                                     computer is occupying one of those positions, the value is automatically
#                                     switched to "-1"
#
# OUTPUT: best_move (str): the best possible move in the world I promise
#
    my_best_moves = []
    player_best_moves = []
    player_fork = []
    max_counter = 0
    maxp_counter = 0
    
    
    if "5" in free_pos: #Always center first
        return "5"
    
    if len(free_pos)==7: #Opposite corner
        corner_sum = 0
        for pos in free_pos:
            corner_sum += int(pos)
        if corner_sum%2 != 0:
            return str(-30+corner_sum)
    
    for pos in free_pos:
        my_counter = 0
        player_counter = 0
        my_fork_counter = 0
        player_fork_counter = 0
            
        for wincon in my_wincons:
            if pos in wincon:
                my_counter += 1
                if my_wincons_dict[wincon] == 1:
                    my_fork_counter += 1
                    if my_fork_counter == 2:
                        return pos
            
        if my_counter >= max_counter:
            
            if my_counter > max_counter:
                my_best_moves = []
                max_counter = my_counter
            my_best_moves.append(pos)
            
        for wincon2 in player_wincons:
            if pos in wincon2:
                player_counter += 1
                if player_wincons_dict[wincon2] == 1:
                    player_fork_counter += 1
                    if player_fork_counter == 2:
                        player_fork.append(pos)       
                    
        if player_counter >= maxp_counter:
            
            if player_counter > maxp_counter:
                player_best_moves = []
                maxp_counter = player_counter
            player_best_moves.append(pos)
            
    if len(player_fork) != 0:
        print(my_best_moves)
        for fork in player_fork:
            if fork in my_best_moves:
                return fork
        return player_fork[0]
    
    for best in my_best_moves:
        if best in player_best_moves:
            return best

                
    return my_best_moves[0]


def tictactoe():

#  ***************************************
#
#                 THE GAME
#
#  ***************************************

#
#  ****************  Printing instructions  ***************
#
    
    print("\n")
    print("\n")
    print("INSTRUCTIONS: \n")
    print("Each position of the board has an assigned number from 1 to 9. In each of your turns, choose a free position in the board an introduce the corresponding number to play in that position. You can see the correspondence in the following diagram: \n")
    state_dict_help = {"1":"1","2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9"}
    graph(state_dict_help)
    
    time.sleep(1)
    
    play_again = True
    
    while play_again:
        
#
#  ****************  Restarting variables  ***************
#
        first_error = True
        again_error = True
        move_error = True
        state_dict = {"1":" ","2":" ", "3":" ", "4":" ", "5":" ", "6":" ", "7":" ", "8":" ", "9":" "}
        
        free_pos = ["1","2","3","4","5","6","7","8","9"]
        win = False
        
        my_wincons = ["123","456","789","159","357","147","258","369"]
        my_wincons_dict = {"123":0,"456":0,"789":0,"159":0,"357":0,"147":0,"258":0,"369":0}
        
        player_wincons = ["123","456","789","159","357","147","258","369"]
        player_wincons_dict = {"123":0,"456":0,"789":0,"159":0,"357":0,"147":0,"258":0,"369":0}
#
#  ****************  Who goes first  ***************
#
        while first_error:    #Playing first or second input
            
            print("\n")
            first_yn = input("Do you want to go first? (Y/N): ",)
            print("\n")
            
            if "y" in first_yn.lower():
                
                player_turn = True
                print("You chose playing first")
                
                first_error = False
                print("\n")
                print("The game starts!")
                graph(state_dict)
                
                time.sleep(1)
                
            elif "n" in first_yn.lower():
                
                player_turn = False
                print("You chose playing second")
                
                first_error = False
                print("\n")
                print("The game starts!")
                
                time.sleep(1)
                
            else:
                print("Input was invalid. Please, answer with 'Y' (Yes) or 'N' (No)")   
                
#
#  ****************  Game starts  ***************
#
        while win == False:

#
#  ****************  Player Turn  ***************
#
            
            if player_turn == True:
            
                
                while player_turn:  #Player move input 
            
                    print("\n")
                    player_move = input("Your turn! Choose a position where you want to play: ")
                    print("\n")
            
                    if player_move in free_pos:
                    
                        player_turn = False
    
                    elif player_move == "00":
                        sys.exit()
                        
                    else:
                        
                        print("Input was invalid. Please, choose one of the available positions. Available positions are: \n",free_pos)  
                
                state_dict[player_move] = "X"
                free_pos.remove(player_move)
                
                print("You played in position",player_move,"! Take a look at it and regret your life choices")
                graph(state_dict)
                
                time.sleep(2)
                
                for wincon in player_wincons: #update player wincons

                    if player_move in wincon:

                        player_wincons_dict[wincon] += 1

                        if player_wincons_dict[wincon] == 3:
    
                            win = True
                            break
            
                my_wincons_temp = list(my_wincons)
                for wincon2 in my_wincons_temp: #update computer wincons

                    if player_move in wincon2:

                        my_wincons_dict[wincon2] = -1
                        my_wincons.remove(wincon2)
                
                if win:
                    
                    print("\n")
                    print("Amazing! You beat the computer!")
                
                

#
#  ****************  Computer Turn  ***************
#         
            else:              
                
                no_move = True
                for wincon in my_wincons: #if the computer can win in one move
                    
                    if my_wincons_dict[wincon]==2:
                        for pos in free_pos:
                            if pos in wincon:
                                no_move = False
                                my_move = pos
                                break
                        break
                        
                if no_move: #if the computer can lose in one move
                    
                    for wincon in player_wincons:
                    
                        if player_wincons_dict[wincon]==2:
                            for pos in free_pos:
                                if pos in wincon:
                                    no_move = False
                                    my_move = pos
                                    break
                            break
                 
                if no_move:  #A.I. motherfucker
                    
                    my_move = find_best_move(free_pos,my_wincons,player_wincons,my_wincons_dict,player_wincons_dict)
            
                state_dict[my_move] = "O"
                free_pos.remove(my_move)
                
                print("\n")
                print("The computer played in the position",my_move,"!")
                graph(state_dict)
                
                player_turn = True   
                
                for wincon in my_wincons:
                    
                    if my_move in wincon:

                        my_wincons_dict[wincon] += 1

                        if my_wincons_dict[wincon] == 3:
    
                            win = True
                            break
                player_wincons_temp = list(player_wincons)
                for wincon2 in player_wincons_temp:
                    if my_move in wincon2:
                        player_wincons_dict[wincon2] = -1
                        player_wincons.remove(wincon2)
                
                if win:
                    
                    print("\n")
                    print("The computer beat you! At least you can say you tried ;)")
                    time.sleep(2)
                    
            if len(player_wincons) == 0 and len(my_wincons) == 0:

                print("\n")
                print("No one can win, it's a tie! What a boring game :S")
                time.sleep(2)
                win = True

#
#  ****************  Another game?  ***************
#     
        while again_error:  #Asking to play again 
            
            print("\n")        
            again_yn = input("Do you want to go play again? (Y/N): ")
            print("\n")
            
            if "y" in again_yn.lower():
                
                print("Let's play again!")
                again_error = False
              
                
            elif "n" in again_yn.lower():
                
                play_again = False
                again_error = False
               
            else:
                print("Input was invalid. Please, answer with 'Y' (Yes) or 'N' (No)")
                
#
#  ****************  End of the game  ***************
# 
    print("Thanks for playing! :)")
    print("\n")
    
    return 
