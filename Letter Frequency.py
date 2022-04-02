#your code goes here
text = input()
letter = input()

i = 0
for letter in text:
    if text[0] == letter:
        i = i + 1

c = len(text)
sonuc = (i / c) * 100
print(int(sonuc))