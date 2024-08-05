import tokenize
import io
import keyword

def categorize_tokens(code):
    # Convert the code string to a stream
    code_stream = io.StringIO(code)
    
    # Tokenize the code
    tokens = tokenize.generate_tokens(code_stream.readline)
    
    # Initialize lists to store different types of tokens
    keywords = []
    identifiers = []
    operators = []
    separators = []
    literals = []
    
    # Loop through each token
    for token in tokens:
        token_type = token.type
        token_string = token.string

        # Check for keywords
        if token_type == tokenize.NAME and keyword.iskeyword(token_string):
            keywords.append(token_string)
        # Check for identifiers
        elif token_type == tokenize.NAME:
            identifiers.append(token_string)
        # Check for operators
        elif token_type in (tokenize.OP,):
            operators.append(token_string)
        # Check for literals (strings and numbers)
        elif token_type in (tokenize.STRING, tokenize.NUMBER):
            literals.append(token_string)
        # Skip certain tokens
        elif token_type in (tokenize.INDENT, tokenize.DEDENT, tokenize.NEWLINE, tokenize.ENDMARKER):
            continue
        # Treat everything else as separators
        else:
            separators.append(token_string)

    return {
        'keywords': keywords,
        'identifiers': identifiers,
        'operators': operators,
        'separators': separators,
        'literals': literals,
    }

# Example usage
code = '''
def add_two_numbers(a, b):
    return a + b 

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = add_two_numbers(num1, num2)

        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
'''

token_categories = categorize_tokens(code)
for category, tokens in token_categories.items():
    print(f"{category.capitalize()}: {', '.join(tokens)}")
