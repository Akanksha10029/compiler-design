import re

# Python code for calculating the area of a rectangle
code = """
def area_of_rectangle(length, width):
    return length * width
length = 5
width = 3
area = area_of_rectangle(length, width)
print("Area of rectangle: ", area)
"""

# Regular expression to match tokens, including quoted strings
token_pattern = r'"[^"]*"|\'[^\']*\'|[a-zA-Z_]\w*|\d+|\S'
tokens = re.findall(token_pattern, code)

print("Tokens:\n", tokens)
print("\nNumber of Tokens:", len(tokens))
