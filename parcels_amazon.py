parcels = [2, 3, 6, 10, 11]
k = 9
to_add = k - len(parcels)
addition = []

parcels.sort()


def find_index(arr, n, K):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == K:
            return mid
        elif arr[mid] < K:
            start = mid + 1
        else:
            end = mid - 1

    # Return the insert position
    return end + 1


pos = find_index(parcels,len(parcels), k)
sub_array = parcels[:pos]

for i in range(1,k):
    if i not in sub_array and (len(parcels)+len(addition)<k):
        addition.append(i)

print(sum(addition))
