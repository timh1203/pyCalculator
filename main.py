import re

print("Welcome To Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = input("Please enter equation: ")
    if equation == "quit":
        run = False
    else:
        previous = eval(equation)
        print("You typed: ", previous)


while run:
    performMath()