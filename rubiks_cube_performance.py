lists = []

for i in range(1, 6):
    num = float(input("Enter the time for performance {:.0f}: ".format(i)))
    lists.append(num)

m = min(lists)
n = max(lists)

lists.remove(m)
lists.remove(n)

ave = sum(lists) / len(lists)

print()
print("The official competition score is {:.2f} seconds.".format(ave))