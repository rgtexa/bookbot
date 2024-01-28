import sys

def main() -> int:
    book = "books/frankenstein.txt"
    file_contents = get_book_text(book)
    freq = char_frequency(file_contents)
    words = count_words(file_contents)
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in document.")
    char_freq = sorted(list(freq.items()))
    for char, count in char_freq:
        if char.isalpha():
            print(f"The {char} character was found {count} times")
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def char_frequency(text):
    freq = {}
    for char in text:
        if char.lower() in freq:
            freq[char.lower()] += 1
        else:
            freq[char.lower()] = 1
    return freq

if __name__ == '__main__':
    sys.exit(main())