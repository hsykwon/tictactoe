#http://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html

from graphics import *
import random
from Tkinter import *
import sys
import time

#the center of each coordinate box
#coordinates = [[150, 150], None, None, None, None, None, None, None, None];
coordinates = [[150, 150], [250, 150], [350, 150], [150, 250], [250, 250], [350, 250], [150, 350], [250, 350], [350,350]];
coordinates_shape = ["A", "A", "A", "A", "A", "A", "A", "A", "A"] #this is going to contain a list that matches the coordinate with the shape (either a circle (C) or X)
coordinates_copy = [[150, 150], [250, 150], [350, 150], [150, 250], [250, 250], [350, 250], [150, 350], [250, 350], [350,350]];
coordinates_shape_copy = ["A", "A", "A", "A", "A", "A", "A", "A", "A"] #this is going to contain a list that matches the coordinate with the shape (either a circle (C) or X)
coordinates_shape_copy_checker = [0, 0, 0, 0, 0, 0, 0, 0, 0] #this is to make sure that every time the "isWinner" is looped through, the coordinates_shape_copy isn't overridden with "A". It will only be overriden if there is a "0"
win = GraphWin("Tic Tac Toe", 500, 500)
global winner
winner = ""

def draw_board():
    h_line_1 = Line(Point(100,200), Point(400,200))
    h_line_1.draw(win)
    h_line_2 = Line(Point(100,300), Point(400,300))
    h_line_2.draw(win)

    v_line_1 = Line(Point(200,100), Point(200,400))
    v_line_1.draw(win)
    v_line_2 = Line(Point(300,100), Point(300,400))
    v_line_2.draw(win)

    #win.getMouse() #pausing to view result

def draw_circle(coordinates, which_coordinate):
    circle = Circle(Point(coordinates[which_coordinate][0], coordinates[which_coordinate][1]), 20)
    
    coordinates_shape[which_coordinate] = "C" 
    coordinates_shape_copy[which_coordinate] = "C"
    coordinates_shape_copy_checker[which_coordinate] = 1
    circle.draw(win)

def draw_x(coordinates, which_coordinate):
    x_line_1 = Line(Point(coordinates[which_coordinate][0]-25, coordinates[which_coordinate][1]-25), Point(coordinates[which_coordinate][0]+25, coordinates[which_coordinate][1]+25))
    x_line_1.draw(win)
    x_line_2 = Line(Point(coordinates[which_coordinate][0]-25, coordinates[which_coordinate][1]+25), Point(coordinates[which_coordinate][0]+25, coordinates[which_coordinate][1]-25))
    x_line_2.draw(win)
    coordinates_shape[which_coordinate] = "X" 
    coordinates_shape_copy[which_coordinate] = "X"
    coordinates_shape_copy_checker[which_coordinate] = 1

"""
make sure to check if there's already a shape in the particular coordinate of the board
integrate random to pick a random spot
"""
def computer_turn():
    time.sleep(1)
    if all(coordinate == None for coordinate in coordinates):
            winner = "none"
            end_game()

    which_coordinate = random.randint(0,8)
    while coordinates[which_coordinate] is None: #if the random number corresponds to an index on the list with None, then it picks another random number
        which_coordinate = random.randint(0,8)

    for coordinate in range(0,9): #checking each coordinate to see which ones are open
        if coordinates[coordinate] is not None: 
            if is_winner(coordinate, coordinates_copy, "C") is True: #if there is a spot where the computer can win, put the circle there
                which_coordinate = coordinate
                draw_circle(coordinates, which_coordinate)
                coordinates[which_coordinate] = None
                coordinates_copy[which_coordinate] = None
                global winner
                winner = "computer"
                end_game()
                return #exit the function
                

    for coordinate in range(0,9):
        if coordinates[coordinate] is not None: 
            if is_winner(coordinate, coordinates_copy, "X") is True: #if there is a spot where the user can win, block that spot with a circle
                which_coordinate = coordinate
                draw_circle(coordinates, which_coordinate)
                coordinates[which_coordinate] = None
                coordinates_copy[which_coordinate] = None
                return #exit the function

    draw_circle(coordinates, which_coordinate)
    coordinates[which_coordinate] = None
    coordinates_copy[which_coordinate] = None

