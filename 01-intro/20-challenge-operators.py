def validate_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def get_two_values():
    first_value = input("Enter first value: ")
    second_value = input("Enter second value: ")
    return first_value, second_value

def return_biggest(num1, num2):
    if num1 != num2:
        if num1 > num2:
            return num1
        else:
            return num2
    else:
        return "Both have the same value"

def main():
    if __name__ == '__main__':
        first_value, second_value = get_two_values()
        if validate_num(first_value) and validate_num(second_value):
            biggest = return_biggest(int(first_value), int(second_value))
            print(f"Result: {biggest}")
        else:
            print("Incorrect input. You need to type two numbers")
            main()


main()
