# Dave Lage
# Compound Interest with Loops


def main():
    # Assemble questions an data type
    aQuestions = [
        ("What is the Original Deposit? ", float),
        ("What is the Interest Rate? ", float),
        ("What is the Number of Months? ", int),
        ("What is the Goal Amount? (0 for no goal) ", float),
    ]

    aAnswers = []

    # Each question and conversion
    for i, (sQuestion, conv) in enumerate(aQuestions):
        while i >= len(aAnswers):
            sAnswer = input(sQuestion)

            try:
                # Type conversion
                fValue = conv(sAnswer)

                # Check goal value is 0 or higher
                if i == 3:
                    if fValue < 0.0:
                        print("Input must be 0 or greater")
                        continue

                # Check if value is less than or equal to 0
                elif fValue <= 0.0:
                    print("Input must be a positive numeric value")
                    continue

                aAnswers.append(fValue)
            except ValueError:
                print("Input must be a positive numeric value")
                continue

    fDeposit, fInterestRatePercentage, iNumOfMonths, fGoal = aAnswers

    # Convert percentage into decimal
    fInterestRatePercentage /= 100.0

    # Calculate monthly interest rate
    fMonthlyInterestRate = fInterestRatePercentage / 12

    # Initialize the account balance to the deposit
    fAccountBalance = fDeposit

    # Calculate the accumulated account balance each month
    for iMonth in range(1, iNumOfMonths + 1):
        # Calculate month interest
        fMonthInterest = fAccountBalance * fMonthlyInterestRate

        # Accumulate monthly interest
        fAccountBalance += fMonthInterest

        print(
            f"Month: {iMonth:{len(str(iNumOfMonths))}} Account Balance is: ${fAccountBalance:,.2f}"
        )

    # Initialize account balance to original deposit
    fProjectedAccountBalance = fDeposit

    # Increment value for month
    iMonth = 0

    # Check if we are calculating a goal
    if fGoal > 0.0:
        # Loop until projected account balance greater than or equal to goal
        while fProjectedAccountBalance < fGoal:
            iMonth += 1

            # Calculate monthly interest
            fMonthInterest = fProjectedAccountBalance * fMonthlyInterestRate

            # Accumulate monthly interest
            fProjectedAccountBalance += fMonthInterest

        print(f"It will take: {iMonth:,} months to reach the goal of ${fGoal:,.2f}")


if __name__ == "__main__":
    main()
