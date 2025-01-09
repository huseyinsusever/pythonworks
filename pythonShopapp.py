# we will make empty basket
basket = {}

# Fill Basket enter user
while True:
    product_name = input("Enter product name(if you want exit 'q'):")
    if product_name.lower() =='q':
        break

    # Filling the cart by getting input from the user
    amount = input(f"{product_name} enter an amount: ")
    if not amount.isdigit(): 
        print("Please enter a number!")
        continue

    amount = int(amount) 
    basket[product_name] = amount

    # Basket lists
    print("\n--- Shopping basket---")
    for product, amount in basket.items():
        print(f"{product}: {product} amount")

    # Calculating total amount
    total_product = sum(basket.values())
    print("\nTotal number of products:", total_product)

   # Calculating total price by taking amount from user
    total_price = 0
    for product in basket:
     unit_price = input(f"{product} Enter the unit price for (TL): ")
    try:
        unit_price=float(unit_price) # Type conversion
        total_price += basket[product] * unit_price
    except ValueError:

        print("You have entered an invalid price. Continuing...")
        continue

    # Show results
    print("\n---Payment Information---")
    print("Total price:",str(total_price) + "TL") # `str()`

    #discount control(mantıksal değerler)
    discount = total_price > 100
    if discount:
        print("Congulations! %10 discount")
        total_price*=0.9 
        print("discount total:", str(total_price) + "TL")
    else:
        print("You are very close to winning a discount!")

    # end of program
    print("\n thank you for shopping!")   
