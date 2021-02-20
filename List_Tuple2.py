# 문자열에서 모음 제거하기

str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
a =list(str)
c=['a','e','i','o','u']

def remove_vowels(a):
    return ''.join([x for x in a if x not in c])

print(remove_vowels(a))
