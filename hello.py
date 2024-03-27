def main():
    # ask for name
    name = input("what's your name? ")
    # remove whitespace and capitalise
    # title can be used to detect the capitalise the name or any input inside it
    name = name.strip().capitalize().title()
    # print hello and name
    # print(" Hello,", name)
    # # using text formating  or f string
    # print(f"hello, {name}")

    hello(name)
    # print(name)


def hello(to="world"):
    print("hello!", to)


main()

# putting hello.py into a funciton
