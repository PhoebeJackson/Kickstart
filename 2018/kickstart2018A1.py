#the highest valued non even digit either rounds up and is then followed by 0s or rounds down and is followed by 8s evaluate closer and answer is difference
#beware of 9s

def all_even(number):
    all_even = True
    for digit in str(number):
        if int(digit)%2==1:
            all_even = False
            break
    print(number, all_even)
    return all_even

def round_up_function(N):
    print(N)
    round_up=0
    round_now=False
    for digit in N:
        digit=int(digit)
        if round_now:
            round_up = round_up*10 + 0
        else:
            if digit%2 == 0:
                round_up = round_up*10 + digit
            else:
                round_up = round_up*10 + digit + 1
                round_now = True
    if not(all_even(round_up)):
        round_up = round_up_function(str(round_up))
    return round_up

def round_down_function(N):
    round_down=0
    round_now=False
    for digit in N:
        digit=int(digit)
        if round_now:
            round_down = round_down*10 + 8
        else:
            if digit%2 == 0:
                round_down = round_down*10 + digit
            else:
                round_down = round_down*10 + digit - 1
                round_now = True
    return round_down

T = int(input())
for case in range(1, T+1):
    N = input()
    round_up=round_up_function(N)
    round_down=round_down_function(N)
    round_up_diff = round_up-int(N)
    round_down_diff = int(N) - round_down
    print("Case #{}: {}".format(case, min(round_up_diff, round_down_diff) ))


