import sys

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        content = file.read()
    return content

from stats import get_word_count
from stats import count_characters
from stats import sort_counts
from stats import print_pretty

def main():
    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    word_count = get_word_count(book_text)
    num_chars = count_characters(book_text)
    sorted = sort_counts(num_chars)
    pretty = print_pretty(sorted)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted:
            print(f"{char}: {count}")
    print("============= END ===============")

main()