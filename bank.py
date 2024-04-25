greet = input("Enter the greeting you received: ").lower().strip()

match greet:
    case x if greet.startswith("hello"):
        print("$0")
    case x if greet.startswith("h"):
        print("$20")
    case _:
        print("$100")

