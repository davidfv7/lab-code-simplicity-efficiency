"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

numbers = {"zero": 0, "one": 1, "two": 2,"three": 3, "four": 4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}

if a not in numbers.keys() or c not in numbers.keys() or (b != "minus" and b != "plus"):
     print("I am not able to answer this question. Check your input.")
else:
   print("%s %s %s equals %s" % (a,b,c,[x for x,y  in numbers.items() if y == numbers[a]-numbers[c] ][0]))  if b == "minus" else print("%s %s %s equals %s" % (a,b,c,[x for x,y  in numbers.items() if y == numbers[a]+numbers[c] ][0]))
    
            
print("Thanks for using this calculator, goodbye :)")
