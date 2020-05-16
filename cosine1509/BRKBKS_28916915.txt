t = int(input())
for _ in range(t):
    inp = list(map(int, input().split()))
    s = inp[0]
    bricks = inp[1:]

    if s >= sum(bricks):
        print(1)
    elif ( bricks[0]+bricks[1]<=s or bricks[1]+bricks[2]<=s ):
        print(2)
    else:
        print(3)
