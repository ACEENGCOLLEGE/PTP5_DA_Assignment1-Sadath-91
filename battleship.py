"""
Battleship Project
Name:
Roll No:
"""

import battleship_test as test


project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###



from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4

'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    # Initialize game data like rows, columns, boards, ships, and other parameters.
    pass

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    # Render both user and computer grids along with any temporary or final states.
    pass

'''
keyPressed(data, event)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    # Handle key events to restart the game or perform specific actions.
    pass

'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    # Handle mouse events for ship placement or gameplay interactions.
    pass

'''

### STAGE 1 ###

emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    # Create and return a 2D grid initialized with EMPTY_UNCLICKED.
    pass

'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    # Generate a 3-cell ship, randomly aligned either vertically or horizontally.
    pass

'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    # Validate whether the ship placement overlaps with existing ships.
    pass

'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    # Randomly add the specified number of ships to the grid.
    pass

'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    # Render the grid on the canvas, showing or hiding ship placements based on the flag.
    pass

'''
### STAGE 2 ###



isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    # Check if the ship cells are vertically aligned.
    pass

'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    # Check if the ship cells are horizontally aligned.
    pass

'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    # Determine the cell clicked based on the event coordinates.
    pass

'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    # Visualize a temporary or placed ship on the grid.
    pass

'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    # Ensure the ship is valid in terms of placement rules and alignment.
    pass

'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    # Place a ship on the user board if it meets validity criteria.
    pass

'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    # Manage user interaction for ship placement.
    pass



### STAGE 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    # Update the board state after a user's or computer's turn.
    pass

'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col, player):
    # Execute a single turn for the user and the computer.
    pass

'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    # Generate a random valid guess for the computer's turn.
    pass

'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    # Check if all ships on the board have been sunk.
    pass

'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    # Display the game-over message based on the winner.
    pass

### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    # print("\n" + "#"*15 + " STAGE 1 TESTS " +  "#" * 16 + "\n")
    # test.stage1Tests()
    # test.testEmptyGrid()
    # test.testCreateShip()
    # test.testCheckShip()
    # test.testAddShips()
    # test.testGrid()


    ## Uncomment these for STAGE 2 ##

    # print("\n" + "#"*15 + " STAGE 2 TESTS " +  "#" * 16 + "\n")
    # test.stage2Tests()
    # test.testIsVertical()
    # test.testIsHorizontal()

    # test.testGetClickedCell()
    # test.testShipIsValid()
    

    ## Uncomment these for STAGE 3 ##
    
    # print("\n" + "#"*15 + " STAGE 3 TESTS " +  "#" * 16 + "\n")
    # test.stage3Tests()
    # test.testUpdateBoard()
    # test.testGetComputerGuess()
    # test.testIsGameOver()
    # test.testDrawGameOver()
    

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
