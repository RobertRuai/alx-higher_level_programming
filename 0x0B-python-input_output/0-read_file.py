#!/usr/bin/python3
""" a function that reads a text file """


def read_file(filename=""):
    """reads a text file and prints to stdout"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
