#exercise 1
def repeat(string, num):
    print(string * num)

repeat("man ", 400)

#exercise 2
def print_right(text,num=40):
    print(" " * (num - len(text)),text)
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
print_right("was amazing?!")

#exercise 3
def triangle(text, num):
    for i in range(num + 1):
        print(i * text)

triangle("L", 5)

#exercise 4
def rectangle(text, w, h):
    for i in range(h):
        print(text * w)

rectangle("H", 5,4)

#exercise 5
def bottle_verse(number):
    if number > 1:
        print(f"""
{number} bottles of beer on the wall
{number} bottles of beer 
Take one down, pass it around
{number - 1} bottles of beer on the wall
    """)
    elif number == 1: #Singular
        print(f"""
{number} bottle of beer on the wall
{number} bottle of beer 
Take one down, pass it around
{number - 1} bottles of beer on the wall
        """)

for n in range(99, 0, -1):
    bottle_verse(n)
    print()