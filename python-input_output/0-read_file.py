#!/usr/bin/python3
"""Write a function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """this is the function """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
