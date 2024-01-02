from itertools import count


empty_tuple = ()
empty_tuple_1 = tuple()

print(empty_tuple)
print(empty_tuple_1)

sibilings = ('Shefy', 'kalu','Dora')
names = ('Ginura', 'Ranuli', 'Chanuli')
all = sibilings + names


print(all.count('Ginura'))
print(len(all))

list = list(all)
list.append('Inoka')
list.append('Buwaneka')
list.insert(3, 'Inoka')
tpl = tuple(list)

print(list)
print(tpl)