def get_num_words(t):
    num_words = len(t.split())
    return num_words


char_count = {}


def get_num_char(t):
    cleaned_t = t.lower()
    for char in cleaned_t:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def num(char_dictionary):
    return char_dictionary["num"]


def get_sorted_list(dictionary):
    char_list = []
    for key in dictionary:
        char_dictionary = {}
        char_dictionary["char"] = key
        char_dictionary["num"] = dictionary[key]

        char_list.append(char_dictionary)
    char_list.sort(reverse=True, key=num)
    return char_list
