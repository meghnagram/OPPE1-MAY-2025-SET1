def rotate_even(l: list, k: int) -> list:
    '''
    Returns a list with the elements at the even indices by k position.

    Examples:
    >>> rotate_even([1,2,3,4,5,6],1)
   [5,2,1,4,3,6]
   >>> rotate_even([1,2,3,4,5,6,7,8],3)
   [3,2,5,4,7,6,1,8]

    Args:
        l (list): a list
        k (int): number of positions to rotate.

    Returns:
        list: A list with even indices rotated.
    '''
    
    
    l = l.copy() # this ensures that the original list is not modified
    e = l[::2]
    k = k%len(e)
    l[::2] = e[-k:]+e[:-k]
    return l
    
# #Another method
# def rotate_even(l: list, k: int) -> list:
  
#     e=l[0::2]
#     o=l[1::2]
    
#     le=len(e)
#     lo=len(o)
    
#     for i in range(k):
#         a=e.pop()
#         e.insert(0,a)
    
#     final=[]
    
#     for i in range(len(l)//2):
#             final.append(e[i])
#             final.append(o[i])
#     if le>lo:
#             final.append(e[-1])
#     if lo>le :
#         final.append(o[-1])
   
#     return final
    
#     Rotate Even Indices
# Write a function rotate_even(l, k), which rotates the elements at the even indices by k positions.

# Hint: This can be solved using slicing and slice update.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example\

# >>> rotate_even([1,2,3,4,5,6],1)
# [5,2,1,4,3,6]
# >>> rotate_even([1,2,3,4,5,6,7,8],3)
# [3,2,5,4,7,6,1,8]
# Explanation

# rotate_even([1,2,3,4,5,6],1)

# +----------+
# |  +---+   |
# |  |   V   |
# | [1,2,3,4,5,6]
# |  ^   |   ^ 
# +--+   +---+ 
# Each element moves 1 even index and cycle back.

# 1 (index 0) moves to index 2
# 3 (index 2) moves to index 4
# 5 (index 4) moves to index 0
# rotate_even([1,2,3,4,5,6,7,8],3)

#  +-----------+   
#  |   +---+   |
#  |   V   |   V 
# [1,2,3,4,5,6,7,8]
#  ^   |   ^   |
#  +---+   +---+
# Each element moves two even indices and cycle back.

# 1 (index 0) moves to index 6
# 3 (index 2) moves to index 0
# 5 (index 4) moves to index 2
# 7 (index 6) moves to index 4
