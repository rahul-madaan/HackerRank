def max_days(a):
    a = sorted(a)
    is_odd = len(a)%2
    final = a[:len(a)//2]
    final_len = len(final)
    rem = a[(len(a)//2):]

    for i in range(0,len(a),2):
        final.insert(i,rem[0])
        rem.pop(0)

    if is_odd ==1:
        print(final_len)
    else:
        print(final_len-1)
    for ele in final:
        print(ele, end =" ")


a = input()
a = input()
a = a.split(" ")

a = list(map(int, a))

max_days(a)