"""
prompt the user to pick a spot for their turn (choosing a number 1-9 and using that as a which_coordinate)
"""
def user_turn():
    if all(coordinate == None for coordinate in coordinates):
        global winner
        winner = "none"
        end_game()
    which_coordinate = int(raw_input("Which coordinate would you like to place your symbol in? "))-1
    if which_coordinate > 9:
        which_coordinate = int(raw_input("Invalid coordinate. Enter another coordinate: "))-1
    while coordinates[which_coordinate] is None:
        which_coordinate = int(raw_input("Invalid coordinate. Enter another coordinate: "))-1 #if the user chooses a coordinate that is already taken
    draw_x(coordinates, which_coordinate)
    # draw_x(coordinates_copy, which_coordinate)
    coordinates[which_coordinate] = None
    coordinates_copy[which_coordinate] = None

def check_three_in_a_row(coordinates, coordinates_shape):
    if coordinates[0] is None and coordinates[1] is None and coordinates[2] is None:
        if coordinates_shape[0] is "C" and coordinates_shape[1] is "C" and coordinates_shape[2] is "C":
            return True
        if coordinates_shape[0] is "X" and coordinates_shape[1] is "X" and coordinates_shape[2] is "X":
            return True
    if coordinates[3] is None and coordinates[4] is None and coordinates[5] is None:
        if coordinates_shape[3] is "C" and coordinates_shape[4] is "C" and coordinates_shape[5] is "C":
            return True
        if coordinates_shape[3] is "X" and coordinates_shape[4] is "X" and coordinates_shape[5] is "X":
            return True
    if coordinates[6] is None and coordinates[7] is None and coordinates[8] is None:
        if coordinates_shape[6] is "C" and coordinates_shape[7] is "C" and coordinates_shape[8] is "C":
            return True
        if coordinates_shape[6] is "X" and coordinates_shape[7] is "X" and coordinates_shape[8] is "X":
            return True

    if coordinates[0] is None and coordinates[3] is None and coordinates[6] is None:
        if coordinates_shape[0] is "C" and coordinates_shape[3] is "C" and coordinates_shape[6] is "C":
            return True
        if coordinates_shape[0] is "X" and coordinates_shape[3] is "X" and coordinates_shape[6] is "X":
            return True
    if coordinates[1] is None and coordinates[4] is None and coordinates[7] is None:
        if coordinates_shape[1] is "C" and coordinates_shape[4] is "C" and coordinates_shape[7] is "C":
            return True
        if coordinates_shape[1] is "X" and coordinates_shape[4] is "X" and coordinates_shape[7] is "X":
            return True
    if coordinates[2] is None and coordinates[5] is None and coordinates[8] is None:
        if coordinates_shape[2] is "C" and coordinates_shape[5] is "C" and coordinates_shape[8] is "C":
            return True
        if coordinates_shape[2] is "X" and coordinates_shape[5] is "X" and coordinates_shape[8] is "X":
            return True

    if coordinates[0] is None and coordinates[4] is None and coordinates[8] is None:
        if coordinates_shape[0] is "C" and coordinates_shape[4] is "C" and coordinates_shape[8] is "C":
            return True
        if coordinates_shape[0] is "X" and coordinates_shape[4] is "X" and coordinates_shape[8] is "X":
            return True
    if coordinates[2] is None and coordinates[4] is None and coordinates[6] is None:
        if coordinates_shape[2] is "C" and coordinates_shape[4] is "C" and coordinates_shape[6] is "C":
            return True
        if coordinates_shape[2] is "X" and coordinates_shape[4] is "X" and coordinates_shape[6] is "X":
            return True

def is_winner(coordinate, coordinates_copy, shape):
    original_coordinate = coordinates_copy[coordinate]
    coordinates_copy[coordinate] = None
    coordinates_shape_copy[coordinate] = shape
    if check_three_in_a_row(coordinates_copy, coordinates_shape_copy) is True:
        coordinates_shape_copy[coordinate] = "C"
        return True
    else:
        coordinates_copy[coordinate] = original_coordinate
        if coordinates_shape_copy_checker[coordinate] == 0:
            coordinates_shape_copy[coordinate] = "A"

def end_game():
    print "Game over!"
    if winner == "computer":
        print "You lost!"
    elif winner == "none":
        print "Tie!"
    elif winner == "user":
        print "You won!"
    time.sleep(3)
    sys.exit()

def main():
    while winner == "":
        draw_board()
        computer_turn()
        # if winner == "computer":
        #     break
        #     time.sleep(10)
        # if winner == "none":
        #     break
        #     time.sleep(10)
        user_turn()

main()