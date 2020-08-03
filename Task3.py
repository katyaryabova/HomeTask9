side = int(input("Enter side: "))


def square(data):
    return "Perimeter: " + str(4 * data), "Square: " + str(data ** 2), "Diagonal: " + str(data * 2 ** (1 / 2))


print(square(side))
