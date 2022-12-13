a = 'AAAA'
b = 'B'
c = 1.1

# NOTE:It will get the values in order, if you don't have a 'c={}' it won't appear
# It will also not return an error
format = 'a={} b={}'.format(a, b, c)
format2 = 'a={} b={} c={}'.format(a, b, c)
print(format)
print(format2)

# NOTE: you can also pass parameters inside {}
# IT's possible to format decimal
format3 = 'a={} b={} c={:.2f}'.format(a, b, c)
print(format3)

# NOTE:Theres also a huge advantage, you don't depend on order
# You can specify indexes
string = 'a={2} b={1} c={0}'
format4 = string.format(a, b, c)
print(format4)

# NOTE: You can also renomeate parameters
string = 'a={name1} b={name2} c={name3}'
format5 = string.format(
        name1=a, name2=b, name3=c
        )
# print(format5)
