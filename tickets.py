# lottery tickets
from sys import argv

cr=[]
for i in range(1,8):
    cr.append(argv[i])
tickets=[]
for j in range(1, int((len(argv)-1)/7)):
    ticket=[]
    for i in range(j*7+1,j*7+8):
        ticket.append(argv[i])
    tickets.append(ticket)

def isIN(x):
    l=[]
    for i in x:
        if i in cr:
            l.append(i)
    return l


print('Correct numbers: {}'.format(' '.join(cr)), )
for i in tickets:
    info=isIN(i)
    if len(info):
        print('Ticket: {} ({} correct: {})'.format(' '.join(i), len(info), ' '.join(info)))
    else:
        print('Ticket: {} ({} correct)'.format(' '.join(i), len(info)))
