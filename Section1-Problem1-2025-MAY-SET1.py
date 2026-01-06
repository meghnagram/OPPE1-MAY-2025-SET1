def describe_number(num: int) -> str:
    '''
    Given an integer, return the description based on divisibility:
    - "Fizz" if divisible by 3
    - "Buzz" if divisible by 5
    - "FizzBuzz" if divisible by both 3 and 5
    - "Normal" if divisible by neither

    Examples:
    describe_number(9) -> "Fizz"
    describe_number(10) -> "Buzz"
    describe_number(15) -> "FizzBuzz"
    describe_number(7) -> "Normal"

    Args:
        num (int): The number to be checked.

    Returns:
        str: The description based on divisibility.
    '''
    
    
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "Normal"
      
# Describe Number Based on Divisibility
# Write a function describe_number that takes an integer as input and returns:

# "Fizz" if the number is divisible by 3.
# "Buzz" if divisible by 5.
# "FizzBuzz" if divisible by both 3 and 5.
# "Normal" if it is divisible by neither.
# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example
# describe_number(9) -> "Fizz"
# describe_number(10) -> "Buzz"
# describe_number(15) -> "FizzBuzz"
# describe_number(7) -> "Normal"



    
