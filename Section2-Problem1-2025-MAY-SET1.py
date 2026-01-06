def unique_sum_pairs(nums: list, k: int) -> set:
    '''
    Given a list of integers and an integer k, return a set of unique tuples
    where each tuple contains two different elements that sum up to k.

    Same number can only be used as a pair if it appears atleast twice in the list.

    Examples:
    >>> unique_sum_pairs([1, 2, 3, 2, 1], 4)
    {(1, 3), (2, 2)}
    >>> unique_sum_pairs([1, 5, 7, -1, 5], 6)
    {(1, 5), (-1, 7)}

    Args:
        nums (list): A list of integers
        k (int): The target sum to be achieved by pairs

    Returns:
        set: A set of unique tuples where the sum is k
    '''
    
    
    result = set()
    seen = set()
    for num in nums:
        complement = k - num
        if complement in seen:
            result.add(tuple(sorted((num, complement))))
        seen.add(num)
    return result

# #Another Method

# def unique_sum_pairs(nums: list, k: int) -> set:
#     d=[]
#     d=sorted(nums)
#     a=set()
    
    
#     for i in range(len(d)):
#         for j in d[i+1::]:
#             if d[i]+j == k:
#                 t=(d[i],j)
#                 a.add(t)
    
#     return a

# Unique Sum Pairs
# Write a function unique_sum_pairs(nums: list, k: int) -> set that takes a list of integers nums and an integer k, and returns a set of unique tuples, where each tuple contains two elements from the list that sum up to k and sorted in ascending order.

# Same number can only be used as a pair if it appears atleast twice in the list.

# Example

# >>> unique_sum_pairs([1, 2, 3, 2, 1], 4)
# {(1, 3), (2, 2)}
# >>> unique_sum_pairs([1, 2, 3, 1], 4)
# {(1, 3)}
# >>> unique_sum_pairs([1, 5, 7, -1, 5], 6)
# {(1, 5), (-1, 7)}
# >>> unique_sum_pairs([3, 3, 3, 3], 6)
# {(3, 3)}
# >>> unique_sum_pairs([1, 2, 3, 4, 5], 10)
# set()
    
