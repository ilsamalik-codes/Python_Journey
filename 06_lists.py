print("--- The Adventure Backpack ---")

# Let's create a List using square brackets [ ]
backpack = ["Water Bottle", "Map", "Flashlight"]

print("Right now, my backpack contains:")
print(backpack)

# We can add a brand new item to the END of the list using .append()
print("\nOh look! I found a Magic Compass on the ground!")
backpack.append("Magic Compass")

print("\nMy updated backpack:")
print(backpack)

# A neat trick: In Python, we can pick a specific item by its position.
# But computers count starting from 0, not 1!
# 0 = Water Bottle, 1 = Map, 2 = Flashlight...
print("\nThe item in position 0 is:", backpack[0])
print("\n The item in position 2 is:", backpack[2])
print("\n I found a notebook in my backpack!")
backpack.append("notebook")
print("\n My updated backpack:")
print(backpack)
print("\n The item in position 4 is:", backpack[4])
backpack.append("lunch box")
print(backpack)
