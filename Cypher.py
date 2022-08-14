# https://codeforces.com/problemset/problem/1703/C

'''
3
3
9 3 1
3 DDD
4 UDUU
2 DU
2
0 9
9 DDDDDDDDD
9 UUUUUUUUU
5
0 5 9 8 3
10 UUUUUUUUUU
3 UUD
8 UUDUUDDD
10 UUDUUDUDDU
4 UUUU
'''

def get_original(new_number,movement_list):
    for move in movement_list:
        if move == "D" and new_number<9:
            new_number += 1
        elif move == "D" and new_number==9:
            new_number = 0
        elif move == "U" and new_number>0:
            new_number -= 1
        elif move == "U" and new_number==0:
            new_number =9

    return new_number


n = int(input())
for i in range(n):
    no_of_wheels = int(input())
    initial_wheel_values = [int(i) for i in input().split(" ")]
    # print(initial_wheel_values)
    for i in range(no_of_wheels):
        movement = [char for char in input().split(" ")[1]]
        # print(movement)
        original_number = get_original(initial_wheel_values[i],movement)
        print(original_number, end=" ")
    print("")



