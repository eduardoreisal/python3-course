print("Hello from 02-print.py!", "Everything here will be printed", 1234)
print("#"*20)

# If you don't give any argument to sep, python will print it without spaces
print(12, 34, sep='')
print(56, 78, sep="")

print("#"*20)
# Now python will print 12-34
print(12, 34, sep='-')

print("#"*20)
# Python adds a \n by default, but you can ovewrite it using end
print("First print ", end='')
print("Second print", end='\n')
