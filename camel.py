def main():
    word = input("Input your camel cased word: ")
    print(f"The snake cased word for {word} is {snake(word)}")

def snake(w):
    if w == w.lower():
        return w
    elif w[0] == w[0].upper() and w[1:].lower():
        return w.lower()
    else:
        words = split(w)
        words =  ''.join(words)
        words = words.lower()
        for letters in words:
            s = words.replace(' ', '_')
        return s

def split(s):
    new = []
    for letter in s:
        if letter.islower():
            new.append(letter)
        elif letter.isupper():
            new.append(' ')
            new.append(letter)
    return new


if __name__ == "__main__":
    main()


