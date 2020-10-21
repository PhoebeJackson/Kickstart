"""import math
T=int(input())
for case in range(1,T+1):
    N, K =[int(s) for s in input().split(" ")]
    M = [int(s) for s in input().split(" ")]
    difficulties=[]
    for i in range(N-1):
        difficulties.append(M[i+1]-M[i]) #difficulty
    difficulties=sorted(difficulties)
    grouped_difficulties = []
    diff_current=difficulties[0]
    count=0
    for diff in difficulties:
        if diff>diff_current:
            grouped_difficulties.append([diff_current, 1, count])#difficulty, number of chunks it is split into, number of times it occurs
            diff_current=diff
            count=1
        else:
            count+=1
    grouped_difficulties.append([diff_current, 1, count])#difficulty(chunk size), number of chunks it is split into, number of times it occurs
    num_left = K
    while len(grouped_difficulties)>0 and grouped_difficulties[0][0]<=1:
        grouped_difficulties.pop(0)
    while len(grouped_difficulties)>0 and num_left>=grouped_difficulties[-1][2]:
        original_difficulty = grouped_difficulties[-1][0]*grouped_difficulties[-1][1]
        grouped_difficulties[-1][1]+=1
        grouped_difficulties[-1][0] = original_difficulty/grouped_difficulties[-1][1]
        num_left-=grouped_difficulties[-1][2]
        while len(grouped_difficulties)>1 and grouped_difficulties[-1][0]>=grouped_difficulties[-2][0] and num_left>=grouped_difficulties[-1][2]:
            grouped_difficulties[-1][1]+=1
            num_left-=grouped_difficulties[-1][2]
        grouped_difficulties=sorted(grouped_difficulties, key=lambda tuple: tuple[0])
        while len(grouped_difficulties)>0 and grouped_difficulties[0][0]<1:
            grouped_difficulties.pop(0)
    if len(grouped_difficulties)>0:
        solution = math.ceil(grouped_difficulties[-1][0])
    else:
        solution = 1
    print("Case #{}: {}".format(case, solution))"""

#quicker solution found by binary searching for optimal difference and resulting k until k <= given K
import math

def corresponding_k(difficulties, d_potential):
    corresponding_k = 0
    for difficulty in difficulties:
        corresponding_k += math.ceil(difficulty/d_potential)-1
    return corresponding_k

T=int(input())
for case in range(1,T+1):
    N, K =[int(s) for s in input().split(" ")]
    M = [int(s) for s in input().split(" ")]
    difficulties=[]
    for i in range(N-1):
        difficulties.append(M[i+1]-M[i]) #difficulty
    lower = 0
    upper = max(difficulties)
    while (upper-lower)>1:
        mid = int((upper+lower)/2)
        if corresponding_k(difficulties, mid)>K:
            lower = mid
        else:
            upper = mid
    print("Case #{}: {}".format(case, upper))
