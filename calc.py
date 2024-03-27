def main():
    x = int(input("enter first number: "))
    y = int(input("enter second number: "))

    # print(f"the sum is: {x + y:,} ")  # the , will seperate every 3 digits

    print("the sum of the two numbers is: ", add(x, y))
    print("the difference of numbers is :", sub(x, y))
    print("the product is: ", mul(x, y))
    print(f"the divison of two numbers is :{ div(x, y): .2f}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


main()
