a=int(input())
b=int(input())
k=int(input())
def primeRange(x):
    prime=[2]
    digits=[2]
    for i in range(3,x):
        digits+=[i]
        val=[]
        for k in range(0, len(digits)-1):
            val+=[i%digits[k]]
        if val.count(0)==0:
            prime+=[i]
        else:
            continue
    return prime
p=primeRange(b)
for j in range (0,len(p)):
    if a>p[j]:
        continue
    else:
        for l in range (j,len(p), k):
          if l!=j:
            print(' ', end='')
            print('{}'.format(p[l]), end='')
          else:
            print('{}'.format(p[l]), end='')
        break
print('')