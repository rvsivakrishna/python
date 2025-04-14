print("*" * 50)
print("Welcome to the Game")
print("*" * 50)
toothpicks_left = int(input("Enter no of Toothpicks:" ))
player_1 = input("Enter player1's Name: ").capitalize()
player_2 = input("Enter player2's Name:").capitalize()
current_player = player_1
while True:
    print("|" * toothpicks_left)
    print(f"There are {toothpicks_left} toothpicks left.")
    one = int(input(f"How many do you take, {current_player} ? \n"))
    while one != 1 and one !=2 and one !=3:
        one= int(input(f"you can only choose 1, 2 or 3: "))
    toothpicks_left -= one
    if toothpicks_left <= 1:
        print(f"{current_player} won the game.")
        break
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1
		
print("Game Over")