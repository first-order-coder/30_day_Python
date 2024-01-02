# course = 'Python For All'
# print(course.split())

# abbreviataion = course.strip('hon For All')
# print('abbreviataion:', abbreviataion)

# input = str(input('Enter a Phrase:'))
# phrase = (input.replace('of', '')).split()
# acronym = ''
# for word in phrase:
#     acronym = str(word[0]).upper()
#     print('Acronym of input is', acronym)

data = int(input('Enter Data amount in MB:'))
Gigabytes, megabytes = divmod(data, 1024)
print(f'{Gigabytes}GB and {megabytes}MB')