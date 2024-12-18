# Dave Lage
# CIT-115-D2

MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066


def main():
    name = input("What is your name: ")
    earth_weight = input("What is your weight: ")

    print(f"{name.strip()} here are your weights on our Solar System's planets:")

    # Convert weight to a float
    earth_weight = float(earth_weight)

    print("Weight on %-20s %6.2f" % ("Mercury:", MERCURY * earth_weight))
    print("Weight on %-20s %6.2f" % ("Venus:", VENUS * earth_weight))
    print("Weight on %-20s %6.2f" % ("Moon:", MOON * earth_weight))
    print("Weight on %-20s %6.2f" % ("Mars:", MARS * earth_weight))
    print("Weight on %-20s %6.2f" % ("Jupiter:", JUPITER * earth_weight))
    print("Weight on %-20s %6.2f" % ("Saturn:", SATURN * earth_weight))
    print("Weight on %-20s %6.2f" % ("Uranus:", URANUS * earth_weight))
    print("Weight on %-20s %6.2f" % ("Neptune:", NEPTUNE * earth_weight))
    print("Weight on %-20s %6.2f" % ("Pluto:", PLUTO * earth_weight))


if __name__ == "__main__":
    main()
