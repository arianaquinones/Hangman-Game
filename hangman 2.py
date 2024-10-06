import random
from words import word_list

# Function to get a random word of a specified length from the word list
def get_word_by_length(length):
    suitable_words = [word for word in word_list if len(word) == length]
    if suitable_words:
        return random.choice(suitable_words).upper()
    else:
        return None

# Function to play the hangman game
def play(word):
    word_completion = "_" * len(word)  # String to display the guessed letters and underscores
    guessed = False  # Flag to indicate if the word has been guessed
    guessed_letters = []  # List to store guessed letters
    guessed_words = []  # List to store guessed words
    tries = 6  # Number of tries the player has
    score = 0  # Player's score
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        # If the guess is a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                score -= 5  # Deduct points for incorrect guess
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                score += 10  # Add points for correct guess
                if "_" not in word_completion:
                    guessed = True
        
        # If the guess is a word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                score -= 5  # Deduct points for incorrect guess
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
                score += 10 * len(word)  # Bonus for guessing the whole word
        
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(word_completion)
        print(f"Score: {score}")
        print("\n")
    
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
    print(f"Final Score: {score}")

# Function to display the hangman stages
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# Main function to start the game
def main():
    while True:
        try:
            length = int(input("Enter the desired word length: "))
            word = get_word_by_length(length)
            if word:
                play(word)
            else:
                print(f"No words of length {length} found. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        if input("Play Again? (Y/N) ").upper() != "Y":
            break

if __name__ == "__main__":
    main()