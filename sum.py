def main():
    num = int(input("enter an integer: "))
    print(f"the sum is: {sum(num)}")


def sum(n):
    return (n * (n + 1)) * 0.5


if __name__ == "__main__":
    main()
