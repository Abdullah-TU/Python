
while True:
    h=input()
    if h=='':
        print()
    else:
        h=int(h)
        c=input()
        step=h//2
        gap=-1
        for i in range(0,h):
            if i==0:
                s=' '*(step)+c+' '*(step)
                print(s)
            elif i<(h/2):
                step-=1
                gap+=2
                s=' '*(step)+c+' '*(gap)+c+' '*(step)
                print(s)
            elif i>(h/2) and i!= (h-1):
                step+=1
                gap-=2
                s=' '*(step)+c+' '*(gap)+c+' '*(step)
                print(s)
            elif  i==(h-1):
                step=h//2
                s=' '*(step)+c+' '*(step)
                print(s)
    print('')