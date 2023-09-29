# Calculation Program
# Date: Sept. 28, 2023

print("Welcome to Python Calculator!")

ans: float = 0.0

mode = ""

options = """
Options:
Enter '+' to add mode
Enter '-' to subtract mode
Enter '*' to multiply mode
Enter '/' to divide mode
Enter '^' to power mode
Enter '?' to see the options again
Enter 'quit' to end the program
"""

print(options)

while True:
    user_input = input("-> ")

    if user_input == "quit":
        break        
    elif user_input == "?":
        print(options)
    elif user_input.isnumeric():
        user_input = float(user_input)
        if mode == "":
            ans = user_input
        elif mode == "+":
            ans += user_input
        elif mode == "-":
            ans -= user_input
        elif mode == "*":
            ans *= user_input
        elif mode == "/":
            ans /= user_input
        elif mode == "^":
            ans **= user_input
        print(ans)
    elif user_input in ("+", "-", "*", "/"):
        mode = user_input
    else:
        print("Unknown input")





