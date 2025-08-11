

print("--Welcome to the Taxi Fare Estimator--")
print("How many kilometers will you travel?")
_customer_kilometers = int(input("Customer: "))
print(f"That would be a total of ₱{40 + (_customer_kilometers * 15)} for {_customer_kilometers} kilometers.")