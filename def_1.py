price = float(input("Price of the Goods:" ))
qty = int(input("no of goods: "))
tax = 0.02
def get_total(price, qty, tax ,dd):
    subtotal = price * qty * (1-dd)
    print(f"Total amount to be paid: {subtotal *(1+tax)}.")  
###########################################################################

dd=float(input("DD: "))
if dd != 0.01:
    dd = float(input("new DD: "))
get_total(price, qty,tax,dd)


    

