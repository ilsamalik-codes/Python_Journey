print("--- Welcome to the Python Cafe! ---")

# 1. VARIABLES & INPUT
name = input("Hello! What is your name? ")
print("Nice to meet you,", name)

# 2. IF / ELSE
drink = input("\nWould you like Coffee or Tea? ")
if drink == "Coffee":
    print("One hot Coffee coming right up!")
else:
    print("A nice cup of Tea for you!")

# 3. LISTS
print("\nHere is what we have in the bakery today:")
snacks = ["Chocolate Chip Cookie", "Blueberry Muffin", "Croissant"]

# 4. LOOPS (Showing the menu)
# This loops through our list of snacks and prints them one by one!
for item in snacks:
    print(" -", item)

# 5. Bringing it all together!
chosen_snack = input("\nWhich snack would you like to order? ")

print("\n--- YOUR RECEIPT ---")
print("Order for:", name)
print("Drink:", drink)
print("Food:", chosen_snack)
print("Thank you for visiting the cafe!")
tip = input ("Would you like to give a tip? ")
tip =int (tip)
print("Thank you for the $ ", tip ,"tip!")