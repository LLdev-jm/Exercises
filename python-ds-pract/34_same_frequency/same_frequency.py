def freq_counter(collection):
    counter = {}

    for element in collection:
        counter[element] = counter.get(element, 0) + 1

    return counter


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

            >>> same_frequency(1212, 2211)
        True
    """

    str_num1 = str(num1)
    str_num2 = str(num2)

    return freq_counter(str_num1) == freq_counter(str_num2)
