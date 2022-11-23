# You can convert one type to another

my_string = "10"
print(type(my_string))  # Type str
print(type(int(my_string)))  # Type int

# Poliformfism, using the same operator to do different things
print(1 + 1)  # 2
print('a' + 'b')  # ab

# You can't use + to add 2 elements of diferent type. You need to use coercion
# and make sure they are the same type


print(bool(0))  # False
print(bool(''))  # False
print(bool(' '))  # True
print(bool('1'))  # True
print(bool('a'))  # True
