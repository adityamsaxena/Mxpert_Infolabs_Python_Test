l1=[20,25,10,45,22,50,40]
 
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
 
print("Largest element is:", l1[-1])