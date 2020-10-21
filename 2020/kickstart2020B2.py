T=int(input())
for case in range(1,T+1):
    N, D =[int(s) for s in input().split(" ")]
    X = [int(s) for s in input().split(" ")]
    for i in range(N-1,-1,-1):
        X_i = X[i]
        D = int(D/X_i)*X_i
    print("Case #{}: {}".format(case, D))
