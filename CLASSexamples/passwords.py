#8 character random password, letters only
from random import randint
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def chooseRandom(choices):
    return choices[randint(0, len(choices) - 1)]

# newPassword = newPassword + chooseRandom(alphabet)
# newPassword = newPassword + chooseRandom(alphabet)
# newPassword = newPassword + chooseRandom(alphabet)
# newPassword = newPassword + chooseRandom(alphabet)
# newPassword = newPassword + chooseRandom(alphabet)
# newPassword = newPassword + chooseRandom(alphabet)
# newPassword = newPassword + chooseRandom(alphabet)
# newPassword = newPassword + chooseRandom(alphabet)

newPassword = ""
#generating passwords with a loop 
for i in range(8):
    newPassword = newPassword + chooseRandom(alphabet)

print newPassword
