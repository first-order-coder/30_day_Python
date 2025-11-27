empty_tuple = ()
empty_tuple_1 = tuple()

print(empty_tuple)
print(empty_tuple_1)

sibilings = ('Brian', 'Peter','Stewie')
names = ('John', 'Meg', 'Cleavelend')
all_names = sibilings + names


print(all_names.count('Brian')) #number of times an item appears in a list
print(len(all_names))

new_lst: list[str] = list(all_names) #added an annotation to say that this new_lst is a list contatining str items
print(type(new_lst))
new_lst.append('Tray')
new_lst.append('Nate')
new_lst.insert(3, 'Nashua')
tpl = tuple(new_lst)

print(new_lst)
print(tpl)