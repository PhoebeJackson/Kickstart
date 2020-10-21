import random
def result(costs, r, M):
    total=-int(costs[0])*(1+r)**(M+1)
    for month in range(1,M+1):
        total+=int(costs[month])*(1+r)**(M+1-month)
    if total>0:
        positive = True
    else:
        positive = False
    return total, positive
T = int(input())
for test in range(1,T+1):
    M = int(input())
    costs= input().split(" ")
    r1=0
    r2=random.uniform(-1,1)   
    result1, positive1 = result(costs, r1, M)
    result2, positive2 = result(costs, r2, M)
    while positive1==positive2:
        r2=random.uniform(-1,1)
        result2, positive2 = result(costs, r2, M)
    rMiddle = (r1+r2)/2
    resultMiddle, positiveMiddle = result(costs, rMiddle, M)
    while abs(result(costs, rMiddle*1.000001, M)[0])<abs(resultMiddle) or abs(result(costs, rMiddle * 0.999999, M)[0])<abs(resultMiddle):
        if positiveMiddle==positive1:
            positive1=positiveMiddle
            r1=rMiddle
            result1=resultMiddle
        elif positiveMiddle==positive2:
            positive2=positiveMiddle
            r2=rMiddle
            result2=resultMiddle
        else:
            while positive1==positive2:
                r2=random.uniform(-1,1)
                result2, positive2 = result(costs, r2, M)
        rMiddle = (r1+r2)/2
        resultMiddle, positiveMiddle = result(costs, rMiddle, M)
    print("Case #{}: {}".format(test, rMiddle))