import sys
from stats import get_num_words
from stats import count_characters
from stats import sort_on
from stats import split_dic
from stats import sort
def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text=get_book_text(book_path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books...")
    print("----------- Word Count ----------")
    print (f"Found {get_num_words(text)} total words")
    char_counts=count_characters(text)
    sorted_char_list = sort(char_counts)
    print("--------- Character Count -------")
    for entry in char_counts:
        if entry.isalpha():
            print(f"{entry}: {char_counts[entry]}")
    print (sorted_char_list)
    print ("============= END ===============")


main()
