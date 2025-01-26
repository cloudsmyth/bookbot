def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        char_freq = char_occurance(file_contents)
        print(f"----- Begin Report of {book} -----")
        print(f"{len(words)} words were found in this book")
        print_char_freq(char_freq)
        print("----- End Report -----")


def print_char_freq(dict):
    list = [{"char": key, "freq": value} for key, value in dict.items()]
    list.sort(reverse=True, key=sort_dict)
    for pair in list:
        char = pair["char"]
        freq = pair["freq"]
        if char.isalpha():
            print(f"The '{char}' character was found {freq} times")


def sort_dict(dict):
    return dict["freq"]


def char_occurance(string):
    freq = {}
    lower_string = string.lower()
    for char in lower_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


main()
