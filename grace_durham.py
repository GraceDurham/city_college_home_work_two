import random


#Question 12 Solution 

def roll_polygon_dice(start, num_sides):
	"""Return rolled value of any polygon shape dice"""

	roll = random.randint(start, num_sides)

	return roll


#Question 13 Solution

import turtle



def segment_a(turtle):
    """Represents segment a in seven segments"""
    turtle.pendown()
    turtle.forward(10)
    
    
def segment_b(turtle):
    """Represents segment b in seven segments"""
    turtle.pendown()
    turtle.forward(10)
    
def segment_c(turtle):
    """Represents segment c in seven segments"""
    turtle.pendown()
    turtle.forward(10)
    
def segment_d(turtle):
    """Represents segment d in seven segments"""
    turtle.pendown()
    turtle.forward(10)
    
def segment_e(turtle):
    """Represents segment e in seven segments"""
    turtle.pendown()
    turtle.forward(10)
    
def segment_f(turtle):
    """Represents segment f in seven segments"""
    turtle.pendown()
    turtle.forward(10)
    
def segment_g(turtle):
    """Represents segment g in seven segments"""
    turtle.pendown()
    turtle.forward(10)

def spaces_right(turtle):
    """turn turtle right with a space between segments"""
    turtle.penup()
    turtle.right(90)
    turtle.forward(3)
    
def space_3_half(turtle):
    turtle.penup()
    turtle.forward(3)

def space_left(turtle):
    """turn turtle left with a space between segments"""
    turtle.penup()
    turtle.left(90)
    turtle.forward(3)

    
def move_turtle_to_right(turtle):
    """Moves turtle to the right and forward with the pen up"""
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

def face_turtle_left(turtle):
    """Moves turtle with pen up left and forward"""
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    
def draw_number_zero(turtle, number):
    """draws the number zero with seven segments"""
    if number == 0:
        turtle.home()
        segment_a(turtle)
        spaces_right(turtle)
        segment_b(turtle)
        space_3_half(turtle)
        segment_c(turtle)
        spaces_right(turtle)
        segment_d(turtle)
        spaces_right(turtle)
        segment_e(turtle)
        turtle.penup()
        turtle.forward(3)
        segment_f(turtle)
       
    

def draw_number_one(turtle, number):
    """draws the number one with seven segments"""
    if number == 1:
        spaces_right(turtle)
        segment_b(turtle)
        space_3_half(turtle)
        segment_c(turtle)
        turtle.penup()
        turtle.home()
        
def draw_number_two(turtle, number):
    """draws the number two with seven segments"""
    if number == 2:
        turtle.home()
        segment_a(turtle)
        spaces_right(turtle)
        segment_b(turtle)
        turtle.penup()
        turtle.right(90)
        turtle.forward(3)
        segment_g(turtle)
        space_left(turtle)
        segment_e(turtle)
        space_left(turtle)
        segment_d(turtle)
        turtle.penup()
        turtle.forward(10)
        
        

def draw_number_three(turtle, number):
    """draws the number three with seven segments"""
    if number == 3:
        turtle.home()
        segment_a(turtle)
        spaces_right(turtle)
        segment_b(turtle)
        turtle.penup()
        turtle.forward(3)
        turtle.right(90)
        segment_g(turtle)
        turtle.right(180)
        turtle.penup()
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(3)
        segment_c(turtle)
        turtle.penup()
        turtle.right(90)
        turtle.forward(3)
        segment_d(turtle)
        turtle.penup()
        turtle.home()
        
def draw_number_four(turtle, number):
    """draws the number four with seven segments"""
    if number == 4:
        turtle.home()
        turtle.left(90)
        turtle.penup()
        turtle.forward(3)
        segment_f(turtle)
        turtle.penup()
        turtle.right(90)
        turtle.forward(13)
        turtle.right(90)
        segment_b(turtle)
        turtle.penup()
        turtle.right(90)
        turtle.forward(3)
        segment_g(turtle)
        turtle.penup()
        turtle.right(180)
        turtle.forward(13)
        turtle.right(90)
        turtle.forward(3)
        segment_c(turtle)
        turtle.penup()
        turtle.home()
        
        
