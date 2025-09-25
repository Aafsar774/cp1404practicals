number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Variable to keep track of total
total_price = 0

# Loop through each item and ask for price
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price = total_price + price

# Give a 10% discount if total is over $100
if total_price > 100:
    total_price = total_price*0.9

# Display the result with 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
