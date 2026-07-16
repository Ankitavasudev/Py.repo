"""
Password Generator 🔐
Generate secure, customizable passwords for various use cases.

Author: Ankita Salaria
"""

import random
import string
from typing import Optional


class PasswordGenerator:
    """Generate secure passwords with customizable options."""
    
    def __init__(self):
        """Initialize password generator."""
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate(self, 
                 length: int = 16,
                 use_uppercase: bool = True,
                 use_lowercase: bool = True,
                 use_digits: bool = True,
                 use_special: bool = True,
                 exclude_chars: Optional[str] = None) -> str:
        """
        Generate a secure password.
        
        Args:
            length: Password length (default: 16)
            use_uppercase: Include uppercase letters
            use_lowercase: Include lowercase letters
            use_digits: Include numbers
            use_special: Include special characters
            exclude_chars: Characters to exclude
        
        Returns:
            Generated password string
        """
        if length < 4:
            raise ValueError("Password length must be at least 4")
        
        # Build character pool
        pool = ""
        required = []
        
        if use_uppercase:
            pool += self.uppercase
            required.append(random.choice(self.uppercase))
        
        if use_lowercase:
            pool += self.lowercase
            required.append(random.choice(self.lowercase))
        
        if use_digits:
            pool += self.digits
            required.append(random.choice(self.digits))
        
        if use_special:
            pool += self.special
            required.append(random.choice(self.special))
        
        if not pool:
            raise ValueError("At least one character type must be enabled")
        
        # Remove excluded characters
        if exclude_chars:
            pool = ''.join(c for c in pool if c not in exclude_chars)
        
        # Generate password
        remaining_length = length - len(required)
        password_chars = required + [random.choice(pool) for _ in range(remaining_length)]
        
        # Shuffle to avoid predictable positions
        random.shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def generate_memorable(self, word_count: int = 4) -> str:
        """
        Generate a memorable password using word combinations.
        
        Args:
            word_count: Number of words to combine
        
        Returns:
            Memorable password string
        """
        words = [
            "correct", "horse", "battery", "staple", "purple",
            "monkey", "dragon", "castle", "rocket", "garden",
            "winter", "summer", "golden", "silver", "cosmic",
            "lunar", "solar", "nebula", "quasar", "pulsar"
        ]
        
        selected = [random.choice(words) for _ in range(word_count)]
        separator = random.choice(["-", "_", ".", " "])
        
        return separator.join(selected)
    
    def check_strength(self, password: str) -> dict:
        """
        Check password strength and return analysis.
        
        Args:
            password: Password to analyze
        
        Returns:
            Dictionary with strength analysis
        """
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Password is too short")
        
        # Character variety
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if any(c in self.special for c in password):
            score += 2
        else:
            feedback.append("Add special characters")
        
        # Sequential check
        sequential = sum(1 for i in range(len(password)-1) 
                        if ord(password[i+1]) - ord(password[i]) == 1)
        if sequential > 2:
            score -= 1
            feedback.append("Avoid sequential characters")
        
        # Determine strength level
        if score >= 7:
            strength = "Strong 💪"
        elif score >= 5:
            strength = "Medium 🛡️"
        else:
            strength = "Weak ⚠️"
        
        return {
            "strength": strength,
            "score": score,
            "max_score": 8,
            "feedback": feedback
        }


def main():
    """Interactive password generator."""
    gen = PasswordGenerator()
    
    print("\n" + "="*50)
    print("🔐 SECURE PASSWORD GENERATOR 🔐")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Generate random password")
        print("2. Generate memorable password")
        print("3. Check password strength")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == "1":
            length = int(input("Password length (default 16): ") or 16)
            password = gen.generate(length=length)
            print(f"\nGenerated: {password}")
            
            strength = gen.check_strength(password)
            print(f"Strength: {strength['strength']} ({strength['score']}/{strength['max_score']})")
        
        elif choice == "2":
            words = int(input("Number of words (default 4): ") or 4)
            password = gen.generate_memorable(word_count=words)
            print(f"\nMemorable: {password}")
        
        elif choice == "3":
            password = input("Enter password to check: ")
            strength = gen.check_strength(password)
            print(f"\nStrength: {strength['strength']}")
            print(f"Score: {strength['score']}/{strength['max_score']}")
            if strength['feedback']:
                print("Suggestions:")
                for f in strength['feedback']:
                    print(f"  - {f}")
        
        elif choice == "4":
            print("\nGoodbye! 👋")
            break
        
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
