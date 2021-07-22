def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] # pivot element
   for j in range(low , high):
      # If current element is smaller
      if arr[j] <= pivot:
         # increment
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )
# sort
def quickSort(arr,low,high):
   if low < high:
      # index
      pi = partition(arr,low,high)
      # sort the partitions
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)
# main



def activityNotifications(expenditure, d):
    noti = 0
    for i in range(len(expenditure) - d):
        print(i)
        focus_expenditure = expenditure[i:i+d]
        print(focus_expenditure)
        quickSort(focus_expenditure, 0, d-1)
        mid = 0
        if d % 2 == 1:
            mid = focus_expenditure[(d // 2)]
        else:
            mid = (focus_expenditure[(d // 2)-1] + focus_expenditure[(d // 2)]) / 2

        # print(expenditure[d+i])
        if expenditure[d + i] >= mid * 2:
            noti = noti + 1

    print(noti)

    return noti


activityNotifications([10,20,30,40,50], 4)
