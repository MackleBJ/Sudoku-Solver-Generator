# Author: Brett M.
# Date: 12/11/2021
# Sudoku Solver/Generator (Non-brute force)
import random

'''I wanted to create a sudoku solver that didn't use brute
force (recursion). I wanted the program to show step by step the numbers added
to the puzzle. Thereby, allowing the user to follow the steps the program took
to solve the puzzle. Due to the complexity level that sudoku puzzles can achieve,
this sudoku solver is aimed at beginner level puzzles that don't use advanced
solving methods and strategies to solve.'''

# Function to hold puzzle locations.
def puzzle_locations():
    print("Puzzle locations: ")
    print("------------------------------------")
    print("| |0 |1 |2 | |3 |4 |5 | |6 |7 |8 | |")
    print("| |9 |10|11| |12|13|14| |15|16|17| |")
    print("| |18|19|20| |21|22|23| |24|25|26| |")
    print("------------------------------------")
    print("| |27|28|29| |30|31|32| |33|34|35| |")
    print("| |36|37|38| |39|40|41| |42|43|44| |")
    print("| |45|46|47| |48|49|50| |51|52|53| |")
    print("------------------------------------")
    print("| |54|55|56| |57|58|59| |60|61|62| |")
    print("| |63|64|65| |66|67|68| |69|70|71| |")
    print("| |72|73|74| |75|76|77| |78|79|80| |")
    print("------------------------------------\n")

# Function to get the starting numbers of the sudoku board from the user.
def get_starting_numbers():
    master = []
    puzzle_locations()

    for position in range(0,81):
        while True:
            try:
                number = int(input("Please enter the number (0 = blank) for {}: ".format(position)))
                break
            except:
                print("You will need to enter a number from 0-9. 0 for a blank space.")
        while True:
            if number >= 0 and number <= 9:
                master.append(number)
                break
            else:
                try:
                    number = int(input("Please enter a number between 0-9. 0 for a blank space."))
                except:
                    print("You will need to enter a number from 0-9. 0 for a blank space.")

    return master

# Function to determine if number is in the current row.
def is_number_in_row(master, position, number):
    row1 = [0,1,2,3,4,5,6,7,8]
    row2 = [9,10,11,12,13,14,15,16,17]
    row3 = [18,19,20,21,22,23,24,25,26]
    row4 = [27,28,29,30,31,32,33,34,35]
    row5 = [36,37,38,39,40,41,42,43,44]
    row6 = [45,46,47,48,49,50,51,52,53]
    row7 = [54,55,56,57,58,59,60,61,62]
    row8 = [63,64,65,66,67,68,69,70,71]
    row9 = [72,73,74,75,76,77,78,79,80]
    rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    for row in rows:
        if position in row:
            for integer in row:
                if number == master[integer]:
                    in_row = True
                    break
                else:
                    in_row = False

    return in_row

# Function to determine if number is in the current column.
def is_number_in_column(master, position, number):
    column1 = [0,9,18,27,36,45,54,63,72]
    column2 = [1,10,19,28,37,46,55,64,73]
    column3 = [2,11,20,29,38,47,56,65,74]
    column4 = [3,12,21,30,39,48,57,66,75]
    column5 = [4,13,22,31,40,49,58,67,76]
    column6 = [5,14,23,32,41,50,59,68,77]
    column7 = [6,15,24,33,42,51,60,69,78]
    column8 = [7,16,25,34,43,52,61,70,79]
    column9 = [8,17,26,35,44,53,62,71,80]
    columns = [column1, column2, column3, column4, column5, column6, column7, column8, column9]

    for column in columns:
        if position in column:
            for integer in column:
                if number == master[integer]:
                    in_column = True
                    break
                else:
                    in_column = False

    return in_column

# Function to determine if number is in the current 3x3 section.
def is_number_in_box(master, position, number):

    box1 = [0,1,2,9,10,11,18,19,20]
    box2 = [3,4,5,12,13,14,21,22,23]
    box3 = [6,7,8,15,16,17,24,25,26]
    box4 = [27,28,29,36,37,38,45,46,47]
    box5 = [30,31,32,39,40,41,48,49,50]
    box6 = [33,34,35,42,43,44,51,52,53]
    box7 = [54,55,56,63,64,65,72,73,74]
    box8 = [57,58,59,66,67,68,75,76,77]
    box9 = [60,61,62,69,70,71,78,79,80]
    boxes = [box1, box2, box3, box4, box5, box6, box7, box8,box9]

    for box in boxes:
        if position in box:
            for integer in box:
                if number == master[integer]:
                    in_box = True
                    break
                else:
                    in_box = False

    return in_box

