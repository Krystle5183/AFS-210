import time
import random

def quick_sort(a_list, start, end):
  
    if start >= end:
        return
    
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        
def partitionStart(a_list, start, end):
    return partition(a_list, start, end)
  
def partitionMiddle(a_list, start, end):
    a_list[start], a_list[len(a_list)//2] = a_list[len(a_list)//2], a_list[start]
    return partition(a_list, start, end)

def partitionEnd(a_list, start, end):
    a_list[start], a_list[end] = a_list[end], a_list[start]
    return partition(a_list, start, end)

def partitionRandom(a_list, start, end):
    a_list[start], a_list[random.randint(0, end) ] = a_list[random.randint(0, end)], a_list[start]
    return partition(a_list, start, end)

def partition(a_list, start, end):
    
    pivot = a_list[start]
    
    low = start + 1
    high = end
    
    while True:
        
        while low <= high and a_list[high] >= pivot:
            high = high - 1
       
        while low <= high and a_list[low] <= pivot:
            low = low + 1
        
        if low <= high:
            
            a_list[low], a_list[high] = a_list[high], a_list[low]
            
        else:
           
            break
    
    a_list[start], a_list[high] = a_list[high], a_list[start]
    
    return high
  

print("Quick Sort:")
#myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

#print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
#print()
#print("Sorted Listed: ")
#print(myList)   

print(f"The execution time is: {end_time-start_time}")
