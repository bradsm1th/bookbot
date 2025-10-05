from stats import count_words, count_chars, sorted_dicts
import sys

def get_book_text(path):
    with open(path) as file_obj:
        text = file_obj.read()
    return text 
    
def print_report(title, path, words, counts_list):
    print("")
    print(F"============ {title} ============ ")
    print(f"Analying book found at {path}…")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for each in counts_list:
        print(f"{each['char']}: {each['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    words = count_words(text)
    char_count = count_chars(text)
    list_of_counts = sorted_dicts(char_count)

    print_report("BOOKBOT",sys.argv[1], words, list_of_counts)
    
main()