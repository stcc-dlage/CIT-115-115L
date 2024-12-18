# Dave Lage
# CIT-115-D2
# Code Temperature Converter


def main():
    print("Welcome to Code Temperature Converter by Dave Lage")
    fTemp = float(input("What is the temperature? "))
    strScale = input(
        "Which temperature scale was used? ('F' or 'f' for Fahrenheit and 'C' or 'c' for Celsius) "
    ).upper()

    if strScale not in ["F", "C"]:
        print("Enter a F or C")
    else:
        if strScale == "F":
            if fTemp <= 212:
                fCelsius = (5.0 / 9) * (fTemp - 32)
                print(f"The Celsius equivalent is: {fCelsius:.1f}")
            else:
                print("Temp can not be > 212")
        else:
            if fTemp <= 100:
                fFahrenheit = ((9.0 / 5.0) * fTemp) + 32
                print(f"The Fahrenheit equivalent is: {fFahrenheit:.1f}")
            else:
                print("Temp can not be > 100")


if __name__ == "__main__":
    main()
