# groceries = ['OJ', 'oreos', 'bananas', 'grapes', 'brocolli', 'sweet potatoes', 'bread']
#
# for i in range(len(groceries)):
#     #for lists in range(len(groceries)):
#     print "%s.      %s" % (i+1, groceries[i])


def nameGroceries():
    groceries = []
    howMany = raw_input('How many groceries do you want ')
    for x in range(int(howMany)):
        item  = raw_input('What do you want? ')
        groceries.append(item)
    return "%s.  %s" % (x, groceries[x])

print nameGroceries()
