r=int(input())
c=int(input())
h=int(input())
w=int(input())

for y in range(0,r):
    if y%2==0:
        for x in range(0,h):
            for i in range(0,c):
                if i%2==0:
                    for j in range(0, w):
                        print(' ', end='')
                else:
                    for k in range(0, w):
                        print('💖', end='')
            print('')
    else:
        for x in range(0,h):
            for i in range(0,c):
                if i%2==0:
                    for j in range(0, w):
                        print('💖', end='')
                else:
                    for k in range(0, w):
                        print(' ', end='')
            print('')