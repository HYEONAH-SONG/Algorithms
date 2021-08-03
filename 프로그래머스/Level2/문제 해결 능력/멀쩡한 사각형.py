# 사용할 수 있는 정사각형의 갯수 구하기
# 문제의 창의적인 해결 능력을 보는 문제
def solution(w,h):
    all = w * h
    if w == h : # 가로와 세로의 길이가 동일한 경우
        substract = w
    elif w > h : # 가로가 더 긴 경우
        substract = h *2
    else: # 세로가 더 긴 경우
        substract = w * 2
    answer = all - substract
    return answer