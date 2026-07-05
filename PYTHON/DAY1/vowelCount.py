st = input("Enter string: ")
a = e = i = o = u = 0
for i in range(len(st)):
    if st[i].lower=='a':
        a+=1
    elif st[i].lower=='e':
        e+=1
    elif st[i].lower=='i':
        i+=1
    elif st[i].lower=='o':
        o+=1
    elif st[i].lower=='u':
        u+=1

print(a,e,i,o,u)