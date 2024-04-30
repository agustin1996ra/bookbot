
def sort_on(dict):
    return dict["num"]

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    num_letters = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            if c not in num_letters:
                num_letters[c] = 0
            num_letters[c] += 1
    letters = []
    for k in num_letters:
        letters.append({"letter": k, "num": num_letters[k]})
    letters.sort(reverse=True, key=sort_on)
    return letters

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        words = count_words(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f'{words} words found in the document')
        print()
        letters = count_letters(file_contents)
        for letter in letters:
            print(f'The {letter["letter"]} character was found {letter["num"]} times')
        print("--- End report ---")


if __name__ == "__main__":
    main()