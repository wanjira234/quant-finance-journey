def geuss_num():
    guess = int(input("enter a guess: "))
    return guess

def main():
    guess = geuss_num()
    if guess == 34:
        print("you guessed it right")
    else:
        print("you guessed it wrong")

# always remember to call the function
main()