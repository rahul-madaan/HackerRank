from math import ceil

def convert(s: str, numRows: int) -> str:
    group_size = (2*numRows)-2

    # first and last layer out of the loop
    final_string = ""

    for x in range(int(ceil((len(s)/group_size )))):
        print(s[x*group_size])
        final_string += s[x*group_size]

    print(final_string)

    #loop for n-(n-1) to n-1 element(2nd to second last row)
    # n = numRows
    for x in range(int(len(s)/group_size )):





convert("ABCDEFGHIJKLMNOPQRST",4)