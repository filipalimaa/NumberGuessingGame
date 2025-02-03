import random as rd

### First Requirement: Display a welcome message along with the rules when the game starts.

def welcomeMessage():
    print("""
          ==========================================
             Welcome to the Number Guessing Game!
          ==========================================
          I'm thinking of a number between 1 and 100.
        You have 5 chances to guess the correct number.
    
             GOOD LUCK!""")
    

### Second Requirement: Selection of the difficulty level.

def difficultyLevel():
    while True:
        difficulty = input("""Please select the difficulty level:
                            1. Easy (10 chances)
                            2. Medium (5 chances)
                            3. Hard (3 chances)""")
        
        if difficulty == "1":
            print("Great! You have selected the Easy difficulty level.")
        elif difficulty == "2":
            print("Great! You have selected the Medium difficulty level.")
        elif difficulty == "3":
            print("Great! You have selected the Hard difficulty level.")
        else:
            print("Invalid option. Please, select between 1 (Easy), 2 (Medium) or 3 (Hard).")            
          