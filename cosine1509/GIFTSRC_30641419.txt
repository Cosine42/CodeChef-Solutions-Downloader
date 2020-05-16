for _ in range(int(input())):
    n = int(input())
    s = input()
    w=s[0]
    for i in range(1,n):
        a=s[i]
        b=w[-1]
        if a=='L' or a=='R':
            if b=='U' or b=='D':
                w+=s[i]
        elif b=='L' or b=='R':
            w+=s[i]
    xco = w.count('R')-w.count('L')
    yco = w.count('U')-w.count('D')
                         
    print(xco, yco)
