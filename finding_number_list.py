print("Give 5 numbers:")

lists=[]

for i in range(5):
    num=int(input("Next number: "))
    lists.append(num)

m=lists.reverse()
print("The numbers you entered that were greater than zero were:")
for i in lists:
    print(i)