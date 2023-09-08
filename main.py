import firstclass


def print_test():
    input_number = input("Please input two digit number: ")
    try:
        input_number = int(input_number)
    except Exception as e:
        print("Failed to input number: " + e)
    try:
        if len(str(input_number)) != 2:
            raise ValueError("not two digits")
    except ValueError as e:
        print("Invalid input: " + str(e))
        return

if __name__ == '__main__':
    print_test()
