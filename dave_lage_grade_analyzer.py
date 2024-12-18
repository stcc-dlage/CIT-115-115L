# Dave Lage
# CIT-115-D2
# Grade Analyzer


def main():
    strName = input("Name of person we are calculating the grades for: ")

    # Capture 4 test scores
    lstScores = [int(input(f"Test score {i+1}: ")) for i in range(4)]

    # Filter out invalid values
    lstScores = [iScore for iScore in lstScores if iScore >= 0]

    # Test we have enough scores
    if len(lstScores) != 4:
        exit("Test scores must be greater than 0.")

    strDropLowest = input("Drop Lowest? (Y/N) ").strip().upper()

    if strDropLowest not in ["Y", "N"]:
        print("Enter Y or N to Drop the Lowest Grade.")
        exit(2)

    if strDropLowest == "Y":
        # Test 1
        if (
            lstScores[0] <= lstScores[1]
            and lstScores[0] <= lstScores[2]
            and lstScores[0] <= lstScores[3]
        ):
            fAverage = (lstScores[1] + lstScores[2] + lstScores[3]) / 3.0

        # Test 2
        elif (
            lstScores[1] <= lstScores[0]
            and lstScores[1] <= lstScores[2]
            and lstScores[1] <= lstScores[3]
        ):
            fAverage = (lstScores[0] + lstScores[2] + lstScores[3]) / 3.0

        # Test 3
        elif (
            lstScores[2] <= lstScores[0]
            and lstScores[2] <= lstScores[1]
            and lstScores[2] <= lstScores[3]
        ):
            fAverage = (lstScores[0] + lstScores[1] + lstScores[3]) / 3.0

        # Test 4
        else:
            fAverage = (lstScores[0] + lstScores[1] + lstScores[2]) / 3.0
    else:
        fAverage = (lstScores[0] + lstScores[1] + lstScores[2] + lstScores[3]) / 4

    if type(fAverage) is not float:
        print("Absolute failure")
        exit(4)

    if fAverage >= 97.0:
        strLetterGrade = "A+"
    elif 94.0 <= fAverage < 97.0:
        strLetterGrade = "A"
    elif 90.0 <= fAverage < 94.0:
        strLetterGrade = "A-"
    elif 87.0 <= fAverage < 90.0:
        strLetterGrade = "B+"
    elif 84.0 <= fAverage < 87.0:
        strLetterGrade = "B"
    elif 80.0 <= fAverage < 84.0:
        strLetterGrade = "B-"
    elif 77.0 <= fAverage < 80.0:
        strLetterGrade = "C+"
    elif 74.0 <= fAverage < 77.0:
        strLetterGrade = "C"
    elif 70.0 <= fAverage < 74.0:
        strLetterGrade = "C-"
    elif 67.0 <= fAverage < 70.0:
        strLetterGrade = "D+"
    elif 64.0 <= fAverage < 67.0:
        strLetterGrade = "D"
    elif 60.0 <= fAverage < 64.0:
        strLetterGrade = "D-"
    else:
        strLetterGrade = "F"

    print(f"{strName} test average is: {fAverage:.1f}")
    print(f"Letter Grade: {strLetterGrade}")


if __name__ == "__main__":
    main()
