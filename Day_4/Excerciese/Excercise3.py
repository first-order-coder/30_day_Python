course = 'Coding For All People'

word = 'C'
print(course.index(word))

print(course.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.index('because'))
print(sentence.rfind('because'))

slice = sentence[31:54]
print(reversed(slice))
slice1 = sentence[0:31]
slice2 = sentence[55:72]
print(slice1 + slice2)