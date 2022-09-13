def diagonalDifference(arr):
    # Write your code here
    s1=0;s2=0
    n=int(len(arr)**0.5)
    j=0;k=n-1
    for i in range(len(arr)):
        if i==j:
            s1 = s1 + arr[i]
            j+=n+1
        if i==k:
            s2 = s2 + arr[i]
            k+=n-1
    s=s1-s2    
    s=abs(s)
    return s
