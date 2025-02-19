text_1 = int(input("Give me a number: "))
text_2 = int(input("Give me a second number: "))
text_3 = int(input("Give me a third number: "))

def multiplication(x,y,z):
    s = x*y*z
    s = s - 10
    print(s)

multiplication(text_1, text_2, text_3)

def bond(first_name="James", last_name="Bond"):
    return(f"{last_name}, {first_name} {last_name}")

def introduce(name):
    print(f"My name is {name}")

introduce(bond("James", "Smith"))

