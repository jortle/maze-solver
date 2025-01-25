# Maze Solver Project

### Summary of Project

This project is a simple maze solver written in python using TKinter. It is started as the tutorial at [boot.dev](https://www.boot.dev/courses/build-maze-solver-python). I have added some buttons to it to make it more interactive. 

This project takes us step by step through the creation of a maze, including drawing and generating all the cells. Breaking down the walls of the cells to make hallways. Lastly, it takes us through creating a depth-first search algorithm to solve the maze and generating a line to animate this process. 
### Features

#### From the tutorial
* maze structure generation
* depth-first search algorithm

#### What I have added
* buttons to create a new maze, reset the maze, and solve the maze
* refactoring to make the button logic easier to create and maintain
* breadth-first search algorithm a button to switch the algorithm

#### to add
* buttons to pause/play the animation
* a way to select the rows and columns of the maze

### How to run
1. clone the repo
2. run `python main.py`
3. to start a new maze, click the "New Maze" button
4. after a maze is generated you can click solve maze to show the algorithm solving it, or create a new maze by clicking the make new maze button
5. if you want to reset the maze after the algorithm is done, click the reset maze button. This will be better after I implement the other algorithms and you can see how each solves the maze.
