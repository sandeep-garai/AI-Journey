st = input("Enter string: ")
a = e = ic = o = u = 0
for i in range(len(st)):
    if st[i].lower()=='a':
        a+=1
    elif st[i].lower()=='e':
        e+=1
    elif st[i].lower()=='i':
        ic+=1
    elif st[i].lower()=='o':
        o+=1
    elif st[i].lower()=='u':
        u+=1
#using .lower() for the method properties
#using .lower without brackets will show the method defination but will not work
print(a,e,ic,o,u)