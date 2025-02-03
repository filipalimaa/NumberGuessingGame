import random as rd

### First Requirement: Display a welcome message along with the rules when the game starts.

def welcomeMessage():
    print("""
          ==========================================
             Welcome to the Number Guessing Game!
          ==========================================
          I'm thinking of a number between 1 and 100.
        You have 5 chances to guess the correct number.
        
        Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    
             GOOD LUCK!""")