def combinations(l, sum, K, local, A): 

    if (sum == K): 
        temp=[]
        for i in range(len(local)): 
            temp.append(local[i])
        if len(temp)==2:
            super_set.append(temp)
        return
  
    # For all other combinations 
    for i in range(l, len(A), 1): 
        if (sum + A[i] > K): 
            continue
  
        if (i == 1 and 
            A[i] == A[i - 1] and i > l): 
            continue
  
        local.append(A[i]) 
  
        combinations(i + 1, sum + A[i],  
                                K, local, A) 
  
        local.remove(local[len(local) - 1]) 
  
  
A = [10, 1, 2, 7, 6, 1, 5] 
super_set=[]
K = 8
local = [] 
A.sort(reverse = False) 
combinations(0, 0, K, local, A)
print(super_set)

