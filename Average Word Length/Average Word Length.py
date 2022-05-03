text = input()

kelimeSayaci = 1

k = 0
for i in text:
	if text[k] == " ":
		kelimeSayaci = kelimeSayaci + 1
	k = k + 1
	
harfSayisi = len(text) - kelimeSayaci + 1

print(harfSayisi/kelimeSayaci)