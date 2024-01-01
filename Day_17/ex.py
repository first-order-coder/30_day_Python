fruits = ['Banana', 'Mango', 'Avacado','Lemon']
veg = ['Tomato','Potato','Onion', 'Carrot']
fruits_and_veg = []
for f,v in zip(fruits, veg):
    fruits_and_veg.append({'fruit:': f, 'veg:': v })
print(type(fruits_and_veg))

# names = ['gh', 'sad', 'asda', 'asa', 'vaa']
# wok = ['sa', 'qw', 'cz', 'asc', 'qdqd']

# names_and_wok = []
# for n,w in zip(names, wok):
#     names_and_wok.append({'Name':n, 'Wok':w})
# print(names_and_wok)

# #getting the index and character as tyuple using enumerate
# for ele in enumerate(names):
#     print(ele)

# # #changing the index using enumerate
# # for ele, inde in enumerate(names, 1000):
# #     print(ele, inde)

# #getting the desired index or item using enumerate
# for ele, inde in enumerate(wok):
#     print(ele)
#     print(inde)