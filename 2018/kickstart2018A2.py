"""def solve(list, K, N):
    sorted_list=sorted(list)
    prize_values=[]
    previous_prize=0
    sum_all = 0
    for prize in sorted_list:
        sum_all+=prize
        if prize>previous_prize:
            if previous_prize>0:
                prize_values.append((previous_prize,prize_count))
            prize_count=1
            previous_prize=prize
        else:
            prize_count+=1
    prize_values.append((previous_prize,prize_count))
    if len(prize_values)==1:
        return prize_values[0][0]
    av_all = sum_all/N    
    sum_keep=0
    no_keep=0
    keep_values=[]
    for keep in range(1,len(prize_values)):
        sum_keep+=prize_values[-keep][0]*prize_values[-keep][1]
        no_keep+=prize_values[-keep][1]
        keep_values.append((no_keep, sum_keep))
    return(optimum(keep_values, av_all, K, N))
    
def optimum(keep_values, av_all, K, N):
    if K==0:
        return av_all
    best_after = optimum(keep_values, av_all, K-1, N)
    best=0
    for keep in keep_values:
        sum_keep=keep[1]
        no_keep=keep[0]
        expected = (no_keep / N)* (sum_keep / no_keep) + ((N-no_keep)/N)*best_after
        if expected>best:
            best=expected
        else:
            break
    return best

T = int(input())
for case in range(1, T+1):
    N,K = [int(s) for s in input().split(" ")]
    V = [int(v_i) for v_i in input().split(" ")]    
    print("Case #{}: {}".format(case, solve(V,K,N)))
"""


#better solution: each time redip if expected value of remaining redips is higher than what you draw

T = int(input())
for case in range(1, T+1):
    N,K = [int(s) for s in input().split(" ")]
    V = [int(v_i) for v_i in input().split(" ")]
    expected = sum(V)/N
    V=sorted(V, reverse=True)
    for i in range(1,K+1):
        total=0
        for i in range(N):
            if V[i]>expected:
                total+=V[i]
            else:
                total+=expected*(N-i)
                break
        expected=total/N
    print("Case #{}: {}".format(case, expected))