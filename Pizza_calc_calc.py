print("PIZZA PRICE CHART")
print("Small Pizza = 100")
print("Medium Pizza = 200")
print("Large Pizza = 300")
print("\n")
print("Pepperoni for small pizza = 30")
print("Pepperoni for medium or large pizza = 50")
print("Extra cheese for any pizza = 20")

pizza_size = input("\nWhat size of pizza do you want?\n=")
pizza_pepperoni = input("Do you want pepperoni?\n=")
extra_cheese = input("Do you want extra cheese?\n=")

Bill = 0
Price_addition_pepperoni = 0
Price_addition_cheese = 0
Pizza_price = 0
pepperoni_status = "No pepperoni"
cheese_status ="No cheese"

if  pizza_size == "small" or pizza_size== "Small":
    Bill = 100
    Pizza_price = 100
    
    if pizza_pepperoni == "yes":
        Bill += 30
        Price_addition_pepperoni = 30
        pepperoni_status = "pepperoni"

elif pizza_size == "medium" or pizza_size== "Medium":
    Bill = 200
    Pizza_price = 200
    if(pizza_pepperoni == "yes"):
     Bill += 50
     Price_addition_pepperoni = 50
     pepperoni_status = "pepperoni"

elif pizza_size == "large" or pizza_size== "Large":
    Bill = 300
    Pizza_price = 300
    if(pizza_pepperoni == "yes"):
        Bill += 50
        Price_addition_pepperoni = 50
        pepperoni_status = "pepperoni"

if extra_cheese == "yes" or extra_cheese == "Yes":
    Bill += 20
    Price_addition_cheese = 20
    cheese_status="cheese"

print("\n ===YOUR BILL===")
print(f"Pizza    = {Pizza_price}") 
if pepperoni_status == "pepperoni":
    print(f"Pepperoni= {Price_addition_pepperoni}") 
if cheese_status == "cheese":
    print(f"Cheese   = {Price_addition_cheese}") 
print(f"Bill     = {Bill}" )
#{Pizza_price}+{Price_addition_pepperoni}({pepperoni_status})+{Price_addition_cheese}({cheese_status})")
