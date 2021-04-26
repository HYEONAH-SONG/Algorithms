
import re
from collections import OrderedDict
import string
left_word ='(s *SmartContract)'
right_word = '(APIstub shim.'
fun_list=[]
f = open("input.txt", 'r')
list_name =[]
sen = f.read()
sen_list =re.split(r'[}:{]',sen)
for index, i in enumerate(sen_list):
    if 'func 'in i:
        b= re.split(r'[(:)]',i)
        if len(b)==5:
            list_name.append(b[2])
        else:
            m = b[0].split(' ')[1]
            list_name.append(m)
print(list_name)
f.close()
# sen = f.read()
# sen_list =re.split(r'[}:{]',sen)
# for index, i in enumerate(sen_list):
#     if 'func ' in i:
#         fun_list.append(i)
#         print(i)
print(fun_list)
