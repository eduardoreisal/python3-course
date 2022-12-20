"""
Ask the user name and age.
If he enter name ande age:
    Show:
        Your name is {name}.
        Your reversed name is {reversed name}.
        Your name contains (or not) spaces.
        Your name has {n} letters.
        The first letter of your name is {letter}.
        The last letter of your name is {letter}.
Else:
    Shows "Sorry, there are empty fields."
"""

def get_name_and_age():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

def is_empty(var):
    if not bool(var):
        return True
    else:
        return False

def is_string(variable):
    if isinstance(variable, str) and not is_empty(variable):
        return True
    else:
        return False

def is_int(variable):
    try:
        int(variable)
        return True
    except ValueError:
        return False

def check_spaces(name):
    if " " in name:
        return "has"
    else:
        return "doesn't have"

def count_letters(string):
    count = 0
    for letter in string:
        if letter.isalpha():
            count += 1
    return count


def print_user_info(name, age):
    print(f"Your name is {name} and you are {age} years old.")
    print(f"Your reversed name is {name[::-1]}.")
    print(f"Your name {check_spaces(name)} spaces.")
    print(f"Your name has {count_letters(name)} letters.")
    print(f"The first letter of your name is {name[0]}.")
    print(f"The last letter of your name is {name[-1]}.")


def main():
    if __name__ == '__main__':
        name, age = get_name_and_age()
        if is_int(age) and is_string(name):
            print_user_info(name,age)
        else:
            print("Wrong input. Try again")
            main()

main()
