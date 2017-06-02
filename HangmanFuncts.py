from random import randint


def random_word(words):
    # Create a variable that will hold a random number from 0 to the length of the string of words
    rand_num = randint(0, len(words)-1)

    # Use the random number to get the word at the random index
    rand_word = words[rand_num]

    return rand_word


def draw_spaces(randword, guessreference):
    # Create a variable to keep count of how many times we have looped and
    # make sure we don't go past the length of the Word
    count = 0

    # Create a variable to hold the underscores representative of the number of letters in the word
    spaces = ''

    # While the Count is less than the length of the RandWord, add an underscore
    while count < len(randword):
        if randword[count] in guessreference:
            spaces += (randword[count] + ' ')
        else:
            spaces += '_ '
        count += 1

    return spaces
