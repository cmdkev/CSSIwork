snax = {
    'fruit snacks' : 10,
    'mini golden oreos' : 9,
    'apples' : 10,
}

snax['raisins'] = 8

for item in snax:
    # print item
    # print snax[item]
    if 'raisins' in snax:
        snax['raisins'] = 2
    print "%s get a %s out of 10" % (item, snax[item])
