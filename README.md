# Conway's Game of Life

A simple implementation of John Conway's Game of Life. 

![](images/acorn_seed.png)

- [About](#about)
- [Demo](#demo)
- [Options](#options)
	- [Seeds](#seeds)
	- [Other Options](#other-options)
- [Usage](#usage)
- [Future Work](#future-work)
- [License](#license)

## About

The Game of Life is a cellular automaton, a mathematical model, and a simulation of a two-dimensional grid of square cells. Each cell can be in one of two states, alive or dead. The state of a cell evolves over discrete time steps based on a set of rules:

- **Underpopulation**: A live cell with fewer than two live neighbors dies (loneliness).
- **Survival**: A live cell with two or three live neighbors survives to the next generation.
- **Overpopulation**: A live cell with more than three live neighbors dies (overcrowding).
- **Reproduction**: A dead cell with exactly three live neighbors becomes alive.

These rules lead to the emergence of complex patterns and behaviors, and the "game" is not played by a player but rather evolves on its own based on the initial configuration of live and dead cells. The Game of Life is a classic example of cellular automata and has applications in computer science, mathematics, and artificial life studies.

## Demo

View the program in action: 

![program demo](images/game-of-life-demo.gif)

## Options

### Seeds

The _seed_ is the starting cells arrangement that influences the rest of the game. We have implemeneted 5 different seeds for the user to choose from:

- **Beacon**: An *oscillator* that switches back and forth between two states. 
- **R-Pentomino**: A *methuselah* that evolves over many generations, before eventually stabilizing.
- **Diehard**: A pattern that disappears after 130 generations. 
- **Acorn**: A pattern that takes 5206 generations to generate 633 cells.
- **Block Switch Engine**: An infinite growth pattern that leaves stable blocks in its wake.

### Other Options

There are 3 speed options: slow, medium, fast. This corresponds to the speed at which each generation occurs. 

## Usage

### Linux/UNIX

Download the `game_of_life` executable file from this repository. Add it to your PATH:

	export PATH="/path/to/executable:$PATH"

Or, just move the file into your `usr/local/bin` folder (or equivalent). 

Then, call the program from the terminal to play: 

	game_of_life

### Windows/Manual Operation

We don't have a Windows `.exe` file yet. You can run the program manually.

The only dependencies required for this script are `blessed` and `numpy`. 
These can be installed with:

	pip install numpy blessed

Then, clone this repository or just download the `game_of_life.py` script directly.

With your dependencies installed, execute the following to run the script:

	python3 game_of_life.py

That's it --- the program will prompt you with a few options before allowing you to create life. 

## Future Work

- Change background/cell colors.
- More starting seed options.
- Allow the user to input their own starting seed!

## License 

Distributed under the MIT License. See LICENSE.txt for more information.
