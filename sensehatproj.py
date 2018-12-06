from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()

purple = (139,0,139)
orange = (197,179,88)

matrix = [[orange for column in range(8)] for row in range(8)]

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

def gen_pipes(matrix):
   for row in matrix:
       row[-1]=purple
   gap = randint(1,6)
   matrix[gap][-1]=orange
   matrix[gap-1][-1]=orange
   matrix[gap+1][-1]=orange
   return matrix

def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i+1]
        row[-1]=orange
    return matrix

while True:
    matrix = gen_pipes(matrix)
    for i in range(3):
        sense.set_pixels(flatten(matrix))
        matrix = move_pipes(matrix)
        sleep(1)

matrix = gen_pipes(matrix)
sense.set_pixels(flatten(matrix))
matrix = move_pipes(matrix)
