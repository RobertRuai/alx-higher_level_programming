#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """function that prints a text with 2 new lines after ., ? and : chars
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.replace(". ", ".\n\n").replace("? ", "?\n\n").replace(": ", ":\n\n")
    print(lines)
