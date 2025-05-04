def get_word_count(book_text):
    word_count = book_text.split()
    return len(word_count)

def count_characters(book_text):
    lowercase_text = book_text.lower()
    char_counts = {}
    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_counts(char_counts):
    char_list = list(char_counts.items())
    char_list.sort(key = lambda item: item[1], reverse = True)
    
    return char_list

def print_pretty(char_list):
    for char, count in char_list:
        return f"{char}: {count}" 