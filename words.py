def print_upper_words(words):
    """"Print each word on seperpate line, uppercased."""

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_word2(words, start_letter):
    for word in words:
        for letter in start_letter:
            if word.startswith(letter):
                return(word.upper())


