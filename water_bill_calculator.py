

def calculate_water_bill(_customer_cubic_meters):
    if _customer_cubic_meters >= 1 and _customer_cubic_meters <= 10:
        print("Your water bill is: ₱300.00")
    else:
       
        print(f"Your water bill is: ₱{(_customer_cubic_meters - 10) * (30) + 300:.2f}")


calculate_water_bill(10)
calculate_water_bill(20)
calculate_water_bill(30)
calculate_water_bill(40)
calculate_water_bill(50)
print()
calculate_water_bill(11)
calculate_water_bill(21)
calculate_water_bill(35)
calculate_water_bill(48)
calculate_water_bill(99)