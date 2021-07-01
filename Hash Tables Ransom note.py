from collections import Counter

def checkMagazine(magazine, note):
    # for element in note:
    #     flag=0
    #     for i in range(len(magazine)):
    #         if element == magazine[i]:
    #             magazine.pop(i)
    #             flag=1
    #             break
    #     if flag==0:
    #         print("No")
    #         return "No"
    # print("Yes")
    # return"Yes"


    if(Counter(note) - Counter(magazine) == {}):
        return "Yes"
    else: return "No"




checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'], ['two', 'times', 'two', 'is', 'four'])