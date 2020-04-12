from IPython.display import clear_output

def display_board(board):

    clear_output()
    print(board[7]+ ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4]+ ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1]+ ' | ' + board[2] + ' | ' + board[3])


'''
All Python classes will reside in this file
'''
# Establish board for game here. This may be subject to change
class Board:

    def __init__(self):
        pass

    def __str__(self):
        pass

# Establish Stones
class Stones:

    def __init__(self, board):
        pass

'''
Establish rule for liberties - adjacent spaces near a stone being open
'''

def liberties_check(board, player):
    pass


'''
Establish rule against self capture
'''
def no_self_capture(board, player): 
    pass


'''
Establish string check - a line of stones of the same color that occupy the adjacent liberties
'''

def string_check(board):
    pass

'''
Establish a group check - several strings of the same color close together
'''

def group_check(board):
    pass

'''
Establish a hopeless string check - any string that is surrounded by an enemy group and it is obvious it would be captured.
Hopeless strings can be left alone until the end of the game.
'''

def hopeless_string_check(board):
    pass


'''
Establish an eye check - a group with two vacant spaces inside the area. Any group with eyes is permanently safe from capture.
'''

def eye_check(board):
    pass

'''
Optional Coo rule - an area on the board where a continuous back and forth can occur. 
The rule prevents this back and forth until a move somewhere else is made
'''

def coo_rule(board):
    pass

