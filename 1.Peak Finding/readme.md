# Peak Finding

## One Dimentional Array

Assume we have: a= [1,2,3,..., n/2-1, n/2, n/2+1, n-2, n-1,n]  

### Steps
- If a[n/2] < a[n/2−1] then only look at left half 1...n/2−−−1 tolookforpeak.  
- Else if a[n/2] < a[n/2+1] then only look at right half n/2 + 1. . . n to look for peak.
- Else a[n/2] is the peak.


## Two Dimentional Array

Assume that we have:

a=  
[1,2,...,n/2-1, n/2, n/2+1, n/2+2,..,n]  
[.....................................]  
[.................,m/2,...............]  
[.....................................]  
[.................,m,.................]  

### Steps
- Pick middle columnj=m/2
- Find global maximum on column j at (i,j)
- Compare(i,j−1),(i,j),(i,j+1)
- Pick left columns of (i,j−1)>(i,j)
- Similarly for right
- (i,j) is a 2D-peak if neither condition holds.
- Solve the new problem with half the number of columns.
- When you have a single column,find global maximum and you‘re done.
   
   
