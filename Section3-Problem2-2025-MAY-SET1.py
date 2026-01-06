

deltas = list(map(int, input().split()))
curr = 0
for value in deltas:
    if value == 0:
        print(" " * curr + "=")
    elif value > 0:
        print(" " * curr + "=" * value + ">")
    else:
        print(" " * (curr + value) + "<" + "=" * (-value))
    curr += value

# #Another Method:

# s=input()

# m=[]
# q=[]

# m=s.split()
# for i in m:
#     q.append(int(i))

# pos=0



# for i in q:
#     if i > 0:
#         print(' '*pos,end='')
#         print('='*i+'>')
#         pos=pos+i
#     if i < 0 :
#         pos=pos+i
#         print(' '*pos,end='')
#         print('<'+'='*abs(i))
#     if i == 0 :
#         print(' '*pos,end='')
#         print('=')

# Draw Arrow Trail from Movement Deltas
# A movement delta is the change from the current position to the next position.

# Given a sequence of non-zero integers representing movement deltas, draw arrows representing each movement as described below.

# Starting with current position as 0, for each number in the input:

# Positive value v: draw a rightward arrow =====> of length v starting from the current position.
# Negative value -v: draw a leftward arrow <==== of length v, ending at the current position.
# Zero: draw a = at the current position.
# Assume that the current position will be always greater than or equal to zero.

# Arrows are made using:

# '=' repeated v times
# '>' for right arrow (ends with >)
# '<' for left arrow (starts with <)
# Each arrow should be drawn on a new line, aligned based on the cumulative position as described.

# Note:

# The starting position is index 0.
# After printing each arrow, update the position by adding the delta value to it.
# Sample Input

# 1 4 -2 5 0 -3 0 -3 1 4
# Sample Output

# =>
#  ====>
#    <==
#    =====>
#         =
#      <===
#      =
#   <===
#   =>
#    ====>
# Input Format

# A single line containing space-separated non-zero integers, the movement deltas.
# Output Format

# Print one line per delta representing the arrow as described.


