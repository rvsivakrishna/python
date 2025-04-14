n=100
while n > 1:
    n -=1
    if n >= 2:
        print(f"{n} bottles of beer on the wall.")
        print(f"{n} bottles of beer")
        print(f" take one down, pass it around {n -1} bottles of beer.")
    
    if n==1:
        print(f"{n} bottle of beer on the wall.")
        print("Take down one and no more bottles")
        print("*"*50)
    
    print("*"*50)
    