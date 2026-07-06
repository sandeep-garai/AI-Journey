from collections import defaultdict
st = input()

# dt = {}

# for word in st.split():
#     if word not in dt:
#         dt[word]=0
#     dt[word]+=1
# print(dt)

dt = defaultdict(int)

for word in st.split():
    dt[word]+=1;

sorted_list = sorted(dt.items(),key = lambda item: item[1],reverse=True)

for li in range(5):
    print(sorted_list[li])