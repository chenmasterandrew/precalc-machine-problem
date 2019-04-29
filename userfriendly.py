from random import randint
cost = 0
"""
# Random variables
n = randint(300, 1001)
d = randint(3, 10)
g = randint(96, 100)
k = randint(88, 93)
w = randint(78, 85)
m = randint(50, 101)
s = randint(2, 7)
"""
mode = int(input('Would you like to use (1) preset or (2) user-chosen variable values? (Type 1 or 2)'))
if mode == 1:
    n = 444
    d = 4
    g = 98
    k = 89
    w = 80
    m = 64
    s = 6
elif mode == 2:
    n = int(input('What n value? (Int 299<n<1001)'))
    assert (n in range(300, 1001)), '{0} is not (Int 299<n<1001)'.format(n)
    d = int(input('What d value? (Int 2<d<10)'))
    assert (d in range(3, 10)), '{0} is not (Int 2<d<10)'.format(d)
    g = int(input('What g value? (Int 95<g<100)'))
    assert (g in range(96, 100)), '{0} is not (Int 95<g<100)'.format(g)
    k = int(input('What k value? (Int 87<k<93)'))
    assert (k in range(88, 93)), '{0} is not (Int 87<k<93)'.format(k)
    w = int(input('What w value? (Int 77<w<85)'))
    assert (w in range(78, 85)), '{0} is not (Int 77<w<85)'.format(w)
    m = int(input('What m value? (Int 49<m<101)'))
    assert (m in range(50, 101)), '{0} is not (Int 49<m<101)'.format(m)
    s = int(input('What n value? (Int 1<s<7)'))
    assert (s in range(2, 7)), '{0} is not (Int 1<s<7)'.format(s)
else:
    Exception('{0} is not 1 or 2. Choose 1 or 2'.format(mode))
masterMechanic = False

print('n = ' + str(n))
print('d = ' + str(d))
print('g = ' + str(g))
print('k = ' + str(k))
print('w = ' + str(w))
print('m = ' + str(m))
print('s = ' + str(s))

adjustments = randint(1, 101)
if adjustments in range(1, 81):
    goodAdjustments = 2
elif adjustments in range(81, 96):
    goodAdjustments = 1
else:
    goodAdjustments = 0


# Strategies
print("""
Please choose a strategy:
#1: call a master mechanic at a cost of ${0} (m)
#2: do nothing and hope for the best
#3: run a sample of parts at a cost of ${1} (s) per part
    and call the master mechanic if any part is defective
""".format(m, s))
strategy = input('Which strategy do you wish to use? Choose 1, 2, or 3')
if strategy == '1':
    print("You've chosen strategy #1: call a master mechanic at a cost of ${0} (m).".format(m))
    masterMechanic = True
    cost += m
elif strategy == '2':
    print("You've chosen strategy #2: do nothing and hope for the best.")
elif strategy == '3':
    print("""
You've chosen strategy #3: run a sample of parts at a cost of ${0} (s) per part
                           and call the master mechanic if any part is defective
    """.format(s))
    samples = int(input('How many parts do you wish to sample? Choose a number > 0'))
    assert (samples > 0), '{0} is not a number > 0'.format(strategy)
    for x in range(5):
        cost += samples * s
        if goodAdjustments == 2:
            if randint(1, 101) in range(1, 100 - g):
                masterMechanic = True
        elif goodAdjustments == 1:
            if randint(1, 101) in range(1, 100 - k):
                masterMechanic = True
        else:
            if randint(1, 101) in range(1, 100 - w):
                masterMechanic = True
    if masterMechanic == True:
        print('Master mechanic was called')
else:
    raise Exception('{0} is not a viable strategy. Choose 1, 2, or 3'.format(strategy))
    
if masterMechanic == True:
    goodAdjustments = 2


# cost of hand fitting defective parts:
if goodAdjustments == 2:
    goodParts = n * (g/100)
elif goodAdjustments == 1:
    goodParts = n * (k/100)
else:
    goodParts = n * (w/100)
badParts = n - goodParts
cost += d * badParts
print('The total cost is ${0}'.format(cost))