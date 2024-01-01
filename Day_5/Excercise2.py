import secrets


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

print(max(ages))
print(min(ages))

max_age = max(ages)
min_age = min(ages)

ages.append(max_age)
ages.append(min_age)
new_ages = ages
print(ages)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.insert(3, max_age)
ages.insert(5, min_age)
print(ages)

print(ages.index(19))

new_ages.sort()
middle_age1 = new_ages[5]
middle_age2 = new_ages[6]
median_age = (middle_age1 + middle_age2) / 2
print('Median Age:', median_age)

sum = sum(new_ages)
print(sum)

average = sum / 12
print('Average:', average)

range = max_age - min_age
print(range)

countries = ['China', 'Russia', 'Canada', 'Finland', 'Ireland']
first_country, second_country, third_country, *rest = countries
print(first_country)
print(second_country)
print(rest)