

print("--Welcome to the Movie Ticket--")
print("Do you wanna buy a ticket? (Yes or No)")

while True:
    _customer = input("Customer: ").strip().lower()
    
    if _customer not in ["yes", "no"]:
        print("Please answer with 'Yes' or 'No'.")
        continue

    if _customer == "yes":
        print("\nGreat, How old are you?")
        _customer_age = int(input("Customer: "))

        if not isinstance (_customer_age, int) :
            print("Please enter a valid age.")
            continue
        
        if _customer_age < 18 or _customer_age > 60:
            print("\nYou are eligible for a 20% discount")
            print(f"And you final ticket price is ₱{250 * .20:.2f}")
            break
        else:
            print("\nYou are not eligible for a discount.")
            print(f"Your final ticket price is ₱{250:.2f}")
            break
    else:
        print("\nThank you for visiting!")
        break

