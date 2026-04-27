# --- LESSON 9: FUNCTIONS ---

# A function is a block of reusable code that only runs when it is called (used).
# We use the 'def' keyword to "define" a new function.

# 1. Defining a simple function
def say_hello():
    print("Hello, world!")
    print("Welcome to learning functions!")

# The code above "teaches" Python what say_hello means, but it won't do anything yet!
# To make it run, we have to "call" it.

print("--- Example 1 ---")
say_hello()   # This calls the function!
say_hello()   # We can call it as many times as we want without rewriting the print lines!


# 2. Passing arguments (giving our function information)
# We can tell our function to expect a piece of data inside the parentheses.
def say_hello_to(name):
    print("Hello,", name)
    print("I hope you're having a good day!")

print("\n--- Example 2 ---")
# When we call it, we have to give it a name inside the parentheses.
say_hello_to("Alice")
say_hello_to("Bob")

# 1. Define your function here:
def greet_student(name):
    print ("hello ", name)
    print("welcome to learning functions!")



# 2. Call your function here:
print("--- Example 3 ---")
greet_student("ali")
greet_student("ilsa")
