import sys
from stats import get_num_words
from stats import get_num_char
from stats import get_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main(book_path):
    text = get_book_text(book_path)
    num_word = get_num_words(text)
    num_char = get_num_char(text)
    dict_list = get_sorted_list(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")

    for dictionary in dict_list:
        key_value = dictionary["char"]
        char_count = dictionary["num"]
        if key_value.isalpha():
            print(f"{key_value}: {char_count}")

    print("============= END ===============")


main(book_path)
