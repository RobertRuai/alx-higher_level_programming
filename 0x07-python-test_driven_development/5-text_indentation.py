#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """function that prints a text with 2 new lines after ., ? and : chars
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n_chars = ['.', '?', ':']

    for c in n_chars:
        text = text.replace(c, c + "\n\n")
    l_lines = [lines.strip(' ') for lines in text.split('\n')]
    n_lines = "\n".join(l_lines)
    print(n_lines, end="")
