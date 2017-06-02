from random import randint
import HangmanFuncts

while True:
    # Print out a welcome and instructions
    print('\nWelcome to Hangman: the super inappropriate game that is somehow okay for kids to play!\n')
    print('Here are the rules:', '1. Only use lowercase letters.', '2. For each incorrect guess you lose a life.',
          '3. If you runs out of lives you lose!\n', sep='\n')

    # Make a list of random words
    Words = ['calculator', 'music', 'optimal', 'diagonal', 'hexagonal', 'muscle', 'irate', 'python', 'libraries']

    # Get a random word from Words
    RandWord = HangmanFuncts.random_word(Words)

    # Create a variable to hold correct letters to compare against RandWord
    GuessReference = ''

    # Create a variable to hold all guessed letters to prevent guessing the same letter
    AllGuessedLetters = ''

    # Pick an arbitrary number for the max number of guesses
    NumLives = 3

    # Print number of lives and a visual of how many letters in RandWord
    print('You have', NumLives, 'lives.', 'Let\'s begin!')
    print(HangmanFuncts.draw_spaces(RandWord, GuessReference), '\n')
    
    # Create for future winningness loop breaking
    Winner = False

    # As long as you have lives, you are good to go
    while NumLives > 0:
        
        # If there are no '_' that means all of the letters have replaced them and the word if complete
        # You win!
        if '_' not in HangmanFuncts.draw_spaces(RandWord, GuessReference):
            Winner = True
            break
            
        # Holds the user's guessed letter
        Guess = str.lower(input('Enter a lower case letter: '))
        
        # If their guess is not a letter, make them enter a guess again
        if not str.isalpha(Guess):
            print('You suck. That is not even a letter.')
            continue
        elif len(Guess) > 1:
            print('You suck. That\'s too many letters.')
            continue
        elif Guess in AllGuessedLetters:
            print('You suck. you already guessed that.')
            continue

        AllGuessedLetters += Guess
        
        # See if the guessed letter is in the word
        if Guess in RandWord:
            print('You got one!')
            GuessReference += Guess
        else:
            NumLives -= 1
            print('Nope! Try Again. Remaining guesses:', NumLives, '\n')
        
        # If the letter is in the word, replace the underscore with the letter
        print(HangmanFuncts.draw_spaces(RandWord, GuessReference))

    if Winner:
        print('Hooray! You won!\n')
    else:
        print('Better luck next time.')
        print('The word was:', RandWord, '\n')

    PlayAgain = input('Want to play again? Enter \'y\' or \'n\': ')
    if PlayAgain == 'y':
        continue
    else:
        break
