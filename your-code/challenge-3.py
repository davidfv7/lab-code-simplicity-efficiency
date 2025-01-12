
"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""

def get_longest_side(num):
    solutions = [[x,y,z] for x in range(5,num) for y in range(4,num) for z in range(3,num) if (x*x==y*y+z*z)]
    lado = 0
    for value in solutions:
        if lado < max(value):
            lado = max(value)
    return str(lado)

num = int(input("What is the maximal length of the triangle side? Enter a number: "))

print("The longest side possible is {}".format(str(get_longest_side((num)))))