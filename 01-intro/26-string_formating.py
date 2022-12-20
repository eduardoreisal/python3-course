"""
Formating Strings
s   -   string 
d   -   int
f   -   float

.<number of caracters>f 
x or X - Hexadecimal
(Character)(><^)(quantity)
>   -   right
<   -   left
^   -   Center
Sinal   - + or -
E.g: 0>-100,.1f
conversion flags - !r !s !a

"""

variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}')   # Fills wih ' ' (spaces) 10 times to the left
print(f'{variable: <10}*')   # Fills wih ' ' (spaces) 10 times to the right
print(f'{variable: ^10}')   # Fills with ' ' (spaces) at the center
print(f'{1000.45687464845345:,.1f}')  # Rounds to 1 character after .
