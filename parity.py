# program to check whether a number is odd or even


def is_even(number):
    # this is the normal way of doing
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False

    # it can be done in this way as well, less lines of code

    return number % 2 == 0


def main():
    x = int(input("What is the number? "))
    if is_even(x):
        print("the number is even")
    else:
        print("the number is odd")


if __name__ == "__main__":
    main()
