def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))  # Prompt user for input and convert to float
            if value <= 0:
                print("Error: Value must be greater than 0. Please enter again.")
            else:
                return value  # Return valid non-zero float
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def getMedian(sales_list):
    sales_list.sort()  # Sort the list in ascending order
    n = len(sales_list)
    if n % 2 == 1:
        # If odd number of elements, return the middle one
        return sales_list[n // 2]
    else:
        # If even number of elements, return the average of the two middle elements
        mid_index = n // 2
        return (sales_list[mid_index - 1] + sales_list[mid_index]) / 2


def main():
    sales = []

    while True:
        # Call getFloatInput to get a valid sales price
        fSalesPrice = getFloatInput("Enter property sales value: ")

        # Add the sales value to the list
        sales.append(fSalesPrice)

        # Ask if the user wants to enter another value
        while True:
            another = input("Enter another value Y or N: ").strip().lower()
            if another in ["y", "n"]:
                break
            print("Invalid input. Please enter Y or N.")

        if another == "n":
            break

    # Sort the list in ascending order
    sales.sort()

    # Calculate the length of the property value for formatting
    property_str_width = 10
    properties_width = len(str(len(sales))) + property_str_width
    max_sale_width = max([len(f"{sale:,.2f}") for sale in sales])

    # Output the sorted list of sales
    for i, sale in enumerate(sales):
        print(f"{f'Property {i+1}':<{properties_width}} ${sale:>{max_sale_width},.2f}")

    # Calculate and display the Min, Max, Total, Average, Median, and Commission
    min_value = min(sales)
    max_value = max(sales)
    total_value = sum(sales)
    average_value = total_value / len(sales)
    median_value = getMedian(sales)
    commission_value = total_value * 0.03  # Commission is 3% of the total sales

    # Setting the same width for all the labels
    label_width = 12  # To align the labels
    value_width = len(f"{total_value:,.2f}")  # The str length of the largest number

    # Print with proper alignment
    print(f"{'Minimum:':<{label_width}}${min_value:>{value_width},.2f}")
    print(f"{'Maximum:':<{label_width}}${max_value:>{value_width},.2f}")
    print(f"{'Total:':<{label_width}}${total_value:>{value_width},.2f}")
    print(f"{'Average:':<{label_width}}${average_value:>{value_width},.2f}")
    print(f"{'Median:':<{label_width}}${median_value:>{value_width},.2f}")
    print(f"{'Commission:':<{label_width}}${commission_value:>{value_width},.2f}")


if __name__ == "__main__":
    main()
