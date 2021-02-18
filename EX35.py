# 사용자 2명으로부터 가위, 바위, 보를 입력 받아 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성


def game(player,player2, score1, score2) :
    if (score1 == "가위" and score2 == "바위")or (score1 == "보" and score2 == "가위")or (score1 == "바위" and score2 == "보" ) :
        print(score2+"가 이겼습니다!")
    elif (score2 == "가위" and score1 == "바위")or(score2 == "보" and score1 == "가위")or (score2 == "바위" and score1 == "보" ) :
        print(score1+"가 이겼습니다!")
    else:
        print("비겼습니다!")


name_1 = input()
name_2 = input()
score_1 = input()
score_2 = input()
game(name_1, name_2,score_1, score_2)