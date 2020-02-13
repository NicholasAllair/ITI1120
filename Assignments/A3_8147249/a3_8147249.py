import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''

    deck = random.sample(deck, len(deck))
    
    return deck 

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')

def print_board_stars(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way with no numbers shown
    '''
    for i in range(len(a)):
        print('{0:4}'.format("*"), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''

    
    star_board = []
    
    for i in range(len(original_board)):
        star_board = star_board + ['*']

    star_board[p1] = original_board[p1]

    star_board[p2] = original_board[p2]

    

    for i in range(len(original_board)):
        if discovered.count(i) != 0:
            star_board[i] = original_board[i]
    
    print_board(star_board)
         

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
     Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    
    return (raw_board)


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")

    playable_board = []

    for i in range(l.count('*')):
        l.remove('*')

    for i in range(len(l)):
        
        char = l[i]

        if ((playable_board.count(char) % 2) != 0) or ((playable_board.count(char) == 0) and ((l.count(char) % 2) == 0)): 
            playable_board.append(char)

        if (l.count(char) % 2 != 0) and (l.count(char) >= 3) and (playable_board.count(char) == 0):
            playable_board = playable_board + [char] * (l.count(char)-1)
    
    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''


    for i in range(len(l)):
        char = l[i]

        if l.count(char) > 2:
            return False
            print("*********************************************************************************")
            print("*                                                                               *")
            print("*    Thsis deck is now playable but not rigorous and it has ",len(l), "cards    *")
            print("*                                                                               *")
            print("*********************************************************************************")
        
    return True
    print("*****************************************************************************")
    print("*                                                                           *")
    print("*    Thsis deck is now playable and rigorous and it has ",len(l), "cards    *")
    print("*                                                                           *")
    print("*****************************************************************************")



    
    # YOUR CODE GOES HERE
 
                
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    

    num_pairs = int(len(board))/2
    pairs_found = 0
    discovered = []
    guesses = 0
    how_many_more = guesses - num_pairs
    

    while pairs_found != num_pairs:

        star_board = []
    
        for i in range(len(board)):
            star_board = star_board + ['*']

        for i in range(len(board)):
            if discovered.count(i) != 0:
                star_board[i] = board[i]

        print_board(star_board)

        print("\n\n")

        
        print ("Enter two distinct positions on the board that you want revealed.")
        print ("i.e. two integers in the range [1, ",len(board),"]")

        p1 = int(input("Enter position 1: "))
        p2 = int(input("Enter position 2: "))
        p1 = p1-1
        p2 = p2-1
       
        while (p1 == p2) or (discovered.count(p1) != 0) or (discovered.count(p2) != 0) or (p1 < 0) or (p1 > (len(board) -1)) or (p2 < 0) or (p2 > (len(board) -1)) :

            print ("One or both of your chosen pairs has already been paired.")
            if p1 == p2:
                print("You chose the same positions")
            if (p1 < 0) or (p1 > (len(board) -1)) or (p2 < 0) or (p2 > (len(board) -1)):
                print("Your entry is not within range, please try again.")
            print("Please try again. This guess did not count. Your current number of guesses is " ,guesses,".")
            print ("\n")

            print ("Enter two distinct positions on the board that you want revealed.")
            print ("i.e. two integers in the range [1, ",len(board),"]")

            p1 = int(input("Enter position 1: "))
            p2 = int(input("Enter position 2: "))

            p1 = p1-1
            p2 = p2-1

        print_revealed(discovered, p1, p2, board)

        if board[p1] == board[p2]:

            print ("match")
            pairs_found += 1

            discovered = discovered + [p1] + [p2]
        

        wait_for_player()

        print('\n'*40)

        guesses += 1

    how_many_more = int(guesses - num_pairs)
    
    print("\nCongratulations! You completed the game with ",guesses, " guesses.  That is ",how_many_more, " than the best possible")

    
    

    

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE




#main

print("******************************************")
print("*                                        *")
print("*    Welcome to my Concentration game    *")
print("*                                        *")
print("******************************************")
    
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE

print("Would you like (enter 1 or 2 to indicate your choice)")
print("(1) me to generate a rigorous deck of cards for")
print("(2) or, would you like me to read a deack from a file?")

choice  = int(input(""))

while  (choice < 1) or (choice >2):
    print(choice, " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice")
    choice = int(input(""))

# YOUR CODE FOR OPTION 1 GOES HERE

if choice == 1:
    print("\nYou have chosen a rigorous deck generated for you\n")
    print("How many cards do you want to play with?")
    size = int(input("Enter and even number between 0 and 52: "))

    sizemod2 = size % 2

    while (size < 0) or (size > 58) or (sizemod2 != 0):
        print("How many cards do you want to play with?")
        size = int(input("Enter and even number between 0 and 52: "))
        sizemod2 = size % 2

    print("Shuffling the deck...")

    board = create_board(size)
    board = shuffle_deck(board)

    input("Press enter to continue")
    print("\n" * 40)

    play_game(board)
                      
    
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)

# YOUR CODE FOR OPTION 2 GOES HERE

if choice == 2:
    print("You chose to laod a deck of cards from a file")
    file = input("Enter the name of the file: ")
    
    raw_board = read_raw_board(file)
    
    playable_board = clean_up_board(raw_board)

    is_rigorous(playable_board)

    print("\n\n\n")

    wait_for_player()

    print("\n" * 40)

    print("Shuffling the deck...")
    shuffle_deck(playable_board)

    wait_for_player()

    play_game(playable_board)
    


# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
#
#print("You chose to load a deck of cards from a file")
#file=input("Enter the name of the file: ")
#file=file.strip()
#board=read_raw_board(file)
#board=clean_up_board(board)

