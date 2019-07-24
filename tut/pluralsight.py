#!C:\Users\cciocoveanu\AppData\Local\Programs\Python\Python36-32\ python3
"""Retrieves and print words form a URL.

Usage:
    pyton pluralsight.py <URL>
"""
from urllib.request import urlopen
import sys

# "http://sixty-north.com/c/t.txt"


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_item(items):
    for item in items:
        print(item)


def square(x: int):
    return x * x


def launch_missile():
    print('Missile Launched!')


def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")


def main(url):
    words = fetch_words(url)
    print_item(words)


# module code only executed once on first import
if __name__ == "__main__":
    main(sys.argv[1])  # the 0th arg is the module filename


