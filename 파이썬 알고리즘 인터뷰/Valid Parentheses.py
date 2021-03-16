arr = "()[{}[]"
# arr2 = "((())))("
# check1 = []
# check2 = []
# check3 = []
# isTrue = "False"
# for i in arr2:
#     if i == "(":
#         check1.append(i)
#     elif check1 and i == ")":
#         check1.pop()
#     elif i == "[":
#         check2.append(i)
#     elif check2 and i=="]":
#         check2.pop()
#     elif i == "{":
#         check3.append(i)
#     elif check3 and i=="}":
#         check3.pop()
#     else:
#         break
# else:
#     if not check1 and not check3 and not check2:
#         isTrue = "True"
# print(isTrue)

def isValid (str):
    stack = []
    table  = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    # 스택 이용 예외 처리 및 일치 여부 판별

    for s in str :
        if s not in table: # (, {, [
            stack.append(s)
        elif not stack or table[s] != stack.pop():
            return False
    return  len(stack) == 0
