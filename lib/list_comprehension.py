#!/usr/bin/env python3

def return_evens(num_list):
    
    result = [n for n in num_list if (n%2==0)]
    return result

#[ n in num_list if n%2==0 ]


def make_exclamation(sentence_list):
    
    return [n+"!" for n in sentence_list]



#Using a list comprehension, write a function `return_evens()` that returns a
#list of all of the even elements of a sequence of integers.

#```py
#return_evens([0, 1, 3, 5, 7, 8, 9])
# [0, 8]
#```

#Using a list comprehension, write a function `make_exclamation()` that takes
#a list of sentence strings and returns a list of sentence strings with
#exclamation marks at the end.

#```py
#make_exclamation(["Hello", "I'm doing great", "Python is fun"])
# ["Hello!", "I'm doing great!", "Python is fun!"]
#```

#When all of your tests are passing, submit your work using `git`.