# Function to add numbers to master for locations with only 1 possible number.
def fill_out_sudoku_puzzle(master, show_moves):
    possible_location = []
    counter = 0
    was_number_added = False

    for position in master:
        if position == 0:
            for number in range(1,10):
                if is_number_in_row(master, counter, number) == False and is_number_in_column(master, counter, number) == False and is_number_in_box(master, counter, number) == False:
                    possible_location.append(number)

        if len(possible_location) == 1:
            master[counter] = possible_location[0]
            if show_moves == True:
                print('Added the number {} to location {}'.format((possible_location[0]), counter))
            was_number_added = True
        possible_location = []
        counter += 1

    return master, was_number_added

# Function to print 9x9 grid when puzzle is solved/program isn't making progress.
def print_puzzle(master):
    print("---------------------------")
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[0],master[1],master[2],master[3],master[4],master[5],master[6],master[7],master[8]))
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[9],master[10],master[11],master[12],master[13],master[14],master[15],master[16],master[17]))
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[18],master[19],master[20],master[21],master[22],master[23],master[24],master[25],master[26]))
    print("---------------------------")
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[27],master[28],master[29],master[30],master[31],master[32],master[33],master[34],master[35]))
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[36],master[37],master[38],master[39],master[40],master[41],master[42],master[43],master[44]))
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[45],master[46],master[47],master[48],master[49],master[50],master[51],master[52],master[53]))
    print("---------------------------")
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[54],master[55],master[56],master[57],master[58],master[59],master[60],master[61],master[62]))
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[63],master[64],master[65],master[66],master[67],master[68],master[69],master[70],master[71]))
    print("| |{}|{}|{}| |{}|{}|{}| |{}|{}|{}| |".format(master[72],master[73],master[74],master[75],master[76],master[77],master[78],master[79],master[80]))
    print("---------------------------")

# Function to solve/attempt to solve a sudoku puzzle.
def solve_sudoku():
    #master = [0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 9, 0, 0, 4, 6, 0, 7, 0, 0, 7, 2, 3, 0, 8, 0, 0, 0, 9, 0, 7, 2, 6, 1, 0, 8, 3, 8, 0, 6, 0, 0, 0, 2, 0, 0, 4, 0, 1, 9, 0, 3, 6, 5, 7, 0, 6, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 9, 0, 5, 0, 0, 9, 0, 0, 0, 0, 3, 4]
    master = get_starting_numbers()
    while (0 in master):
        master, was_number_added = fill_out_sudoku_puzzle(master, True)
        if was_number_added == False:
            print('\nSorry, it looks like this puzzle is too advanced for this sudoku solver.')
            print('This is how far we were able to solve the puzzle:\n')
            break
    print_puzzle(master)

# Function to solve puzzles that don't require user to input puzzle data. Also, will test to verify if the puzzle can be completed using this program.
def solve_generated_sudoku(master, verifying_puzzle):
    while (0 in master):

        # If we are simplying checking to verify that a puzzle is solvable using the program, we don't want steps to be shown.
        if verifying_puzzle == True:
            master, was_number_added = fill_out_sudoku_puzzle(master, False)
        else:
            master, was_number_added = fill_out_sudoku_puzzle(master, True)

        if was_number_added == False:
            completed = False
            break
        else:
            completed = True

    if verifying_puzzle == True:
        return completed

# Function to randomly generate a sudoku puzzle.
def generate_sudoku():
    master = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    additions = 0
    while additions < 30:
        number = random.randint(1,9)
        position = random.randint(0,80)
        if master[position] == 0:
            if is_number_in_row(master, position, number) == False and is_number_in_column(master, position, number) == False and is_number_in_box(master, position, number) == False:
                master[position] = number
                additions += 1

    return master

print('*** Welcome to the Sudoku Solver/Generator ***')
while True:
    print('\nMain Menu:')
    print('1. Solve a puzzle.')
    print('2. Generate a puzzle.')
    print('3. Exit program.')
    answer = input('\nWhat would you like to do? ')

    # Solve a puzzle that requires user to input puzzle data.
    if answer == '1':
        solve_sudoku()

    # Generate a puzzle for the user and validate that program can solve it.
    elif answer == '2':
        print('\n*** This may take a little bit of time. ***')
        while True:
            master_original = generate_sudoku()
            master = master_original.copy()
            complete = solve_generated_sudoku(master, True)
            if complete == True:
                print('\nGenerated Puzzle:')
                print_puzzle(master_original)
                break

        while True:
            response = input('\nWould you like to use the program to solve this puzzle? (y/n) ')
            print('')

            # User would like program to solve the generated puzzle.
            if response == 'y' or response == 'yes':
                puzzle_locations()
                solve_generated_sudoku(master_original, False)
                print('\nCompleted Puzzle:')
                print_puzzle(master_original)
                break
            # User doesn't want to the program to solve the generate puzzle.
            elif response == 'n' or response == 'no':
                break
            # Invalid entries.
            else:
                print('Invalid response. Please enter yes(y) or no(n).')

    # Exit the program.
    elif answer == '3':
        print('\nThank you for using the Sudoku Solver/Generator')
        exit()

    # Invalid entries.
    else:
        print('\nInvalid entry. Please enter the number 1 or 2.')

