def energy(x):
    return x * pow(300000000,2)
def main():
    mass = int(input("enter the mass you want to calculate: "))
    print(energy(mass))

if __name__ == "__main__":
    main()
