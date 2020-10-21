T=int(input())
for case in range(1,T+1):
    N = int(input())
    H = [int(s) for s in input().split(" ")]
    previous = H[0]
    could_be_peak=False
    count=0
    for i in range(1,N):
        H_i = H[i]
        if H_i>previous:
            could_be_peak=True
        elif H_i<previous and could_be_peak:
            count+=1
        if H_i<previous:
            could_be_peak = False
        previous = H_i
    print("Case #{}: {}".format(case, count))