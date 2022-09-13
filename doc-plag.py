import imghdr
import struct
#
# import docx2txt
#
# text = docx2txt.process("/Users/rahul.madan/PycharmProjects/HackerRank-and-leetcode/lab2.docx",
#                         '/Users/rahul.madan/PycharmProjects/HackerRank-and-leetcode/img/')
#

from collections import Counter
items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']
counts = Counter(items)

print(dict(counts))