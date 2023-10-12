def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    my_list = list(phrase)
    first_letter = my_list[0]
    first_letter = first_letter.upper()
    rest = my_list[1:]
    new_list = [first_letter] + rest
    return ''.join(new_list)
