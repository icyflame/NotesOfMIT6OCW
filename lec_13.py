def fib(n):
    global numCalls
    numCalls += 1
    #print 'fib called with', n
    if n <= 1: return 1
    else: return fib(n-1) + fib(n-2)
    
def fastFib(n, memo):
    global numCalls
    numCalls += 1
    #print 'fib1 called with', n
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]

def fib1(n):
    memo = {0:1, 1:1}
    return fastFib(n, memo)

##numCalls = 0
##n = 300
##m = fib(n)
##print m,' ',
##print 'fib was called ',numCalls,' times'
##
##numCalls = 0
##n = 300
##m = fib1(n)
##print m,' ',
##print 'fib was called ',numCalls,' times'
##

##0-1 knapsack problem
##the w is the weight and v is the value vector
##i is the index of the last element
##aW is the available weight

numCalls = 0

def maxVal(w, v, i, aW):
    print 'maxVal called with:', i, aW
    global numCalls
    numCalls += 1
    if i == 0:
        if w[i] <= aW: return v[i]
        else: return 0
    without_i = maxVal(w, v, i-1, aW)
    if w[i] > aW: return without_i
    else: with_i = v[i] + maxVal(w, v, i-1, aW - w[i])
    return max(with_i, without_i)

w = [1,5,3,4]
v = [15,10,9,5]
i = 3
aW = 8

maxV = maxVal(w,v,i,aW);

print 'Maximum value is:',maxV
print 'Number of times that maxVal was called is:',numCalls
