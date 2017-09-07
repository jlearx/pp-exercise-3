'''
Created on Sep 7, 2017

@author: jlearx
'''

if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    
    # One line solution with list comprehension
    [print(n) for n in a if (n < 5)]
    
    # New list solution
    for n in a:
        if (n < 5):
            b.append(n)
    
    print(b)
    
    # Ask the user for the condition
    b = []
    limit = int(input("Please enter the upper limit: "))
    print("Returning numbers less than " + str(limit) + ".")
    
    for n in a:
        if (n < limit):
            b.append(n)
    
    print(b)
    