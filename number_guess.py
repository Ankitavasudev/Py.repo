"""
Number Guessing Game 🎯
A fun game where the computer picks a random number and you try to guess it!

Author: Ankita Salaria
"""

import random
import time

class NumberGuessingGame:
    """A number guessing game with difficulty levels."""
    
    def __init__(self, min_num=1, max_num=100):
        """Initialize the game with range."""
        self.min_num = min_num
        self.max_num = max_num
        self.target = None
        self.attempts = 0
        self.max_attempts = 10
        self.history = []
    
    def generate_number(self):
        """Generate a random target number."""
        self.target = random.randint(self.min_num, self.max_num)
        self.attempts = 0
        self.history = []
        return self.target
    
    def check_guess(self, guess):
        """Check user's guess and provide feedback."""
        self.attempts += 1
        self.history.append(guess)
        
        if guess == self.target:
            return "correct", "🎉 Congratulations! You got it!"
        elif guess < self.target:
            return "low", "📈 Too low! Try higher."
        else:
            return "high", "📉 Too high! Try lower."
    
    def get_hint(self):
        """Provide a hint to the user."""
        if self.target is None:
            return "No game in progress!"
        
        hints = []
        
        # Even/Odd hint
        if self.target % 2 == 0:
            hints.append("The number is even")
        else:
            hints.append("The number is odd")
        
        # Range hint
        mid = (self.min_num + self.max_num) // 2
        if self.target > mid:
            hints.append(f"It's greater than {mid}")
        else:
            hints.append(f"It's less than {mid}")
        
        # Divisibility hints
        if self.target % 5 == 0:
            hints.append("It's divisible by 5")
        if self.target % 3 == 0:
            hints.append("It's divisible by 3")
        
        return " | ".join(hints[:2])  # Return max 2 hints
    
    def get_remaining_attempts(self):
        """Get remaining attempts."""
        return self.max_attempts - self.attempts
    
    def is_game_over(self):
        """Check if game is over."""
        return self.attempts >= self.max_attempts or self.target is None
    
    def reset(self):
        """Reset the game."""
        self.target = None
        self.attempts = 0
        self.history = []


def display_welcome():
    """Display welcome message."""
    print("\n" + "="*50)
    print("🎯 NUMBER GUESSING GAME 🎯")
    print("="*50)
    print("\nI'm thinking of a number between 1 and 100")
    print("You have 10 attempts to guess it!")
    print("\nCommands: 'hint' for hint, 'quit' to exit")
    print("-"*50)


def display_result(game, won):
    """Display game result."""
    print("\n" + "="*50)
    if won:
        print("🎉 YOU WON! 🎉")
        print(f"Guessed in {game.attempts} attempts!")
    else:
        print("😔 GAME OVER!")
        print(f"The number was: {game.target}")
    
    print(f"\nYour guesses: {game.history}")
    print("="*50)


def main():
    """Main game loop."""
    display_welcome()
    
    game = NumberGuessingGame()
    game.generate_number()
    
    while not game.is_game_over():
        try:
            user_input = input(f"\nAttempts left: {game.get_remaining_attempts()} | Enter your guess: ").strip()
            
            if user_input.lower() == 'quit':
                print("\nThanks for playing! 👋")
                return
            
            if user_input.lower() == 'hint':
                print(f"\n💡 Hint: {game.get_hint()}")
                continue
            
            guess = int(user_input)
            
            if guess < game.min_num or guess > game.max_num:
                print(f"Please enter a number between {game.min_num} and {game.max_num}")
                continue
            
            result_type, message = game.check_guess(guess)
            print(message)
            
            if result_type == "correct":
                display_result(game, True)
                return
                
        except ValueError:
            print("Please enter a valid number!")
    
    display_result(game, False)


if __name__ == "__main__":
    main()
