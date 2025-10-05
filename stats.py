def count_words(t_as_s):
    return len(t_as_s.split())

def count_chars(text_as_string):
    all_the_chars = {}
    for c in text_as_string:
        c = c.lower()
        if c not in all_the_chars:
            all_the_chars[c] = 1
        else:
            all_the_chars[c] += 1
    return all_the_chars

def sorter(dict):
    return(dict['num'])

def sorted_dicts(dict):
    all_sorted = []
    for k, v in dict.items():
        new_dict = {}
        new_dict["char"] = k
        new_dict["num"] = v
        all_sorted.append(new_dict)
    all_sorted.sort(reverse=True, key=sorter)
    return all_sorted
    # return all_sorted.sort(reverse=False, key=sorter)