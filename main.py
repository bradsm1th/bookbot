from stats import count_words, count_chars

def get_book_text(path):
    with open(path) as file_obj:
        text = file_obj.read()
    return text 
    
def main():
    text = get_book_text("books/frankenstein.txt")
    words = count_words(text)
    char_count = count_chars(text)

    print(f"Found {words} total words")
    print(char_count)

main()