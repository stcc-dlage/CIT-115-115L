# Dave Lage
# Compound Interest with Loops


def main():
    questions = [
        ("What is the Original Deposit? ", float),
        ("What is the Interest Rate? ", float),
        ("What is the Number of Months? ", int),
        ("What is the Goal Amount? (0 for no goal) ", float),
    ]

    answers = []

    for i, (question, conv) in enumerate(questions):
        while True:
            answer = input(question)

            # Type conversion
            try:
                value = conv(answer)

                # Check goal value is 0 or higher
                if i == 3:
                    if value < 0.0:
                        print("Input must be 0 or greater")
                        continue

                # Check if value is less than or equal to 0
                elif value <= 0.0:
                    print("Input must be a positive numeric value")
                    continue

                answers.append(value)
            except ValueError:
                print("Input must be a positive numeric value")
                continue

            break

    deposit = answers[0]
    interest_rate_percentage = answers[1]
    num_of_months = answers[2]
    goal = answers[3]

    interest_rate_percentage /= 100.0

    monthly_interest_rate = interest_rate_percentage / 12

    account_balance = deposit

    for month in range(1, num_of_months + 1):
        month_interest = account_balance * monthly_interest_rate

        account_balance += month_interest

        print(f"Month: {month} Account Balance is: ${account_balance:,.2f}")

    projected_account_balance = deposit
    months = 0
    while projected_account_balance < goal:
        months += 1
        month_interest = projected_account_balance * monthly_interest_rate
        projected_account_balance += month_interest

    print(f"It will take: {months:,} months to reach the goal of ${goal:,.2f}")


if __name__ == "__main__":
    main()
