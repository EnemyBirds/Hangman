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
    GuessLetter = ''

    # Pick an arbitrary number for the max number of guesses
    NumLives = 3

    # Print number of lives and a visual of how many letters in RandWord
    print('You have', NumLives, 'lives.', 'Let\'s begin!')
    print(HangmanFuncts.draw_spaces(RandWord, GuessLetter), '\n')

    Winner = False

    while NumLives > 0:

        if '_' not in HangmanFuncts.draw_spaces(RandWord, GuessLetter):
            Winner = True
            break

        Guess = str.lower(input('Enter a lower case letter: '))

        if Guess in RandWord:
            print('You got one!')
            GuessLetter += Guess
        else:
            NumLives -= 1
            print('Nope! Try Again. Remaining guesses:', NumLives, '\n')

        print(HangmanFuncts.draw_spaces(RandWord, GuessLetter))

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
