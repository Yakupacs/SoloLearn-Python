file = open("/usercode/files/books.txt", "r")

for line in file.readlines():
    
    title = line.split()
    a = ""
    for c in title:
        a += c[0]
    print (a)

file.close ()