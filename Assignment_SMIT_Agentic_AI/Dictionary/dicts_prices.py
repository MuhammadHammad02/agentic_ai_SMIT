# Create a dictionary of 3 products and their prices (e.g., {"apple": 1.5, "banana": 0.75, "orange": 1.2}). Ask the user which product's price they want to see and display it.

if __name__ == "__main__":
    products = {
        "apple" : 1.5, 
        "banana" : 0.75,
        "orange" : 1.2,
    }

    # Ask the user which product's price they want to see and display it
    product_name = input("Enter the product name (apple, banana, orange):").lower()

    if product_name in products:
        print(f"The price of {product_name} is ${products[product_name]:.2f}")
    else:
        print("Product not found.")

