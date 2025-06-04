def greet(input):
    if "hello" in input:
        return "Hello, there!"
    else:
        return "I'm not sure what you mean"

# call greet()
greeting  = greet("whas' up")
print(greeting)