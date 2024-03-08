def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_letter_count(book_path)
    print(f"--- Begin the report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for i in range (0, len(characters)):
        print (f"The '{characters[i]["name"]}' character was found {characters[i]["num"]} times")
    print ("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_letter_count (path):
    letters = {}
    book = get_book_text (path)
    lowered_book = book.lower()
    for character in lowered_book:
        if character.isalpha() == True:
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
    letter_loops = []
    for letter, count in letters.items():
        letter_dict = {"name": letter, "num": count}
        letter_loops.append(letter_dict)
    def sort_on(dict):
        return dict["num"]
    letter_loops.sort(reverse = True, key = sort_on)

    return letter_loops

main()