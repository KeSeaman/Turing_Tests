def word_to_number(s):
    # Convert each character to its corresponding integer position in the alphabet
    return ''.join(str(ord(char) - ord('a') + 1) for char in s)

def sum_of_digits(num_str):
    # Sum the digits of the number represented as a string
    return str(sum(int(digit) for digit in num_str))
def transform_word(s, n):
    # Step 1: Convert the word to the corresponding integer as a string
    num_str = word_to_number(s)

    # Step 2: Sum the digits n times
    for _ in range(n):
        num_str = sum_of_digits(num_str)

    # Convert the final string to an integer and return
    return int(num_str)


if __name__ == "__main__":
    # Example usage
    s = "turing"
    n = 3
    result = transform_word(s, n)
    print(result)  # Output: 8
