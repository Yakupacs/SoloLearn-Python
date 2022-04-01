def search(text, word):
    text = text.split(" ")
    for i in text:
        if (i == word):
            return "Word found"
    else:
        return "Word not found"

text = input()
word = input()

print(search(text, word))