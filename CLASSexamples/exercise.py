from random import randint


name = raw_input('Enter your name ')
print "Hello %s. Do you want to play  Mad Libs?" % (name)
answer = raw_input("y/n ")
if answer == "y":
    noun = raw_input('Enter a noun ')
    verb = raw_input('Enter a verb ')
    adjective = raw_input('Enter an adjective ')
    adverb = raw_input('Enter an adverb ')

    #print "The " + adjective + " " + noun + " " + verb + " " + adverb + " and cried the entire time because of the massive tornado"
    #the bad way to do it ^^^

    print "The %s %s %s %s and cried the entire time because of the massive tornado" % (adjective, noun, verb, adverb)
    #the good way to do it ^^^

    print "Super hilarious! " + name
else:
    print "Do you want to do something else?"
    response = raw_input("y/n ")
    if response == "y":
        to_do_list = ['do the dishes', 'finish homework', 'make up your bed',
        'become ruler of the world', 'clean your room']
        tasks = to_do_list[randint(0,4)]
        print "You have to %s" % (tasks)
        excuse = raw_input("What's your excuse??? ")
        print "I didn't %s because %s" % (tasks, excuse)
    else:
        print "See you later!"
