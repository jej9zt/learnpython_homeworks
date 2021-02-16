def string_comparsion(string_1, string_2):
    if not isinstance(string_1, str) or not isinstance(string_2, str):
        return 0
    elif string_1 == string_2:
        return 1
    elif string_1 != string_2 and 'learn' in string_2:
        return 3
    elif string_1 != string_2 and len(string_1) > len(string_2):
        return 2


print(string_comparsion('abcdefg', 12345))
print(string_comparsion('abcdefg', 'abcdefg'))
print(string_comparsion('abcdefg', 'abcd913913123'))
print(string_comparsion('abcdefg', 'ablearnsd'))
