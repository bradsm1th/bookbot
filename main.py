def main():
    path_of_book = 'books/frankenstein.txt'
    # get full text
    text = get_text_of_book(path_of_book)
    print(text)
    # count words
    total_words = count_words(text)
    print(f"There are roughly {total_words} words")

def get_text_of_book(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents


def count_words(string):
    words = string.split()
    return len(words)

main()