def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiouAEIOU'

    vowel_idx = [i for i in range(len(s)) if s[i] in vowels]
    re_vowels = [s[i] for i in reversed(vowel_idx)]

    result = ''.join(re_vowels.pop(
        0) if s[i] in vowels else s[i] for i in range(len(s)))

    return result
