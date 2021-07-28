# ["119", "97674223", "1195524421"]
# zip 활용하기
# 이중 for 문 절대 사용 x 
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p1 in p2[:len(p1)]:
            return False
    return True
phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
#
# def solution2(phone_book):
#     phone = {}
#     count = 0
#     for i in phone_book:
#         phone[i] = i
#     for i in phone:
#         for j in phone_book:
#             if i == j[:len(i)] :
#                 count +=1
#                 print(i)
#     if count ==len(phone_book):
#         return True
#     return False