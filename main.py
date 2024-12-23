def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_words(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lowered_text = text.lower()
    letter_count_map = {}
    letters = lowered_text.split("")
    for letter in letters:
        if letter not in map:
            letter_count_map[letter] = 0
        else:
            letter_count_map[letter] += 1
        return letter_count_map
main()