import numpy as np
from blessed import Terminal
from math import floor

term = Terminal()

universe = np.zeros((term.height,term.width))

beacon = [[1,1,0,0],
          [1,1,0,0],
          [0,0,1,1],
          [0,0,1,1]]

r_pentomino = [[0,1,1],
               [1,1,0],
               [0,1,0]]


def set_initial_universe(chosen_seed):
    """
    Place the seed cells within the initial universe. 

    :param chosen_seed: the user's seed choice

    """
    
    seed_start_y = floor(term.height/2) - floor(len(chosen_seed)/2)
    seed_start_x = floor(term.width/2) - floor(len(chosen_seed[0])/2)
    universe[seed_start_y:seed_start_y+len(chosen_seed), seed_start_x:seed_start_x+len(chosen_seed[0])] = chosen_seed


def survival(x, y, universe):
    """
    Determine survival or death of each cell. 


    """
    num_neighbors = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    if universe[x, y] and not 2 <= num_neighbors <=3:
        return 0
    elif num_neighbors == 3:
        return 1
    return universe[x, y]


def generation(some_universe):
    """
    Compute one generation. 

    :param universe: current universe of cells
    :type universe: n-dimensional array
    :return: updated universe of cells
    :rtype: n-dimensional array
    """
    new_universe = np.copy(some_universe)
    for i in range(some_universe.shape[0]):
        for j in range(some_universe.shape[1]):
            new_universe[i,j] = survival(i, j, some_universe)
    return new_universe


def refresh_screen():
    """
    Display a new generation.


    """
    with term.cbreak(), term.hidden_cursor():
        print(term.fullscreen, term.black_on_olive + term.clear)
        for row in universe:
            for cell in row:
                if cell == int(0):
                    print(term.white_on_darkgreen('0'), end='')
                else:
                    print(term.white_on_darkgreen('1'), end='')
        print('\n')


def options_sequence():
    """
    A sequence of input screens that allows the user to customize the Game of Life. 


    """
    print(term.fullscreen, term.clear + term.move_y(term.height //2))
    print(term.white_on_darkgreen(term.center('Conway\'s Game of Life.')))
    print(term.black_on_darkgreen(term.center('Choose your starting seed.')))
    print(term.black_on_darkgreen(term.center('1    Beacon')))
    print(term.black_on_darkgreen(term.center('2    R-Pentomino')))
    with term.hidden_cursor(), term.cbreak():
        input = ''
        while input == '':
            input = term.inkey()
            if input == '1':
                set_initial_universe(beacon)
            elif input == '2':
                set_initial_universe(r_pentomino)
            else:
                break

        


def main():
    global universe

    print(term.fullscreen, term.clear + term.move_y(term.height //2))
    print(term.white_on_darkgreen(term.center('Conway\'s Game of Life.')))
    print(term.black_on_darkgreen(term.center('Press any key to continue.')))
    print(term.black_on_darkgreen(term.center('Ctrl + C to quit.')))

    with term.hidden_cursor(), term.cbreak():
        input = ''
        while input == '':
            input = term.inkey()
        options_sequence()

    with term.hidden_cursor(), term.cbreak():
        input = ''
        while input.lower != 'q':
            input = term.inkey(timeout=3)
            if input == 'a':
                universe = generation(universe)
                refresh_screen()

main()