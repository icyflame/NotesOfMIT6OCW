import math

b = 0

inputOK = True

while inputOK:   ##we can module this into a function
    b = input('Enter base:')
    if type(b) == type(2.0):
        inputOK = False

    else:
        print 'Error. Base should be floating point value'

inputOK = True

h = 0
while inputOK:
    h = input('Enter height:')
    if type(h) == type(2.0):
        inputOK = False

    else:
        print 'Error. Height should be floating point value'
        
hypo = math.sqrt(b*b + h*h)

print hypo, ' is the hypotenuse of this triangle'
