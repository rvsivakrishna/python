Input_Name=input("Enter your Name: ")
print(f"Name = {Input_Name.capitalize()} ")
Age=int(input("Enter your Age:"))
if Age >= 18:
    print("Come on in")
else:
    print("Go Home Kid")
signal=str(input("Enter Color Choice: ")).lower()
if signal == "green":
    print("Enjoy your ride!!")
elif signal == "orange":
    print("Get ready for Ride")
elif signal == "red":
    print("Take Break :)")
else:
    print("Caution!!!")
weight=float(input("Enter your weight: "))
unit=str(input("Enter unit type: ")).lower()
if unit == 'kg':
  if weight <= 60:
    print("Enjoy your food :) ")
  else:
    print("Better to avoid fatty food")
else:
  print("Oho knew only kg unit :( ")

