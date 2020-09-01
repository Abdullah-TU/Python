def print_list(vals, a=0, b=None, k=1):
    if b==None:
        b=len(vals)-1
        if a>len(vals) or a<0 or k<=0:
            print('Illegal parameter a = {}, b = {} or k = {}!'.format(a, b, k))
        else:
            for i in range(a,len(vals),k):
                print('{}: {}'.format(i, vals[i]))


    elif  0<=a and a<=b and k>0 and b>len(vals):
        for i in range(a,len(vals),k):
            print('{}: {}'.format(i, vals[i]))
    elif  0<=a and a<=b and k>0 and b<=len(vals):
        for i in range(a,b+1,k):
            print('{}: {}'.format(i, vals[i]))
    else:
        print('Illegal parameter a = {}, b = {} or k = {}!'.format(a, b, k))