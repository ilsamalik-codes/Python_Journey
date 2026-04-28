# --- LESSON 11: DICTIONARIES ---

# Lists [] are great for storing multiple items, but what if we want to attach names to them?
# Dictionaries {} store information in "key-value" pairs.
# Think of it like a real dictionary: you look up a word (key) to get its definition (value).

# 1. Creating a Dictionary
# We use curly braces {} and a : between the key and the value.
person = {"name": "Alice", "age": 28, "favorite_color": "blue"}

print("--- Example 1 ---")
# 2. Looking up values
# We use square brackets with the key name inside to find its value.
print("Name:", person["name"])
print("Age:", person["age"])


# 3. Adding or changing values
print("\n--- Example 2 ---")
person["age"] = 29  # Changes existing value
person["city"] = "New York"  # Adds a brand new key-value pair

print("Updated Person:", person)


# 1. Created dictionary here:
my_car = {"brand": "Toyota", "model": "Corolla", "year": 2022}


# 2. Print out the brand and model here:
print("\n   --- Example 3 ---")
print("Brand:", my_car["brand"])
print("Model:", my_car["model"])
print("Year:", my_car["year"])
