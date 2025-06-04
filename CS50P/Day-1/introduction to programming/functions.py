def greetings():
    name = input("whats your name? ")
    name = name.strip().title()
    return name

my_name = greetings()
print(f"Hello, {my_name}")