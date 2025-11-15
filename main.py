
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents
    
def count_words(source_string):
    words = source_string.split()
    return len(words)

def main():
    book_path = "./books/frankenstein.txt"
    output_string = get_book_text(book_path)
    word_count = count_words(output_string)
    print(f"Found {word_count} total words")

main()

