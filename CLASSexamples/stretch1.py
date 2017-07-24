#numbers from 1 to n in a list and find which number is missing from the list
#longList = [1, 2, 3, 5, 6, 7, 9, 10, 11, 20, 100]
longList = [100, 4, 5, 8, 9, 10, 3, 2, 6, 7]
longList.sort()

def findMissing(numbers):
    i = 0
# i is always the correct index values
    missing = []
    for x in numbers:
#for each x (number) in a list
        i += 1
#add 1 to i for each value in list
        while x != i:
#return i is what worked initially, with one number missing --> USED WITH AN IF STATEMENT
            missing.append(i)
            i += 1  #tells python to keep going
# WHILE STATEMENT corrects if statement stopping after a certain vaue such as when
# it prints [4, 5, 6, 7, 8] when 4 and 8 are missing because the index values stop at 9
    return missing
print findMissing(longList)
