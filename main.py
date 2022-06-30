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
num_range = maxi - mini

if num_range%buckets!=0:
    num_range = num_range + (buckets - (num_range%buckets))

bucket_size = num_range//buckets

bucket_split =[]
for i in range(buckets):
    bucket_split.append([])
# num_range -= 1

print(bucket_split)
print(mini - 1, mini + num_range, bucket_size)

for i in range(mini, mini + num_range, bucket_size):
    print(i,", ",end="")

zero_error = 0 - min(input_arr)

print("\n")

