# List of products sold
products = ["Laptop","Mobile","Tablet","Laptop","Mobile","Laptop","Headphones","Mobile"]

# Dictionary to store frequency
freq = {}

for p in products:
    freq[p] = freq.get(p,0) + 1

print("Frequency Distribution:")
print(freq)

# Find most popular product
popular = max(freq, key=freq.get)

print("Most Popular Product:", popular)
