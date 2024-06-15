def convert(x):
    return x.replace(":)", "🙂").replace(":(", "🙁")

def main():
    str = input("Say something with either of emoticons ':)' or ':(': \n")
    print(convert(str))

if __name__ == "__main__":
    main()
