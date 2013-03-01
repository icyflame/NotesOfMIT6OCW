def pigsAndChickens(nHeads,nLegs):
    """The farmer has pigs and chickens only. to find the number of pigs and chickens. enter the number of heads and pigs as parameters"""

    p=0 ##number of pigs
    c=0 ##number of chickens

    while(p<nHeads):
        c=nHeads-p

        if 4*p + 2*c == nLegs:
            print p, ' pigs'
            print c,' chickens'
            input()
            return None

        else: p+=1

    print 'There is no solution'
        

h=0
l=0
h=int(raw_input('Enter the number of heads:'))
l=int(raw_input('Enter the number of legs:'))

pigsAndChickens(h,l)
