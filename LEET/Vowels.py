def reverseVowels(s):
      s = s.lower()
      lst_1 = list(s)
      #print(lst_1)

      vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
      
      lst = []
      for inde_i, i in enumerate(lst_1):
            if i in vowels:
                  lst.append(inde_i)
      print(lst)
      
      revers = list(reversed(lst))
      #print(revers)

      for j, k in zip(lst,revers):
            lst_1[j] = s[k]
            
      reversed_string = ''.join(lst_1)
      print(reversed_string)

reverseVowels('Hello')

# a = ['a', 'b', 'c', 'd']
# b = ['e', 'f', 'g', 'h']

# for i,j in zip(a,b):
#     a[1] = b[1]
# print(a, b)