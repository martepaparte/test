import firstclass


def print_test():
    # Use a breakpoint in the code line below to debug your script.
    mystery = 734_529.699
    print(mystery)  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_test()
    object_one = firstclass.FirstClass()
    y = list(object_one.mytuple)
    y[1] = "kiwi"
    object_one.mytuple = tuple(y)
    print(object_one.mytuple[1])
