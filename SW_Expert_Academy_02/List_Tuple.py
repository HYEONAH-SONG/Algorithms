# 한 학생의 국어, 수학 점수를 튜플로 저장하고 이 튜플을 항목으로 갖는 리스트 객체가 있다
# 이 때 첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)의 점수를 갖는다.

student1 = (90,80)
student2 = (85,75)
student3 = (90,100)

s = [student1,student2,student3]

def check(student) :
    for info in enumerate(student) :
        sum =0
        for score in info[1]:
            sum =sum + score
            average =sum/2.0
        print("{}번 학생의 총점은 {}이고, 평균은 {}입니다.".format(info[0]+1,sum, average))

check(s)
