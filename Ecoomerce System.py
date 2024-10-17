# Ecommerce System
# Writer: Uzair Muhammad

# Stock and Price

products = { 
    "Laptops" : {"price": 140000, "stock": 10},
    "Smartphones" : {"price": 80000, "stock": 15},
    "Tablets" : {"price": 120000, "stock": 20},
    "Desktops" : {"price": 100000, "stock": 8},
    "Gaming Consoles" : {"price": 150000, "stock": 5},
    "Airpods" : {"price": 45000, "stock": 25},
}

Cart = {}

def display_stock():
    print("\nAvailable Stock of Products:")
    for product, details in products.items():  # Loop through the products
        print(f"{product} - {details['stock']} in stock")  # Show only the stock
    print("\n")

def add_to_cart(product, quantity):
    if product in products:
        if products[product]["stock"] >= quantity:  # Check if stock is sufficient
            if product in Cart:
                Cart[product] += quantity
            else:
                Cart[product] = quantity
            products[product]["stock"] -= quantity  # Reduce stock
            print(f"Added {quantity} {product}(s) to the cart successfully!")
        else:
            print(f"Sorry, only {products[product]['stock']} {product}(s) available in stock.")
    else:
        print(f"Sorry, {product} not available in the store.")

def view_cart():
    if not Cart:
        print("Your cart is empty.")
    else:
        print("\nYour Cart:")
        total_price = 0
        for product, quantity in Cart.items():
            price = products[product]["price"] * quantity
            total_price += price
            print(f"{quantity} x {product}: Rs{price}")
        print(f"\nTotal Price: Rs{total_price}")

def ecommerce_system():
    print("Welcome to the Simple E-commerce System!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. View available product stock")
        print("2. Add product to cart")
        print("3. View cart and total price")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            display_stock()  # Show only stock
        elif choice == '2':
            display_stock()  
            product = input("Enter the name of the product you want to add: ")
            try:
                quantity = int(input(f"Enter the quantity of {product} you want to add: "))
                add_to_cart(product, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        elif choice == '3':
            view_cart()
        elif choice == '4':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

ecommerce_system()
