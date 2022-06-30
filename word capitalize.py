def cap(a):
    letters = [char for char in a]
    letters[0] = str.upper(letters[0])
    a = ""
    for letter in letters:
        a += letter
    return a


sentence = input()
print(cap(sentence))
