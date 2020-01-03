#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:33:20 2019

@author: david
"""

import turtle

def draw_k(some_turtle):
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.back(50)
    some_turtle.right(45)
    some_turtle.forward(70)
    some_turtle.back(70)
    some_turtle.right(90)
    some_turtle.forward(70)
    some_turtle.back(70)
    
def draw_E(some_turtle):
    some_turtle.left(90)
    some_turtle.forward(100)
    for i in range(1,3):
        some_turtle.right(90)
        some_turtle.forward(50)
        some_turtle.back(50)
        some_turtle.left(90)
        some_turtle.back(50)
    some_turtle.right(90)
    some_turtle.forward(50)
    some_turtle.back(50)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    dave = turtle.Turtle()
    dave.shape("turtle")
    dave.color("white")
    dave.speed(5)
    dave.penup()
    dave.setpos(150, 0)
    dave.pendown()
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("white")
    angie.speed(5)
    
    draw_E(dave)
    draw_k(angie)
    

    window.exitonclick()

draw_art()
