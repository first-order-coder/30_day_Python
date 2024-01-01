for _ in range(0,num_id + 1):
    method1 = ''.join(random.choices(string.ascii_letters + string.hexdigits, k= char_len1))
    method2 = ''.join(random.choices(string.ascii_letters + string.hexdigits, k= char_len2))
    method = method1 + ' ' + method2
    print(method)