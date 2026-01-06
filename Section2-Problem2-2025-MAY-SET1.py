
# Function to replace consonants with '#' and keep vowels unchanged
def replace_consonants(passage):
    # classical way
    result = ""
    for char in passage:
        if char.isalpha() and char.lower() not in 'aeiou':  # if consonant
            result += '#'
        else:
            result += char
    return result

    # using comprehensions
    # return "".join(
    #     '#' if char.isalpha() and char.lower() not in 'aeiou' else char 
    #     for char in passage
    # )

# Input handling
n = int(input())  # Number of lines
for _ in range(n):
    line = input()  # Read each line of the passage
    print(replace_consonants(line))  # Print the modified line


# #Another Method
# num=int(input())
# l=[]
# for i in range(num):
#     l.append(input())

# row=[]
# s=''
# for i in l:
#     for j in i:
#         if j==' ':
#             s=s+' '
#         elif j.lower() not in ('a','e','i','o','u'):
#             s=s+'#'
#         else:
#             s=s+j
#     row.append(s)
#     s=''

# for i in range(num):
#     print (row[i])   
        


# Replace Consonants with Hash
# Write a program that takes a multi-line string input and returns a new string where all consonants are replaced by #, but vowels stay unchanged.

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# The first line contains an integer n, the number of lines.
# The next n lines contain the passage.
# Output Format

# Print the passage with consonants replaced by # and vowels unchanged.
# Hint
# Use the isalpha() method to check for alphabets and string comparisons to identify vowels.

# Example

# Input

# 2
# Hello World
# Good Night

# Output

# #e##o #o###
# #oo# #i###
