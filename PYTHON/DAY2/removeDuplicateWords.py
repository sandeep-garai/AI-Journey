st = input()

# dt = {}
# result =""

# for word in st.split():
#     if word not in dt:
#         result+= word +" "
#         dt[word] = 1

seen = set()
result = []

for word in st.split():
    if word not in seen:
        result.append(word)
        seen.add(word)

print(" ".join(result))
# for word in st.split():
#     if dt.get(word,0)==0:
#         result+=word+' '
#     dt.setdefault(word,1)
#     # dt[word]=dt.get(word,0)+1

print(result)