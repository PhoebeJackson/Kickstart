T=int(input())
for case in range(1, T+1):
    L=int(input())
    dictionary = input().split(" ")
    S_1, S_2, N, A, B, C, D = input().split(" ")
    string= S_1 + S_2
    N=int(N)
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    x_minus_1 = ord(S_2)
    x_minus_2 = ord(S_1)
    for i in range(3,N+1):
        x_i = (A*x_minus_1 + B*x_minus_2 + C)%D
        string+= chr(97+(x_i%26))
        x_minus_2 = x_minus_1
        x_minus_1 = x_i
    print(string)
    count=0
    dictionary = sorted(dictionary)
    for word in dictionary:
        for i in range(len(string)-len(word)+1):
            if string[i]==word[0]: #first letter found
                if string[i+len(word)-1]==word[-1]: #last letter in correct place
                    if sorted(string[i:i+len(word)])==sorted(word): #rest of the word present?
                        count+=1
                        break
    print("Case #{}: {}".format(case, count))

        
