# Restaurant system
print("Welcome to the Restaurant sir\nWhat would you like to order\nHere is the menu")

# Menu
items={
    "Pizza": 2200,
    "Pasta": 770,
    "Burger": 750,
    "Steak": 2500,
    "Platter": 2400,
    "Water": 150,
    "Salad": 350,
    "Toppings": 440
}

# Loop to display all items and their costs
for item in items:
    print(f"{item}: Rs.{items[item]}/-")

# Asking for order and display total cost
orders_list=[]
orders_price=0
while True:
    orders=input("What's your order sir?\n").capitalize()
    if orders in items:
        confirm=input("Would you like to order anything else Sir\n").capitalize()
        orders_list.append(orders)
        if confirm=="Yes":
            continue
        else:
            print("Your Order Summary is")
            for order in orders_list:
                print(f"{order}")
                orders_price+=items[order]
            print(f"Your order costs you Rs {orders_price}/- only")
            break
    else:
        print("sorry, We dont have that item in menu")