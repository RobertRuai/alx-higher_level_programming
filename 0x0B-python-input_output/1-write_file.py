#!/usr/bin/python3
""" a function that reads a text file """


def write_file(filename="", text=""):
    """reads a text file and prints to stdout"""
    with open(filename, mode='w') as file:
        count = file.write(text)
        return count
