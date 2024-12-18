# Dave Lage
# CIT-115-D2


def main():
    principal_investment = input("Enter the starting principal: ")
    PV = float(principal_investment)

    annual_interest_rate = input("Enter the annual interest rate: ")
    R = float(annual_interest_rate)

    num_of_periods = input("How many times per year is the interest compounded? ")
    m = float(num_of_periods)

    years_interest = input("For how many years will the account earn interest? ")
    t = int(years_interest)

    # Convert the interest rate from percentage to decimal
    r = R / 100

    FV = PV * (1 + r / m) ** (m * t)

    print(f"At the end of 2 years you will have $ {FV:.2f}")


if __name__ == "__main__":
    main()
