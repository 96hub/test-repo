# test_script.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
def subtract(a, b):
    return a - b  # New feature: subtraction


if __name__ == "__main__":
    print("Test Results:")
    print(f"Addition: 3 + 5 = {add(3, 5)}")
    print(f"Multiplication: 3 * 5 = {multiply(3, 5)}")
    print(f"Subtraction: 10 - 3 = {subtract(10, 3)}")  # New test case for subtraction
