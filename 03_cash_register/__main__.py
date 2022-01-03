# Create a map where the key represents the product name and the value
# is a tuple where the first item is the price of the product and the second
# is the product stock
inventory = {
  'Apple': [5.0, 10],
  'Lemon': [1.0, 10],
  'Orange': [1.0, 10],
  'PlayStation 5': [600.0, 5],
  'Mechanical Keyboard': [100.0, 3],
  'Dog': [0.0, 1],
}

# Create a cart which is represented by an empty list
cart = []

# Sentinel value to stop prompting the user for products
ask_again = True

while ask_again:
  # Show table header to the user
  print(f'Article\tPrice\tStock')

  # Show each item to the user
  for key in inventory:
    print(f'{key}\t{inventory[key][0]}\t{inventory[key][1]}')

  # Ask user for option
  option = input('Enter your option: ')

  # Check if the option from the user is valid
  if option in inventory:
    # Appends the selected product to the cart
    # A new map is created with product details
    cart.append({
      'Name': option,
      'Price': inventory[option][0],
    })
    # Substract one item from stock
    inventory[option][1] = inventory[option][1] - 1
  else:
    # If the product name is not valid (the name doesn't exists in the
    # inventory map), then print the error to the screen
    print('Error: Invalid product selected')

  # Prompt the user for stopping the proceedure
  should_stop = input('Proceed to checkout? (y/n): ')

  if should_stop == 'y':
    ask_again = False
    break

# TODO: Print cart products similar to how its done for inventory
#
# Example:
#
# Article Price Stock
# Apple 5.0 9
# Lemon 1.0 9
# Orange  1.0 10
# PlayStation 5 600.0 5
# Mechanical Keyboard 100.0 3
# Dog 0.0 0
print(cart)
