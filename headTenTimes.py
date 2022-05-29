from random import randint

def coinToss():
    randomNum = randint(0,1)
    if randomNum == 0:
        return "heads" 
    else:
        return "tails"

def headTenTimes():
    counter = 0
    percentage = 0
    while counter <= 10:
        toss = coinToss()
        if toss == "heads":
            counter += 1
        else:
            percentage = int(counter/10 * 10)
            return percentage
    return percentage

def tossThousandTimes():
    data = []
    for i in range(0,2**10):
        data.append(headTenTimes())
    return data

def uniqueVals(lst):
    vals = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    vals = [int(val * 10) for val in vals]
    counts = []
    for val in vals:
        counts.append(lst.count(val))
    res = {vals[i]: counts[i] for i in range(len(vals))}
    return res

if __name__ == '__main__':
    data = tossThousandTimes()
    unique = uniqueVals(data)
    print(unique)