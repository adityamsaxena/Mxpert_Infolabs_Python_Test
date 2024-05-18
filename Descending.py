l1 = []
n = int(input("enter number of elements required: "))
for i in range(0, n):
    element = int(input())
    
    l1.append(element)
print("Original List:", l1)
 
for i in range(0, len(l1)):
  for j in range(i+1, len(l1)):
    if l1[i] <= l1[j]:
      l1[i], l1[j] = l1[j], l1[i]
       
print("Sorted List in Descending order:", l1)