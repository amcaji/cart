def frac_knapsack(values, weights, W):
    items=[]
    
    for v,w in zip(values,weights):
        items.append((v/w,v,w))
        
    items.sort(reverse = True)
    
    total = 0
    
    for ratio , value , weight in items:
        if W == 0:
            break 
        
        
        if weight <= W:
            total += value
            W -= weight 
            
            
        else:
            total += ratio * W
            W = 0 
                
                
    return total
n = int(input("Enter number of items: "))

values = list(map(int, input("Enter values: ").split()))
weights = list(map(int, input("Enter weights: ").split()))
W = int(input("Enter capacity: "))

print("Maximum value =", frac_knapsack(values, weights, W))
