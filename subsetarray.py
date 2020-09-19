def printPowerSet(set,set_size): 
    pow_set_size = (int) (2 ** set_size); 
    counter = 0; 
    j = 0; 
      
    # Run from counter 000..0 to 111..1 
    for counter in range(0, pow_set_size): 
        for j in range(0, set_size): 
              
            # Check if jth bit in the  
            # counter is set If set then  
            # print jth element from set  
            if((counter & (1 << j)) > 0): 
                print(set[j], end = ""); 
        print(""); 
  
# Driver program to test printPowerSet 
set = ['a', 'b', 'c']; 
printPowerSet(set, 3); 
