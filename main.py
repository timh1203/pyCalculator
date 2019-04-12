import re

print("Welcome To Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Please enter equation: ")
    else:
        equation = input(str(previous))

    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,.?!@#$&_=" "]', '', equation)
        if previous == 0:
            previous = eval(equation) # type becomes an int
        else:
            previous = eval(str(previous) + equation) # have to convert int to str to concat


while run:
    performMath()