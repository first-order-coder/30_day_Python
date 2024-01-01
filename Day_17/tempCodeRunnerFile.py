fruits = ['Banana', 'Mango', 'Avacado','Lemon']
veg = ['Tomato','Potato','Onion', 'Carrot']
fruits_and_veg = []
for f,v in zip(fruits, veg):
    fruits_and_veg.append({'fruit:': f, 'veg:': v })
print(fruits_and_veg)