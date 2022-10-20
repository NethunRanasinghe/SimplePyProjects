# creating a function for bubble sort 
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

#unsorted list
list1 = [80,11,82,41,10,39,15,53,66]
#sorting the list with bubblesort
bubbleSort(list1)
print(list1)