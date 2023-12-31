def print_upper_words(words):
    """ print out each word on a separate line ( all upper case )
    -> ['hello','hi','goodbye']
    ->HELLO
    ->HI
    ->GOODBYE
    """

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """ print out each word on a separate line ( all upper case )
    -> ['hello','hi','goodbye']
    ->HELLO
    ->HI
    ->GOODBYE
    """

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
