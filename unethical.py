buckets = int(input().strip().split(" ")[1])

input_arr = input().strip().split()
for i in range(len(input_arr)):
    input_arr[i] = int(input_arr[i])

maxi = -9999999999999
mini = 9999999999999

for i in range(len(input_arr)):
    if input_arr[i] < mini:
        mini = input_arr[i]
    if input_arr[i] > maxi:
        maxi = input_arr[i]

num_range = maxi-mini

if num_range%buckets!=0:
    num_range = num_range + (buckets - (num_range%buckets))
bucket_size = num_range//buckets

bucket_split =[]
for i in range(buckets):
    bucket_split.append([])


zero_error = 0 - mini

for i in range(len(input_arr)):
    try:
        bucket_split[(input_arr[i]+zero_error)//bucket_size].append(input_arr[i])
    except:
        bucket_split[((input_arr[i] + zero_error) // bucket_size)-1].append(input_arr[i])

for i in range(len(bucket_split)):
    bucket_split[i] = sorted(bucket_split[i])

for i in range(len(bucket_split)):
    print(len(bucket_split[i]),end=" ")
    for j in range(len(bucket_split[i])):
        print(bucket_split[i][j],end=" ")
    print("")

