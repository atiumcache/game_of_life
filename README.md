# Conway's Game of Life

A simple implementation of John Conway's Game of Life. 

![](images/acorn_seed.png)

Conway's Game of Life is a cellular automaton, a mathematical model, and a simulation of a two-dimensional grid of square cells. Each cell can be in one of two states, alive or dead. The state of a cell evolves over discrete time steps based on a set of rules:

- **Underpopulation**: A live cell with fewer than two live neighbors dies (loneliness).
- **Survival**: A live cell with two or three live neighbors survives to the next generation.
- **Overpopulation**: A live cell with more than three live neighbors dies (overcrowding).
- **Reproduction**: A dead cell with exactly three live neighbors becomes alive.

These rules lead to the emergence of complex patterns and behaviors, and the "game" is not played by a player but rather evolves on its own based on the initial configuration of live and dead cells. The Game of Life is a classic example of cellular automata and has applications in computer science, mathematics, and artificial life studies.

## Demo

View the program in action: 

![program demo](images/game-of-life-demo.gif)

## Seed Options

I have implemeneted 5 different seeds for the user to choose from:

- **Beacon**: An *oscillator* that switches back and forth between two states. 
- **R-Pentomino**: A *methuselah* that evolves over many generations, before eventually stabilizing.
- **Diehard**: A pattern that disappears after 130 generations. 
- **Acorn**: A pattern that takes 5206 generations to generate 633 cells.
- **Block Switch Engine**: An infinite growth pattern that leaves stable blocks in its wake.

## Other Options

3 speed options: slow, medium, fast. This corresponds to the speed at which each generation occurs. 

## Usage

The only dependencies required for this script are `blessed` and `numpy`. 
These can be installed with:

	pip install numpy

and

	pip install blessed

Then, clone this repository or download the `game_of_life.py` script directly.

With your dependencies installed, execute the following to run the script:

	python game_of_life.py

That's it --- the program will prompt you with a few options before allowing you to create life. 
