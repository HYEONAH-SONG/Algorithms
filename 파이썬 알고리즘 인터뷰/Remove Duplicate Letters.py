# 중복 문자 제거
import collections
str = "bcabcz"
str = sorted(set(str))
print(''.join(str))

# 만약 핸재 문자가 스택에 쌓여 있ㅇ는 문자이고, 뒤에 다시 붙일 문자가 남아 있다면, 쌓아둔걸 없앤다.

def removeDuplicateLetters(s):
    counter, seen, stack =collections.Counter(s),set(),[]

    for key in s:
        counter[key]-=1
        if key in seen :
            continue # 중복 방지
        #뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and key<stack[-1] and counter[stack[-1]]>0:
            seen.remove(stack.pop())
        stack.append(key)
        seen.add(key)
    return ''.join(stack)

print(removeDuplicateLetters(str))