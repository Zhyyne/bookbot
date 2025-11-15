from stats import count_words
from stats import count_chars
from stats import sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def main():
    #Check to confirm a book path has been entered
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    output_string = get_book_text(book_path)

    word_count = count_words(output_string)
    character_count = count_chars(output_string)
    sorted_char_list = sort_chars(character_count)

    print(f"Found {word_count} total words")
    print(character_count)
    
    for entry in sorted_char_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")  

main()

