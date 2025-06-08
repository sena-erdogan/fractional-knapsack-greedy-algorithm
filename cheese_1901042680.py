def cheese(price, weight, capacity):
    w = 0
    p = 0.0
    
    sort(price, weight)
    
    for i in range(0,len(price)):
        if w + weight[i] <= capacity:
            w += weight[i]
            p += price[i]
        else:
            p += price[i] * (capacity - w) / weight[i]
            
    print("maximum price: ", p)
    
def sort(price, weight):
    for i in range(0, len(price)):
        for j in range(1, len(price)):
            if price[j]/weight[j] > price[i]/weight[i]:
                temp = price[i]
                price[i] = price[j]
                price[j] = temp
                
                temp = weight[i]
                weight[i] = weight[j]
                weight[j] = temp
    
cheese([1, 3, 2, 5, 8, 5], [2, 4, 6, 7, 9, 9] ,38)