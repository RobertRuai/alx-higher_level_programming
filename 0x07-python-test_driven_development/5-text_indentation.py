#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """function that prints a text with 2 new lines after ., ? and : chars
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
