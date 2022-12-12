def Heron():
    n1 = float(input("Enter a number: "))
    n2 = 1
    while True:
        n3 = n2
        n2 = (n2 + (n1 / n2)) / 2
        if n3 == n2:
            return n3


print(Heron())
