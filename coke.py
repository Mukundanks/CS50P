
current = 0

def main():
    global current
    print("Amount due: 50")
    while current <= 50:
        cash = int(input("Insert coin:"))
        deno = [25, 10, 5, 50]
        if cash in deno:
            current += cash
            change(cash)
            if current >= 50:
                break
        else:
            due = 50 - current
            print(f"Amount Due: {abs(due)}")

def change(coin):
    global current
    due = 50 -current
    print(f"Amount Due: {abs(due)}")
    while current >= 50:
        if current ==50:
            print("Change Owed: 0")
            break
        else:
            print(f"change owed: {current -50}")
            break

    return current

if __name__ == "__main__":
    main()






