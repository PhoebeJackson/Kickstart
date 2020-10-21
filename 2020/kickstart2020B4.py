#only needs calculating up to positive diagonal from the bottom left and top right corners - sum of these squares is the probability
#alternatively one minus the probability of falling in the hole
#calculating hole requires less squares to be calculated

#this method calculates the number of paths (kinda) to the bottom left square and the resulting probability - time limit exceeded for bigger test set
"""import numpy as np

T=int(input())
for case in range(1,T+1):
    W, H, L, U, R, D = [int(s) for s in input().split()]
    map = np.zeros((H,W))
    for row in range(H):
        for place in range(W):
            if row<D and place<R and row>U-2 and place>L-2:
                map[row][place]=0    
            elif row==0 and place==0:
                map[row][place]=1
            elif row==0:
                map[row][place]=map[row][place-1]
            elif place==0:
                map[row][place]=map[row-1][place]
            elif row==H-1 and place==W-1:
                map[row][place]=map[row][place-1]*2+map[row-1][place]*2
            elif row==H-1:
                map[row][place]=map[row][place-1]*2+map[row-1][place]
            elif place==W-1:
                map[row][place]=map[row][place-1]+map[row-1][place]*2
            else:
                map[row][place]=map[row][place-1]+map[row-1][place]
    probability = map[-1][-1]*(0.5**(W+H-2))
    print("Case #{}: {}".format(case, probability))"""

#calculating hole probability - similar method to previous for creating map and calculating each probability but smaller number needed because only requires up to bottom right of hole to be calculated

"""import numpy as np
T=int(input())
for case in range(1,T+1):
    W, H, L, U, R, D = [int(s) for s in input().split()]
    map = np.zeros((D,R))
    not_probability=0
    for row in range(D):
        for place in range(R):   
            if row==0 and place==0:
                map[row][place]=1
            elif row==0:
                if H==1:
                    map[row][place]=2*map[row][place-1]
                else:
                    map[row][place]=map[row][place-1]
            elif place==0:
                if W==1:
                    map[row][place]=2*map[row-1][place]
                else:
                    map[row][place]=map[row-1][place]
            elif row==H-1 and place==W-1:
                map[row][place]=map[row][place-1]*2+map[row-1][place]*2
            elif row==H-1:
                map[row][place]=map[row][place-1]*2+map[row-1][place]
            elif place==W-1:
                map[row][place]=map[row][place-1]+map[row-1][place]*2
            else:
                map[row][place]=map[row][place-1]+map[row-1][place]
            if row>U-2 and place>L-2:
                not_probability+=(0.5**(row+place))*(map[row][place])
                print(place, row, (0.5**(row+place))*(map[row][place]))
                map[row][place]=0
    probability = 1 - not_probability
    print("Case #{}: {}".format(case, probability))"""


#trying a solution using combinatorics
#sum of nCr for diagonal from bottom left and top right, n is row+column (starting from 0) r is row (or column) (starting from 0) diagonal therefore for each diagonal n is constant, use smaller of row or column and sum nCr for decreasing r to 0
#that was still not quick enough so an attempt to speed up this method involving checking if the number of calculations needed for calcuating if it will fall into the hole is more or less than for calculating if it will miss the hole and then (for each test case) use the quicker one - more complicated than thought because of holes that touch the wall needing different probability
from scipy.special import comb
T=int(input())
for case in range(1,T+1):
    W, H, L, U, R, D = [int(s) for s in input().split()]
    probability=0
    if L!=1 and D<H:
        for r in range(L-1):
            probability+=comb(D+L-2, r)*(0.5**(D+L-2))
    if U!=1 and R<W:
        for r in range(U-1):
            probability+=comb(U+R-2, r)*(0.5**(U+R-2))
    print("Case #{}: {}".format(case, probability))

    