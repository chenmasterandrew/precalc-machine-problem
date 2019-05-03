print("""
Welcome to Tom and Andrew's Machine Problem Simulation
This program performs a single production run of the desired strategy and number of sample parts.
The user may input their own variable values or use the preset ones used in our project writeup.
To see the code and comments for this program, please press the "edit" button in the top left.
""")

trials = 100000
from random import randint

# main function of the program
# accounts for the chosen simulation option, setting pre-set values if desired
# or leaving the variables as is if they were already chosen by the user
def go(strategy, samples, mode, n, d, g, k, w, m, s):
    cost = 0
    if mode == 1:
        n = 444
        d = 4
        g = 98
        k = 89
        w = 80
        m = 64
        s = 6
    elif mode == 2:
        dummy = 'dummy'
    else:
        Exception('{0} is not 1 or 2. Choose 1 or 2'.format(mode))
    masterMechanic = False
    
    # randomly sets the number of correct adjustments at the beginning of the production run
    adjustments = randint(1, 100)
    if adjustments in range(1, 81):
        goodAdjustments = 2
    elif adjustments in range(81, 96):
        goodAdjustments = 1
    else:
        goodAdjustments = 0
    
    # accounts for each strategy, modifying the cost depending on whether the mechanic is called
    # or for however many samples are taken
    if strategy == 1:
        masterMechanic = True
        cost += m
    elif strategy == 2:
        dummy = 'dummy'
    elif strategy == 3:
        assert (samples > 0), '{0} is not a number > 0'.format(samples)
        cost += samples * s
        for x in range(samples):
            if goodAdjustments == 2:
                if randint(1, 101) in range(1, 100 - g):
                    masterMechanic = True
            elif goodAdjustments == 1:
                if randint(1, 101) in range(1, 100 - k):
                    masterMechanic = True
            else:
                if randint(1, 101) in range(1, 100 - w):
                    masterMechanic = True
    else:
        raise Exception('{0} is not a viable strategy. Choose 1, 2, or 3'.format(strategy))
    
    # having the mechanic sets the adjustments correctly here
    if masterMechanic == True:
        goodAdjustments = 2

    # determines the cost of hand fitting defective parts:
    if goodAdjustments == 2:
        goodParts = n * (g/100)
    elif goodAdjustments == 1:
        goodParts = n * (k/100)
    else:
        goodParts = n * (w/100)
    badParts = n - goodParts
    cost += d * badParts
    return cost

# choose() function asks the user for which values they wish to choose
# called upon
def choose():
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
    return n, d, g, k, w, m, s

# takes into account the simulation option, calling choose() for user-chosen variables
# then loops for the number trials to make productions runs of each strategy, appending
# found values into lists
def display(mode):
    if mode == 2:
        n, d, g, k, w, m, s = choose()
    else:
        n = 0
        d = 0
        g = 0
        k = 0
        w = 0
        m = 0
        s = 0
    strategy1s = []
    strategy2s = []
    strategy31s = []
    strategy32s = []
    strategy33s = []
    strategies = []
    for t in range(1, trials + 1):
        trial1 = go(1, 100, mode, n, d, g, k, w, m, s)
        trial2 = go(2, 100, mode, n, d, g, k, w, m, s)
        trial31 = go(3, 1, mode, n, d, g, k, w, m, s)
        trial32 = go(3, 2, mode, n, d, g, k, w, m, s)
        trial33 = go(3, 3, mode, n, d, g, k, w, m, s)
        strategy1s.append(trial1)
        strategy2s.append(trial2)
        strategy31s.append(trial31)
        strategy32s.append(trial32)
        strategy33s.append(trial33)
        
    # averages lists of values for each strategy and displays them as the final output
    if mode == 1:
        print('SIMULATION RESULTS USING PRESET VARIABLE VALUES OVER ' + str(trials) + ' TRIALS')
    elif mode == 2:
        print("SIMULATION RESULTS USING USER'S VARIABLE VALUES OVER " + str(trials) + ' TRIALS')
    print('Strategy 1 average cost: $' + str(sum(strategy1s) / trials))
    print('Strategy 2 average cost: $' + str(sum(strategy2s) / trials))
    print('Strategy 3 with 1 sample average cost: $' + str(sum(strategy31s) / trials))
    print('Strategy 3 with 2 samples average cost: $' + str(sum(strategy32s) / trials))
    print('Strategy 3 with 3 samples average cost: $' + str(sum(strategy33s) / trials))

# asks the user for which values, preset as used in the writeup or user-chosen, they want to use
# calls the display() providing it with the chosen simulation option
run = int(input('Would you like to run the simulation with (1) preset variable values or (2) user-chosen variable values? Choose 1 or 2.'))
display(run)