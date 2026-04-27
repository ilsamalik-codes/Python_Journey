# --- LESSON 10: RETURNING VALUES ---

# 1. Returning a value
# 'return' allows the function to compute a result and pass it back
# so we can store it in a variable or use it later.

def add_numbers(num1, num2):
    total = num1 + num2
    return total  # Gives the 'total' back to whoever called this function!

print("--- Example 1 ---")
# Calling the function and saving the result in a variable 'answer'
answer = add_numbers(5, 10)
print("The answer is:", answer)


# 2. Returning without saving to a variable
# We can also put the function call directly inside a print statement:
print("\n--- Example 2 ---")
print("100 + 50 =", add_numbers(100, 50))


# --- YOUR TURN! ---
# 1. Write a function called 'multiply_numbers' that takes two arguments (a, b).
# 2. Make it return the result of a * b.
# 3. Call your function with two numbers and print the result!

# Define your function here:
def multiply_numbers(a,b):
    total = a * b
    return total
    


# Call and print it here:
print("--- Example 3 ---")
print("10 * 5 =", multiply_numbers(10, 5))
print("2 * 3 =", multiply_numbers(2, 3))
print("4* 5 =", multiply_numbers(4, 5))

def divide_numbers(a,b):
    total = a / b
    return total

print("--- Example 4 ---")
print("10 / 5 =", divide_numbers(10, 5))

