def main():
    path_of_book = 'books/frankenstein.txt'
    # get full text
    text = get_text_of_book(path_of_book)
    print(text)
    # count words
    total_words = count_words(text)
    print(f"There are roughly {total_words} words")
    # count letters
    chars = tot_up_letters(text) # a { } of lowercase letters
    for ch in chars:
        print(f"{ch}: {chars[ch]}")

def get_text_of_book(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents


def count_words(string):
    words = string.split()
    return len(words)


def tot_up_letters(book_text_string: str):
    counted_chars = {}
    # make all chars lowercase
    lowercase_text = book_text_string.lower()
    for ch in lowercase_text:
        if ch in counted_chars:
            counted_chars[ch] += 1
        else:
            counted_chars[ch] = 1


    return counted_chars

main()