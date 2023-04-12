#!/usr/bin/python3
""" a function that reads a text file """


def append_write(filename="", text=""):
    """reads a text file,appends text and prints to stdout"""
    with open(filename, mode='a') as file:
        count = file.write(text)
        return count
