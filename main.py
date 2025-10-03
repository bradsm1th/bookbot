def get_book_text(path):
    with open(path) as file_obj:
        text = file_obj.read()
    return text 

def count_words(t_as_s):
    return len(t_as_s.split())

def main():
    print(f"Found {count_words(get_book_text("books/frankenstein.txt"))} total words")
    
main()
