print("*" * 50)
print("Welcome to the Game")
print("*" * 50)
toothpicks_left = int(input("Enter no of Toothpicks:" ))
player_1 = input("Enter player1's Name: ").capitalize()
player_2 = input("Enter player2's Name:").capitalize()
while True:
    print("|" * toothpicks_left)
    print(f"There are {toothpicks_left} toothpicks left.")
    one = int(input(f"How many do you take, {player_1} ? \n"))
    toothpicks_left -= one
    if toothpicks_left <= 1:
        print(f"{player_1} won the game.")
        break
    print("|" * toothpicks_left)
    print(f"There are {toothpicks_left} toothpicks left.")
    two = int(input(f"How many do you take, {player_2} ? \n"))
    toothpicks_left -= two
    if toothpicks_left <= 1:
        print(f"{player_2} won the game.")
        break
print("Game Over")





