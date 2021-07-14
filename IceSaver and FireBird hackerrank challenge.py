def warOrWin(number_of_army, wall_length, distance_army_wall, threshold_power, time, power_list, speed_list):
    pass


if __name__ == '__main__':
    number_of_army, wall_length, distance_army_wall, threshold_power, time, power_list, speed_list = 0, 0, 0, 0, 0, 0, 0
    test_cases = int(input("Enter number of test cases"))
    for i in range(test_cases):
        input_list = input("enter 1st line")
        input_list = input_list.split(" ")
        print(input_list)
        for j in range(len(input_list)):
            input_list[j] = int(input_list[j])
        print(input_list)
        power_list = input("Enter power list")
        power_list = power_list.split(" ")
        for j in range(len(power_list)):
            power_list[j] = int(power_list[j])
        print(power_list)
        speed_list = input("Enter power list")
        speed_list = speed_list.split(" ")
        for j in range(len(speed_list)):
            speed_list[j] = int(speed_list[j])
        print(speed_list)
        warOrWin(input_list[0], input_list[1], input_list[2], input_list[3], input_list[4], power_list, speed_list)

