# If any value evaluates to Ture, the whole expression will be evaluated to
# that value

option = input("Enter (E) to enter or (l) to leave:  ")
password = input("Enter password: ")

allowed_password = '123456'

if option == 'E' or option == 'e' and password == allowed_password:
    print("Welcome!")
else:
    print("Wrong option or password")
