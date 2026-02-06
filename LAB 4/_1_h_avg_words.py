def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

print(average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"]))
