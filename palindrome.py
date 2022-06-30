
s = []

n = int(input())
for i in range(n):
    s.append(input())




def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:]
    return mystring

def palindrome(word):
    fin = ''
    for i in word:
        fin = i + fin
    if fin == word:
        return(1)
    else:
        return(0)

for word in s:
    nopalin = 0
    flag = 1
    for i in range(len(word)):
        newword = insertChar(word, i, 'a')
        flag = palindrome(newword)
        if flag == 0:
            print('YES')
            print(newword)
            nopalin = 1
            break


    if nopalin == 0:
        print("NO")