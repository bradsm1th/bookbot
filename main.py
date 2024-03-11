def main():
    path_of_book = 'books/frankenstein.txt'
    # get full text
    text = get_text_of_book(path_of_book)
    # count words
    total_words = count_words(text)
    # count letters
    chars = tot_up_letters(text) # a { } of lowercase letters
    # test "one dict to list of dicts"
    list_of_letters = to_list_of_dicts(chars)
    # print the report
    print_report(total_words, list_of_letters, path_of_book)


# ============================
# all the helper functions 
# ============================
def get_text_of_book(path: str):
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
        if ch.isalpha():
            if ch in counted_chars:
                counted_chars[ch] += 1
            else:
                counted_chars[ch] = 1
    return counted_chars

def sort_it(dict):
    return dict['count']

def to_list_of_dicts(dict):
    letter_dicts = []
    for entry in dict:
        letter_dicts.append({
            'name': entry,
            'count': dict[entry]
        })

    # sort it
    letter_dicts.sort(key=sort_it, reverse=True)
    return letter_dicts


def print_report(word_count: int, list_of_chars_dicts: list, title: str):
    print()
    print(f"  Start  ".center(40, "*"))
    print()
    print(f"File:\t{title}")
    print(f"Words:\t{word_count}")
    print()

    for entry in list_of_chars_dicts:
        print(f"The '{entry["name"]}' character was found {entry["count"]} times ")
    
    print()
    print(f"  End  ".center(40, "*"))
    print()

    
main()