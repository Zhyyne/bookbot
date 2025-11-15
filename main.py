from stats import count_words
from stats import count_chars

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def main():
    book_path = "./books/frankenstein.txt"
    output_string = get_book_text(book_path)

    word_count = count_words(output_string)
    character_count = count_chars(output_string)
    
    print(f"Found {word_count} total words")
    print(character_count)

main()

