# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tKinter import *

root = TK()

root.title("fibonacci")
root.geometry("400x400")

label_series = Label(root, text ="fibonacci series: ")
label_flower = Label(root)
label_sprial = Label(root)

def Fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    conter = 1
    while (counter <=num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        label_flower["text"] = "flower is fully bloomed "
        label_spiral["text"] = "spirals in right direction are" + str
       