def draw_number_five(turtle, number):
    """draws the number five with seven segments"""
    if number == 5:
        turtle.home()
        turtle.left(90)
        segment_f(turtle)
        spaces_right(turtle)
        segment_a(turtle)
        turtle.penup()
        turtle.left(180)
        turtle.forward(13)
        turtle.left(90)
        turtle.forward(13)
        turtle.left(90)
        segment_g(turtle)
        spaces_right(turtle)
        segment_c(turtle)
        spaces_right(turtle)
        segment_d(turtle)
        spaces_right(turtle)
        
        turtle.home()
        
        
def draw_number_six(turtle, number):
    """draws the number six with seven segments"""
    if number == 6:
        turtle.home()
        turtle.left(90)
        segment_f(turtle)
        spaces_right(turtle)
        segment_a(turtle)
        turtle.penup()
        turtle.left(180)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        segment_g(turtle)
        spaces_right(turtle)
        segment_c(turtle)
        spaces_right(turtle)
        segment_d(turtle)
        spaces_right(turtle)
        segment_e(turtle)
        turtle.penup()
        turtle.home()
        
        
def draw_number_seven(turtle, number):
    """draws the number seven with seven segments"""
    if number == 7:
        turtle.home()
        segment_a(turtle)
        spaces_right(turtle)
        segment_b(turtle)
        space_3_half(turtle)
        segment_c(turtle)
        turtle.penup()
        turtle.home()


    
def draw_number_eight(turtle, number): 
    """draws the number eight with seven segments"""
    if number == 8:
        turtle.home()
        segment_a(turtle)
        spaces_right(turtle)
        segment_b(turtle)
        space_3_half(turtle)
        segment_c(turtle)
        spaces_right(turtle)
        segment_d(turtle)
        spaces_right(turtle)
        segment_e(turtle)
        turtle.penup()
        turtle.right(90)
        turtle.forward(3)
        segment_g(turtle)
        turtle.penup()
        turtle.forward(3)
        turtle.right(180)
        turtle.forward(16)
        turtle.right(90)
        turtle.forward(3)
        segment_f(turtle)


def draw_number_nine(turtle, number):
    """draws the number nine with seven segments"""
    if number == 9:
        turtle.home()
        turtle.left(90)
        turtle.penup()
        turtle.forward(3)
        segment_f(turtle)
        spaces_right(turtle)
        segment_a(turtle)
        spaces_right(turtle)
        segment_b(turtle)
        turtle.penup()
        turtle.right(90)
        turtle.forward(3)
        segment_g(turtle)
        turtle.penup()
        turtle.right(180)
        turtle.forward(13)
        turtle.right(90)
        turtle.forward(3)
        segment_c(turtle)
        turtle.penup()
        turtle.home()
   





#Question 15 Solution 

def is_prime(num):
	"""Return true if number is a prime number, return false if number is not a prime number"""
	if num < 2:
		return False

	for i in range(2,num):
		if num % i == 0:
			return False
	return True


def print_prime(start_num, end_num):
	"""Print out all prime numbers between two given numbers inclusive"""
	for num in range(start_num, end_num + 1):
		if is_prime(num):
			print(num)


    
        
    
def main():

	print_prime(1, 23)
	sides = int(input("How many sides is this polygon"))
	print(roll_polygon_dice(1,sides))
	import turtle
    
	wn = turtle.Screen()             # Set up the window and its attributes
	wn.bgcolor("lightgreen")

	turtle = turtle.Turtle()           # create tess and set some attributes
	turtle.shape("turtle")

	number = int(input("Please input a number"))

	draw_number_zero(turtle, number)
	draw_number_one(turtle, number)
	draw_number_two(turtle, number)
	draw_number_three(turtle, number)
	draw_number_four(turtle, number)
	draw_number_five(turtle, number)
	draw_number_six(turtle, number)
	draw_number_seven(turtle, number)
	draw_number_eight(turtle, number)
	draw_number_nine(turtle, number)


	wn.exitonclick()
    
    
main()