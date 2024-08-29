# area of a rectangle
#allow user to specify the length and width, but use default values of 10 for both if no arguments are provided.

def calculate_area(length=10, width=10):
    area = length * width
    return area

# Example usage
print("Example 1: Default values")
print(f"The area of the rectangle is: {calculate_area()}")

print("\nExample 2: Custom values")
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle is: {calculate_area(length, width)}")
