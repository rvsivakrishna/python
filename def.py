
name = str(input("enter name: "))
customer_input = str(input("enter your msg (default msg is Hello)"))
if customer_input == "":
        customer_input = "Hello"
        
def greet(person="stranger",msg="Hello"):
    print(f"{msg} , {person}")


greet(name,customer_input)

