
_penalty_per_day = 5
_number_of_days_late = 1
_total_fee = None

while True:
    print("\n--Welcome to the Library--")
    print(f"{'Tomorrow' if _number_of_days_late == 1 else 'Today'} is the deadline for returning the book.")
    print("Do you want to return the book now? (Yes/No)")
    _user_input = input("Borrower: ").strip().lower()

    if _user_input not in ["yes", "no"]:
        print("Invalid input. Please enter 'Yes' or 'No'.")
        continue

    if _user_input == "yes":
        if _number_of_days_late > 1:
            print(f"\nYou returned the book {_number_of_days_late-1} day(s) late.")
            print(f"Your total fee is ₱{_total_fee:.2f}")
            break
        else:
            print("Thank you for returning the book on time!")
            break
    else:
        print("You chose not to return the book!")
        _total_fee = _penalty_per_day * _number_of_days_late
        _number_of_days_late +=1
        continue



