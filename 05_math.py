print("--- The Math Machine ---")

# Let's do some basic math
apples = 5
apples = apples + 3  # Adding 3
print("I have this many apples:", apples)

# We can also subtract (-), multiply (*), and divide (/)
# Give it a try below!
points = 25
points = points / 5  # divide by
print("My total points:", points)

# --- THE INPUT TRAP ---
print("\n--- The Time Traveler ---")
age_text = input("How old are you? ")

# input() ALWAYS gives us text (a string), even if you type a number.
# We have to turn that text into a real number using int() before doing math!
age_number = int(age_text)

# Now we can safely add!
next_year = age_number + 1
print("Next year, you will be", next_year, "years old!")
print("\n---My Professional journey---")
profession = input("whats your profession?")
print("I am aspiring to become:", profession)
