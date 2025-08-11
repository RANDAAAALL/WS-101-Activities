_number_items_sold = 0
_total_sales_today = 0

_items_prices = {
    1: ("Pandesal", 5.00),
    2: ("Cookies", 10.00),
    3: ("Taco", 35.00),
    4: ("Chips", 20.00),
    5: ("Siopao", 40.00),
}
print("--Welcome to our Small Bakery--")
print("What do you want for today?")

for _index in _items_prices:
    # print("Index Before: ", _index)
    print(f"[{_index}]: {_items_prices[_index][0]} - ₱{_items_prices[_index][1]:.2f}")
    
    while _index > 4:
        #  print("Index Right Now: ", _index)
         print("\nInstructions: Please type the number of your choice: 1, 2, 3, 4 or 5 only!")
         _customer_choice = input("Customer: ")

         if not _customer_choice.isdigit() or int(_customer_choice) not in _items_prices:
             print("Invalid choice! Please select a valid option from the menu next time!")
             continue
        
         _to_int = int(_customer_choice)

         print(f"You bought {_items_prices[_to_int][0]} for ₱{_items_prices[_to_int][1]:.2f}")
         _number_items_sold += 1
         _total_sales_today += _items_prices[_to_int][1]

         print("\nDo you want to buy another?")
         print("[1]: Yes")
         print("[2]: No")
         _customer_final_thoughts = int(input("Customer: "))
         
         if _customer_final_thoughts == 1: continue
         else:
            print("Thank you for visiting our bakery!")
            break
         
print(f"\nTotal items sold for today: {_number_items_sold}x")
print(f"Total items sales for today: {_total_sales_today:.2f}")

