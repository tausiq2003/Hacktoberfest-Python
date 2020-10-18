def soort(arr):
    low=0
    end=len(arr)-1
    mid=0
    while(mid<end):
        
    
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low=low+1
            mid=mid+1
        elif arr[mid]==1:
            mid=mid+1
        elif arr[mid]==2:
            arr[mid],arr[end]=arr[end],arr[mid]
            end=end-1

    return arr
arr=[1,1,0,2,1,0]
print(soort(arr))        