import re
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
regex = re.sub('[% , @, #, &, ;, $]', ' ', sentence)
s = regex
new = s.strip()
print(new)

# txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# regex_pattern = r'\d+'
# match = re.findall(regex_pattern, txt)
# print(match)