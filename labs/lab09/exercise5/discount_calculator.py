# discount_calculator.py
# Author: RABIATUL ADAWIYAH BINTI ABDUL HAKIM MC2515202759
# Description:
# This program determines the discount category for a movie ticket based on the customer's age.
# It calculates the final ticket price after applying the appropriate discount.
# The program also handles invalid numeric inputs such as negative values.

# --- Input Section ---
# Prompt user to enter age and ticket price
cus_age = int(input("Enter your age: "))
ticket_price = float(input("Enter the price of the movie ticket: "))

# --- Validation Section ---
if cus_age < 0 or ticket_price < 0:
    print("Error: Age and ticket price cannot be negative.")
else:
    # --- Processing Section ---
    if cus_age <= 12:
        discount_category = "Children"
        discount_rate = 0.50
    elif 13 <= cus_age <= 17:
        discount_category = "Teenagers"
        discount_rate = 0.25
    else:
        discount_category = "Adults"
        discount_rate = 0.00

    # Calculate discounted price
    discount_price = ticket_price - (ticket_price * discount_rate)

    # --- Output Section ---
    print(f"You are eligible for the {discount_category} discount ({int(discount_rate * 100)}% off).")
    print(f"Discounted ticket price: ${discount_price:.2f}")
