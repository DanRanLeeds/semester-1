# Week 1.6, Session 1: Task 1

import math


class Point: #definition of the class called point
    """
    A Point in 2D space.
    """

    def __init__(self, x, y): #definition of the constructor method that initializes the x & y coordinates of the point being created
        """
        Creates a Point, given x & y coordinates.
        """
        if not isinstance(x, int): #if statement to check if x coordinate is an integer
            raise TypeError("x coordinate must be an integer") #if it isnt an integer, a type error is raised

        if not isinstance(y, int): #check if y is integer
            raise TypeError("y coordinate must be an integer") #raise type error if y is not an integer
        #defines x and y as instance variables of the Point class, and assigns them the values of the x and y parameters passed to the constructor
        self.x = x
        self.y = y

    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """
        Returns distance of this Point from another Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)
