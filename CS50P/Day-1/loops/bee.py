WORDS = {"PAIR":4, "HAIR":4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("welcome to spelling bee")
#     print("Your letters are: A I R C H G")

#     while len(WORDS) > 0:
#         print(f"{len(WORDS)} words left!")
#         guess = input("Guess a word: ")

#  # TODO: check if guess is in dictionary
#         if guess == "GRAPHIC":
#             WORDS.clear()
#             print("You Won!!.   ")
#         if guess in WORDS.keys():
#             points = WORDS.pop(guess)
#             print(f"Good job! you scored {points} points.")
    for word, points in WORDS.items():

        print(f"{word} was worth {points} points.")
       
    print("That game was good!")

main()