import numpy
from blessed import Terminal
from math import floor
from time import sleep

term = Terminal()

universe = numpy.zeros((term.height - 1, term.width))  # -1 accounts for header

speed = 0.5

num_generations = 2000

"""Starting Seed Options"""
beacon = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]

r_pentomino = [[0, 1, 1], [1, 1, 0], [0, 1, 0]]

diehard = [[0, 0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 1]]

acorn = [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]]

block_switch = [
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
]


def main():
    """
    Main flow for the app.
    """

    global universe

    universe = numpy.zeros(
        (term.height - 1, term.width)
    )  # '-1' accounts for the header

    intro_screen()
    seed_choice()
    rate_choice()

    with term.hidden_cursor(), term.cbreak():
        refresh_screen()
        inp = ""

        while inp.lower() != "q":
            inp = term.inkey()
            if inp == " ":
                universe = generation(universe)
                refresh_screen()
            elif inp.lower() == "m":
                main()
            elif inp.lower() == "q":
                term.clear()
                exit()

            # If window resizes, restart.
            if term.width != len(universe[0]):
                main()

            inp = ""
            sleep(speed)


def set_initial_universe(chosen_seed):
    """
    Place the seed cells within the initial universe.

    :param chosen_seed: the user's seed choice
    """
    seed_start_y = floor(term.height / 2) - floor(len(chosen_seed) / 2)
    seed_start_x = floor(term.width / 2) - floor(len(chosen_seed[0]) / 2)
    universe[
        seed_start_y : seed_start_y + len(chosen_seed),
        seed_start_x : seed_start_x + len(chosen_seed[0]),
    ] = chosen_seed


def survival(x, y, universe):
    """
    Determine survival or death of each cell.

    :param x: current x-coordinate
    :param y: current y-coordinate
    :param universe: current universe
    :return: 0 for death, 1 for life
    :rtype: int
    """
    num_neighbors = numpy.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    if universe[x, y] and not 2 <= num_neighbors <= 3:
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
    new_universe = numpy.copy(some_universe)
    for i in range(some_universe.shape[0]):
        for j in range(some_universe.shape[1]):
            new_universe[i, j] = survival(i, j, some_universe)
    return new_universe


def refresh_screen():
    """
    Display a new generation based on the current state of the universe.
    """

    with term.cbreak(), term.hidden_cursor():
        print(
            term.bold_white_on_darkgreen(
                term.center("Generate Life: Hold Spacebar    Main Menu: M    Quit: Q")
            )
        )
        for row in universe:
            for cell in row:
                if cell == int(0):
                    print(term.darkgreen_on_white(" "), end="")
                else:
                    print(term.bold_darkgreen_on_white("\u2593"), end="")


def seed_choice():
    """
    Prompts user to choose initial seed.
    """

    print(term.clear + term.move_y(term.height // 2 - 5))
    print(term.bold_white_on_darkgreen(term.center("")))
    print(term.bold_white_on_darkgreen(term.center("Conway's Game of Life")))
    print(term.white_on_darkgreen(term.center("Choose your starting seed.")))
    print(term.white_on_darkgreen(term.center("1    Beacon             ")))
    print(term.white_on_darkgreen(term.center("2    R-Pentomino        ")))
    print(term.white_on_darkgreen(term.center("3    Diehard            ")))
    print(term.white_on_darkgreen(term.center("4    Acorn              ")))
    print(term.white_on_darkgreen(term.center("5    Block Switch Engine")))
    print(term.bold_white_on_darkgreen(term.center("")))

    with term.hidden_cursor(), term.cbreak():
        inp = ""
        while inp == "":
            inp = term.inkey()
            if inp == "1":
                set_initial_universe(beacon)
            elif inp == "2":
                set_initial_universe(r_pentomino)
            elif inp == "3":
                set_initial_universe(diehard)
            elif inp == "4":
                set_initial_universe(acorn)
            elif inp == "5":
                set_initial_universe(block_switch)
            else:
                seed_choice()


def rate_choice():
    """
    Prompts user to choose speed/rate.
    """

    print(term.clear + term.move_y(term.height // 2 - 5))
    print(term.bold_white_on_darkgreen(term.center("")))
    print(term.bold_white_on_darkgreen(term.center("Conway's Game of Life")))
    print(term.white_on_darkgreen(term.center("Choose your speed.")))
    print(term.white_on_darkgreen(term.center("1    Slow   ")))
    print(term.white_on_darkgreen(term.center("2    Medium ")))
    print(term.white_on_darkgreen(term.center("3    Fast   ")))
    print(term.bold_white_on_darkgreen(term.center("")))

    with term.hidden_cursor(), term.cbreak():
        global speed
        inp = ""
        while inp == "":
            inp = term.inkey()
            if inp == "1":
                speed = 0.08
            elif inp == "2":
                speed = 0.06
            elif inp == "3":
                speed = 0.04
            else:
                rate_choice()


def intro_screen():
    """
    Loads the title screen.
    """

    print(term.clear + term.move_y(term.height // 2 - 5))
    print(term.bold_white_on_darkgreen(term.center("")))
    print(term.bold_white_on_darkgreen(term.center("Conway's Game of Life")))
    print(
        term.bold_white_on_darkgreen(
            term.center("\u25A0 \u25A0 \u25A0 \u25A0 \u25A0 \u25A0 \u25A0")
        )
    )
    print(term.white_on_darkgreen(term.center("Press any key to continue.")))
    print(term.bold_white_on_darkgreen(term.center("")))

    with term.hidden_cursor(), term.cbreak():
        inp = ""
        while inp == "":
            inp = term.inkey()


if __name__ == "__main__":
    with term.fullscreen():
        main()
