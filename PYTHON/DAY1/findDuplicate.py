st = input("Enter String: ")

freq= [0] * 126

for s in st:
    freq[ord(s)] += 1

for i in range(126):
    if freq[i]>1:
        print(chr(i))