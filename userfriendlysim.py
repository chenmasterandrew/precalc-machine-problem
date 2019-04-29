trials = 100000
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
def go(strategy, samples, mode, n, d, g, k, w, m, s):
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
    adjustments = randint(1, 101)
    if adjustments in range(1, 81):
        goodAdjustments = 2
    elif adjustments in range(81, 96):
        goodAdjustments = 1
    else:
        goodAdjustments = 0
    if strategy == 1:
        masterMechanic = True
        cost += m
    elif strategy == 2:
        dummy = 'dummy'
    elif strategy == 3:
        assert (samples > 0), '{0} is not a number > 0'.format(samples)
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
    return cost


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
        strategies.append((trial1, trial2, trial31, trial32, trial33))
    strategiesdf = pd.DataFrame(strategies)
    if mode == 1:
        print('SIMULATION RESULTS USING PRESET VARIABLE VALUES')
    elif mode == 2:
        print("SIMULATION RESULTS USING USER'S VARIABLE VALUES") 
        
    print('Strategy 1 average cost: $' + str(sum(strategy1s) / trials))
    print('Strategy 2 average cost: $' + str(sum(strategy2s) / trials))
    print('Strategy 3 with 1 sample average cost: $' + str(sum(strategy31s) / trials))
    print('Strategy 3 with 2 samples average cost: $' + str(sum(strategy32s) / trials))
    print('Strategy 3 with 3 samples average cost: $' + str(sum(strategy33s) / trials))
    strategiesdf.columns=['Strategy 1 Cost in $', 'Strategy 2 Cost in $', 'Strategy 3 Cost in $ with 1 Sample', 'Strategy 3 Cost in $ with 2 Samples', 'Strategy 3 Cost in $ with 3 Samples']
    return strategiesdf
run = int(input('Would you like to run the simulation with (1) preset variable values or (2) user-chosen variable values? Choose 1 or 2.'))
display(run)