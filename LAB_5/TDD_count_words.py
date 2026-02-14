# Function that counts the words in a sentence

def count_words(sentence):
    if not sentence:
        return 0
    elif len(sentence) == 1:
        return 1
    else:
        # .split() with no arguments splits by any whitespace
        # and discards empty strings from the resulting list.
        words = sentence.split()
        return len(words)