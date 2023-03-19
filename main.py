import random

def higher_or_lower():
    # This function runs the Higher or Lower game
    print("Welcome to Higher or Lower!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    num_guesses = 0
    
    while True:
        guess = int(input("Take a guess: "))
        num_guesses += 1
        
        if guess < secret_number:
            print("Higher...")
        elif guess > secret_number:
            print("Lower...")
        else:
            print(f"Congratulations, you guessed the secret number ({secret_number}) in {num_guesses} guesses!")
            break

if __name__ == "__main__":
    higher_or_lower()