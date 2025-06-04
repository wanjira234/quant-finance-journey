def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return 
        
    players = input("multiplayer or single-player? ")
    if not (players == "multiplayer" or players == "single-player"):
        print("Enter a valid number of players")
        return 
    if difficulty == "Difficult" and players == "multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")
        

def recommend(game):
    
    print(f"You might like: {game}")

main()