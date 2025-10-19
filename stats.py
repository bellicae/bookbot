def get_num_words(text):
    words=text.split()
    word_count=len(words)
    return word_count
def count_characters(text):
    char_dic ={}
    for char in text:
        char=char.lower()
        if char in char_dic:
            char_dic[char]=char_dic[char]+1
        else:
            char_dic[char]=1
    return char_dic
def sort_on(text):
    return text["num"]
def split_dic(char_dic):
    letters = []
    for char in char_dic:
        count = char_dic[char]
        new_dics={"char":char, "num":count}
        letters.append(new_dics)
    return letters

def sort(char_dic):
    letters_to_sort = split_dic(char_dic)
    letters_to_sort.sort(reverse=True, key=sort_on)
    return letters_to_sort
                