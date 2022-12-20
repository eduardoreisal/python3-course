# in -> between
# not in -> not between
# python strings are iterable. You can navigate element by element

name = 'Eduardo'
print(name[0])
print(name[-1])

if 'u' in name:
    print('Letter found')

if 'z' in name:
    print('Letter found')
else:
    print(f'I was not able to find an z inside {name}')
