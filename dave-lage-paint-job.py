import math


def getFloatInput(prompt):
    while True:
        try:
            # Requesting the input from the user
            user_input = input(prompt)
            # Convert the input to float
            user_input = float(user_input)
            # Check if the input is positive and non-zero
            if user_input <= 0:
                print("Error: Please enter a positive, non-zero number.")
            else:
                return user_input
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return int(math.ceil(fSquareFeet / fFeetPerGallon))


def getLaborHours(fLaborHoursPerGallon, iGallonsRequired):
    return fLaborHoursPerGallon * iGallonsRequired


def getLaborCost(fLaborHoursPerGallon, fLaborChargePerHour, iGallonsRequired):
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iGallonsRequired)
    return fLaborHours * fLaborChargePerHour


def getPaintCost(iGallonsRequired, fPaintPrice):
    return iGallonsRequired * fPaintPrice


def getSalesTax(sState):
    tax_rates = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06,
    }
    return tax_rates.get(sState, 0.0)


def showCostEstimate(
    fGallonsOfPaint,
    fLaborHours,
    fPaintCost,
    fLaborCost,
    fSalesTax,
    fTotalCost,
    sLastName,
):
    # Formatting strings for the cost breakdown
    sGallonsOfPaint = f"Gallons of paint: {fGallonsOfPaint}"
    sLaborHours = f"Hours of labor: {fLaborHours:.2f}"
    sPaintCharges = f"Paint charges: ${fPaintCost:.2f}"
    sLaborCharges = f"Labor charges: ${fLaborCost:.2f}"
    sTax = f"Tax: ${fSalesTax:.2f}"
    sTotalCost = f"Total cost: ${fTotalCost:.2f}"

    # Print the breakdown
    print(sGallonsOfPaint)
    print(sLaborHours)
    print(sPaintCharges)
    print(sLaborCharges)
    print(sTax)
    print(sTotalCost)

    # Create the output file
    filename = f"{sLastName}_PaintJobOutput.txt"
    with open(filename, "w") as file:
        file.write(sGallonsOfPaint + "\n")
        file.write(sLaborHours + "\n")
        file.write(sPaintCharges + "\n")
        file.write(sLaborCharges + "\n")
        file.write(sTax + "\n")
        file.write(sTotalCost + "\n")

    print(f"\nThe cost estimate has been saved to {filename}.")


def main():
    # Get user input for the variables
    fSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHour = getFloatInput("Labor charge per hour: ")

    # Get the state of the job and customer last name
    sState = input(
        "Enter the state where the job will take place (e.g., CT, MA, ME, etc.): "
    )
    sLastName = input("Enter the customer's last name: ")

    # Perform calculations
    iGallonsRequired = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iGallonsRequired)
    fLaborCost = getLaborCost(
        fLaborHoursPerGallon, fLaborChargePerHour, iGallonsRequired
    )
    fPaintCost = getPaintCost(iGallonsRequired, fPaintPrice)
    fSalesTaxRate = getSalesTax(sState)
    fSalesTax = (fPaintCost + fLaborCost) * fSalesTaxRate
    fTotalCost = fPaintCost + fLaborCost + fSalesTax

    # Show the cost estimate and save it to a file
    showCostEstimate(
        iGallonsRequired,
        fLaborHours,
        fPaintCost,
        fLaborCost,
        fSalesTax,
        fTotalCost,
        sLastName,
    )


# Run the main function
if __name__ == "__main__":
    main()
