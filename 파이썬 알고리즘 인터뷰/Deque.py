from collections import deque

def palindrome(word):
    dq = deque(word)
    while len(dq) >1 :
     if dq.popleft() != dq.pop():
         return False
    return True

def palindrome2(word):
    return word == word[::-1]
