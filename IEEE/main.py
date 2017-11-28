
def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                   knapSack(W, wt, val, n - 1))

val = []
wt = []
my_arr =map(int, raw_input().split())
for i in xrange(my_arr[0]):
    arr = map(int, raw_input().split())
    W = arr[0]
    for o in xrange(arr[1]):
        ar = map(int, raw_input().split())
        wt.append(ar[0])
        val.append(ar[1])
        ar = []

    n = len(val)
    print knapSack(W, wt, val, n)
    wt=[]
    val=[]