def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    storage = []

    for paren in parens:
        if paren == '(':
            storage.append(paren)

        elif paren == ')':
            if not storage:
                return False
            else:
                storage.pop()

    return not storage
