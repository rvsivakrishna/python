for n in range(100,0,-1):
    print(f"{n} bottles of beer on the wall.")
    print(f"{n} bottles of beer")
    if n == 1:
        print("Take down one and no more bottles")
        print("*"*50)
    print(f" take one down, pass it around {n -1} bottles of beer.")
    print("*"*50)
