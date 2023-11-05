# Function must be defined before its use unless... (see 019-main.py)
def hello(to="world"):
    print(f"hello, {to}")

hello()
name = input("What's your name? ")
hello(name)