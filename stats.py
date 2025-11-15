def count_words(source_string):
    words = source_string.split()
    return len(words)

def count_chars(source_string):
    string = source_string.lower()
    results = {}
    for char in string:
        if char in results:
            results[char] += 1
        else:
            results[char] = 1
    return results