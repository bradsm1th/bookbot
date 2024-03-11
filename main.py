def main():
    path_of_book = 'books/frankenstein.txt'
    text = get_text_of_book(path_of_book)
    print(text)


def get_text_of_book(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents




main()