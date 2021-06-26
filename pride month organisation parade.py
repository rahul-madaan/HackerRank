def changeTasks(tasks):
    maximum = max(tasks)
    minimum = min(tasks)
    priority = 1
    arr = [0] * len(tasks)
    for i in range(len(tasks)):
        index = tasks.index(min(tasks))
        element = tasks[index]
        arr[index] = priority
        tasks[index] = 999999
        if element not in tasks: priority = priority + 1
    print(arr)
    return arr

changeTasks([2,5,4,4])