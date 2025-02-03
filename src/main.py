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
            return 10
        elif difficulty == "2":
            print("Great! You have selected the Medium difficulty level.")
            return 5
        elif difficulty == "3":
            print("Great! You have selected the Hard difficulty level.")
            return 3
        else:
            print("Invalid option. Please, select between 1 (Easy), 2 (Medium) or 3 (Hard).")            
          
### Rest of the requirements: Definition of the rest of the game

def game():
    welcomeMessage()
    secretNo = rd.randint(1, 100)
    attempts = difficultyLevel()
    usedAttempts = 0
    
    while usedAttempts > 0:
        try:
            guess = int(input(f"Enter your guess: "))
        except ValueError:
            print("Please insert a valid number.")
            continue
        
        usedAttempts += 1
        attempts -= 1
        