import os
import glob
import docx2txt



docx_file_list = glob.glob("submissions/*.docx")

docx_file_list = [i[12:] for i in docx_file_list]

print(docx_file_list)


for i in docx_file_list:
    os.rename("submissions/"+i,"submissions/"+i[15:20]+".docx")

docx_file_list = glob.glob("submissions/*.docx")

docx_file_list = [i[12:] for i in docx_file_list]


print(docx_file_list)
#
# for i in docx_file_list:
#     os.mkdir("/Users/rahul.madan/PycharmProjects/HackerRank-and-leetcode/submissions/img/"+i[:5])
#     _ = docx2txt.process("/Users/rahul.madan/PycharmProjects/HackerRank-and-leetcode/submissions/"+i,
#                             '/Users/rahul.madan/PycharmProjects/HackerRank-and-leetcode/submissions/img/'+i[:5])
#
