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

a_list = [x for x in range(1000)]
random.shuffle(a_list)

start_time = time.time()
quick_sort(a_list,0,len(a_list)-1)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")

def quick_sort(a_list, start, end):
    if start >= end:
        return
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
    

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)
  

def partition(a_list, start, end):
    pivot = a_list[random.randrange(start, end)]
    
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
myList = [x for x in range(1000)]
random.shuffle(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")
