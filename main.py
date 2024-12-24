def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{count_words(text)} words found in document\n")
    print_report(book_path, count_chars(text))
    print("")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lowered_text = text.lower()
    letter_count_map = {}
    for letter in lowered_text:
        letter = letter.lower()
        if letter not in letter_count_map and letter.isalpha():
            letter_count_map[letter] = 0
        elif letter.isalpha():
            letter_count_map[letter] += 1
    return letter_count_map

def print_report(book_path, chars_map):
    sorted_chars = sorted(chars_map.items(), key=lambda x:x[1], reverse=True)
    sorted_chars_map = dict(sorted_chars)

    for key, value in sorted_chars_map.items():
        print(f"The '{key}' character was found {value} times")

main()