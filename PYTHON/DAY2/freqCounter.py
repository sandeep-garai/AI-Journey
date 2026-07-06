from collections import defaultdict
from collections import Counter
st = input("Enter string: ")


# dt = {}

# for s in st:
#     if s not in dt.keys():
#         dt[s]=0
#     dt[s] += 1
# print(dt)

c = Counter(st)
for key, value in c.items():
    print(key, value)

# can also use 
# for s in st:
#     dt[s]=dt.get(s,0)+1 //where the .get() will return the occurances and will give 0 if not present instead of an error.