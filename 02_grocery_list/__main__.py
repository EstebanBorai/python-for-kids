# Define empty list
products_list = []

# Repeat this code 5 times
for x in range(0, 5):
  # Ask the user for the product's name and store it in the `product_name`
  # variable
  product_name = input('Enter product name: ')
  # Ask the user for the product's price and store it in the `product_price`
  # variable
  product_price = input('Enter product price: ')
  # Create a tuple with the product name and product price, and store it in
  # the `product` variable
  product = (product_name, product_price)
  # Add the `product` to the list
  products_list.append(product)

# Show the list to the user
print(products_list)
