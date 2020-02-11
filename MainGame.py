from Live import load_game, welcome
from colorama import init

init()  # colors for prints (Mandatory!!)

print(welcome("ishai")[0])
print(welcome("ishai")[1])
try:
    load_game()

except ValueError:
    print("please enter a valid number")
