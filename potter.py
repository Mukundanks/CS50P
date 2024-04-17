# program to check who belongs to the houses in the comic Harry Potter

name = input("what's your name? ")


# match is similar to the switch case, which will help to eliminate multiple if-elif-else blocks

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("slytherin")
    case _:
        print(f"{name} Who??")
