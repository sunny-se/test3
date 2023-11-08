import random
import os

# Generate a random Python file name
file_name = f"random_{random.randint(1000, 2000)}.py"

# Generate some random Python code for the file content
file_content = f"""
# Random Python File
import random

def generate_random_number():
    return random.randint(50, 150)

if __name__ == "__main__":
    number = generate_random_number()
    print(f"Random number: {number}")
"""

# Write the content to the file
with open(file_name, "w") as file:
    file.write(file_content)

print(f"Random Python file '{file_name}' has been generated.")
