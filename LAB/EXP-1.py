# EXP–1: Total Cost Calculation

# Item prices and quantities
prices = [100, 50, 30]
quantities = [2, 3, 1]

discount_rate = 10   # in percentage
tax_rate = 5         # in percentage

# Step 1: Calculate subtotal
subtotal = 0
for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

# Step 2: Calculate discount
discount = subtotal * (discount_rate / 100)

# Step 3: Price after discount
after_discount = subtotal - discount

# Step 4: Calculate tax
tax = after_discount * (tax_rate / 100)

# Step 5: Final total cost
total_cost = after_discount + tax

# Output
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Total Cost:", total_cost)
