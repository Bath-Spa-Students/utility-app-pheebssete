# Delay print function
import time

def delay_print(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Display for the vending machine
delay_print("""              WELCOME TO READY N GO VENDING MACHINE
                    THE SNACKS THAT YOU NEED""", 0.1)
print()
delay_print(" * PLEASE CHOOSE YOUR SNACKS and DRINKS * ", 0.1)
print()
delay_print(" * Ready n Go Snacks * ", 0.1)
print()

# Snacks and drinks available
#Snacks Available
items_menu = {
   "Snacks": {
      'A01' :{"S":"Lay's Original", 'price': 2.00, 'stock': 5},
      'A02' :{"S":"Doritos", "price": 2.00, "stock": 6},
      'A03' :{"S":"Cheetos", 'price': 2.50, 'stock': 4},
      'A04' :{"S":"Takis", 'price': 3.00, 'stock': 5},
      'A05' :{"S":"Twix", 'price': 1.00, 'stock': 5},
   },
#Cold drinks
    "Cold Drinks": {
      'B01' :{"S":"Mirinda", 'price': 2.00, 'stock': 5},
      'B02' :{"S":"Sprite", 'price': 2.00, 'stock': 7},
      'B03' :{"S":"Diet Coke", 'price': 2.50, 'stock': 9},
      'B03' :{"S":"Coca Cola", 'price': 3.00, 'stock': 3},
      'B04' :{"S":"Water", 'price': 1.50, 'stock': 6},
      'B05' :{"S":"Apple Juice", 'price': 1.00, 'stock': 5},
   },  
#Hot drinks
    "Hot Drinks":{
       'C01' :{"S":"Chocolate Milk", 'price': 2.00, 'stock': 5},
       'C02' :{"S":"Coffee", 'price': 2.00, 'stock': 3},
       'C03' :{"S":"Steamed Milk", 'price': 2.00, 'stock': 4},
       'C04' :{"S":"Matcha", 'price': 2.00, 'stock': 3},
       'C05' :{"S":"Espresso", 'price': 2.00, 'stock': 6},
    }
}

# Funcntions
print("Please Choose What Iteams You Want To Purchase:")
print()
print("-------- Snacks --------")

snacks_items = items_menu["Snacks"]

for code, item_info in snacks_items.items():
    print(f"{code}: {item_info['S']} - AED {item_info['price']} ({item_info['stock']} in stock)") #For Loops to print the snacks items
print()

print("-------- Cold Drinks --------")

cold_drinks_items = items_menu["Cold Drinks"]

for code, iteam_info in cold_drinks_items.items():
    print(f"{code}: {iteam_info['S']} - AED {iteam_info['price']} ({iteam_info['stock']} in stock)") #For Loops to print the Cold drinks items
print()

print("-------- Hot Drinks --------")

hot_drinks_items = items_menu["Hot Drinks"]
for code, items_info in hot_drinks_items.items():
    print(f"{code}: {items_info['S']} - AED {items_info['price']} ({items_info['stock']} in stock)") #For Loops to print the Hot drinks items
print()

while True:
    enter = input("Please, Enter the code of the item you want: ") # User input

    if enter in snacks_items:
        enter = snacks_items[enter]
    elif enter in cold_drinks_items:
        enter = cold_drinks_items[enter]
    elif enter in hot_drinks_items:
        enter = hot_drinks_items[enter]
    else:
        print("Invalid input. Please enter a valid value.") # Wrong input of the user
        print() 
        continue

    if enter['stock'] <= 0: # Stock management
        print("Out of stock. Please choose another item.")
        print()
        continue

    payment = float(input("Enter the amount of money you are inserting: "))

    if payment < enter['price']:
        print("Not enough money. Please try again.")
        print()
        continue

    change = payment - enter['price']
    enter['stock'] -= 1  # Stock management (Decrease by 1)
    print(f"Your selected item is {enter['S']}. Your change is AED{change:.2f}")

    if input("Do you want to buy another item? (yes/no): ").lower() != 'yes':
        break

print()
print("Thank You For Choosing READY n GO, Enjoy your snacks")
