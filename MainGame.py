from Live import load_game, welcome

print(welcome("ishai"))
try:
    load_game()

except ValueError:
    print("please enter a valid number")
