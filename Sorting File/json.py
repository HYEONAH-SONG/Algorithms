
import re
from collections import OrderedDict
import string
left_word ='(s *SmartContract)'
right_word = '(APIstub shim.'
fun_list=[]
f = open("input.txt", 'r')

# sen = f.read()
# sen_list =re.split(r'[}:{]',sen)
# for index, i in enumerate(sen_list):
#     if 'func' and 'pb.Response' in i:
#         b= re.split(r'[):(]',i)
#         print(b[2])
#         for i in b:
#             fun_list.append(i[3])
# f.close()
sen = f.read()
sen_list =re.split(r'[}:{]',sen)
for index, i in enumerate(sen_list):
    if 'func ' in i:
        fun_list.append(i[1:])
print(fun_list)
