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

def sort_chars(source_dict):
    result_list = []
    for pair in source_dict:
        char_key = { "char": pair }
        num_key = { "num": source_dict[pair] }
        new_dict = { "char": pair, "num": source_dict[pair] }
        result_list.append(new_dict)
    result_list.sort(reverse=True, key=char_num_helper)
    return result_list

def char_num_helper(key):
    return key["num"]
    