# print('Bennett University')
# list1 = [5, 6.7, 'bennett', 2016]
# print(list1[0: 3])

# a = 5
# y = ~5
# print(y)

# x = True
# y = not x
# print(y)

# def increment(t):
#    return t + 1

# x = 5
# print(x)

str1 = 'bennett'
vowels = 'aeiouAEIOU'
vow_count = 0
vow_list = []

for char in str1:
    if char in vowels:
        vow_count = vow_count + 1
        vow_list.append(char)

print(vow_list, f'no of consonants: {len(str1) - len(vow_list)}')
