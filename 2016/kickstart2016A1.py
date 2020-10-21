file = 'Other/text1.txt'
f = open(file, 'r')

def numberofletters(word):
    letters=set()
    letters.add(" ")
    for character in word:
        letters.add(character)
    return len(letters)-1

T = int(f.readline().rstrip('\n'))
for case in range(1,T+1):
    N = int(f.readline().rstrip('\n'))
    optimum = 0
    bestname = ""
    for i in range(N):
        name = f.readline().rstrip('\n')
        noletters = numberofletters(name)
        if noletters>optimum:
            bestname = name
            optimum = noletters
        elif noletters==optimum:
            if name < bestname:
                bestname = name
    print("Case #{}: {}".format(case, bestname))

        
