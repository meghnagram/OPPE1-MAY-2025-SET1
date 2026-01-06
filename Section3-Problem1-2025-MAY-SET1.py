def count_non_whitespace(sentence):
    return sum(1 for c in sentence if c not in ' \n')

def get_freqs(sentence):
    freq = {}
    for c in sentence.lower():
        if c.isalpha():
            freq[c] = freq.get(c, 0) + 1
    return freq

def most_frequent_char(sentence):
    freq = get_freqs(sentence)
    return max(freq, key=lambda x: (freq.get(x), x))
    
def count_diverse_words(sentence):
    return sum(
        1
        for word in sentence.lower().split() 
        if len([c for c in set(word) if c.isalpha()]) > 5
    )

def word_with_highest_char_frequency(sentence):
    return max(sentence.split(), key = lambda word: max(get_freqs(word).values()))

    
def analyse_text(sentence: str, task: str):
    """
    Processes the sentence based on the specified task.

    Args:
        sentence (str): The input sentence.
        task (str): 
            The task to perform. 
            One of 'count_non_whitespace', 'most_frequent_char',
            'count_diverse_words', or 'word_with_highest_char_frequency'.

    Returns:
        Result of the specified task.
    """
    
    
    if task == 'count_non_whitespace':
        return count_non_whitespace(sentence)
    elif task == 'most_frequent_char':
        return most_frequent_char(sentence)
    elif task == 'count_diverse_words':
        return count_diverse_words(sentence)
    elif task == 'word_with_highest_char_frequency':
        return word_with_highest_char_frequency(sentence)

# #Another Method:

# def get_freqs(sentence):
#     d={}
#     for i in sentence:
#         j=i.lower()
#         if 97<=ord(j)<=122:
#             if j not in d.keys():
#                 d[j]=1
#             else:
#                 d[j]+=1
#     return d

    
# def analyse_text(sentence: str, task: str):
#     """
#     Processes the sentence based on the specified task.

#     Args:
#         sentence (str): The input sentence.
#         task (str): 
#             The task to perform. 
#             One of 'count_non_whitespace', 'most_frequent_char',
#             'count_diverse_words', or 'word_with_highest_char_frequency'.

#     Returns:
#         Result of the specified task.
#     """
#     d={}
#     if task=='count_non_whitespace':
#         count=0
#         for i in sentence:
#             if i == ' ' or i == "\n":
#                 continue
#             else:
#                 count=count+1 
#         return count
        
#     if task=='most_frequent_char':
#         # d=get_freqs(sentence)
#         # e=max(d,key=d.get)
#         # return e
        
        
#         for i in sentence:
#             j=i.lower()
#             if 97<=ord(j)<=122:
#                 if j not in d.keys():
#                     d[j]=1
#                 else:
#                     d[j]+=1
#         emax=0
#         name=''
#         for key,value in d.items():
#             if value>emax:
#                 emax=value
#                 name=key
#             if value==emax:
#                 if ord(key)>ord(name):
#                     emax=value
#                     name=key
                
#         return name
    
#     if task=='count_diverse_words':
#         l=[]
#         count=0
#         stri=''
#         m=[]
        
#         s=sentence.lower()
#         l=s.split()
#         for i in l:
#             for j in range(len(i)):
#                 if 97<=ord(i[j])<=122:
#                     stri=stri+i[j]
#             m.append(stri)
#             stri=''
                    
#         for i in m:
#             j=set(i)
#             if len(j)>5:
#                 count +=1 
                
#         return count
        
#     if task=='word_with_highest_char_frequency':
#         l=[]
#         c=0
#         emax=0
        
#         charr=''
#         supermax=0
#         superword=''
        
#         s=sentence.lower()
#         l=s.split()
#         for i in l:
#             for j in range(len(i)):
#                 for k in range(j+1,len(i)):
#                     if i[j]==i[k]:
#                         c=c+1
#                 if c>emax:
#                     emax=c
#                     charr=i[j]
#                 c=0
#             if emax>supermax:
#                 supermax=emax
#                 superword=i
#         u=l.index(superword)
        
#         m=sentence.split()
        
        
        
#         return m[u]
            

# Text Frequency Analysis
# Write a function analyse_text(sentence, task) that analyzes a given sentence and computes results based on the task specified. It uses helper sub-functions to achieve the following tasks:

# count_non_whitespace - Returns the total number of characters in the sentence, excluding spaces and newline characters.
# most_frequent_char - Returns the most frequent character in the sentence(case insensitive) as a lowercase alphabet. In case of a tie, return the largest character in alphabetical order.
# count_diverse_words - Returns the number of words that contain more than 5 distinct characters(case insensitive i.e, "A" and "a" is considered same.).
# word_with_highest_char_frequency - Returns the word that has the highest frequency of any single character (case insensitive). In case of a tie, return the word that appears first.
# NOTE: Assume words are separated by spaces, do not consider non alphabetic chars in the analysis

# NOTE: This is a function-type question. You do not have to take input or print the output. Just complete the required function. You may define helper functions inside the main function if needed.

# Examples

# >>> sentence = """Python is fun, programming is awesome."""
# >>> analyse_text(sentence, "count_non_whitespace")
# 33
# >>> analyse_text(sentence, "most_frequent_char")
# 'i'
# >>> analyse_text(sentence, "count_diverse_words")
# 3
# >>> analyse_text(sentence, "word_with_highest_char_frequency")
# 'programming'
