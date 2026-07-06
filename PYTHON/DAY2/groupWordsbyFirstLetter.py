from collections import Counter
from collections import defaultdict

st = input()
# d = {}
# for word in st.split(' '):
#     d.setdefault(word[0],[]).append(word)

# print(d)

dt = defaultdict(list)

for word in st.split():
    dt[word[0]].append(word)

print(dict(dt))