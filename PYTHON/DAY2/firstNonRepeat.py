st = input("Enter string: ")
# size = len(st)
# for i in range(size):
#     flag = 0;
#     for j in range(size):
#         if st[i]==st[j] and i!=j:
#             flag = 1
#             break
#     if flag == 0:
#         print(st[i])

# freq = {}
# for s in st:
#     freq[s]= freq.get(s,0)+1

# for s in st:
#     if freq[s]==1:
#         print(s)
#         break

from collections import Counter

c = Counter(st)
for s in st:
    if c[s]==1:
        print(s)
        break