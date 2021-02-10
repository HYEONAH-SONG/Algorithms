<<<<<<< HEAD
# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

blood=['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']  # array 정의

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

for i in range(len(blood)):
    if blood[i] == 'A':
        cnt1 = cnt1 + 1
    elif blood[i] == 'B':
        cnt2 = cnt2 + 1
    elif blood[i] == 'AB':
        cnt3 = cnt3 + 1
    else:
        cnt4 = cnt4 + 1

print("{\'A\': " + str(cnt1) +", \'O\': " + str(cnt4)+ ", \'B\': "+ str(cnt2)+ ", \'AB\': " +str(cnt3)+ "}")
=======
# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

blood=['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']  # array 정의

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

for i in range(len(blood)):
    if blood[i] == 'A':
        cnt1 = cnt1 + 1
    elif blood[i] == 'B':
        cnt2 = cnt2 + 1
    elif blood[i] == 'AB':
        cnt3 = cnt3 + 1
    else:
        cnt4 = cnt4 + 1

print("{\'A\': " + str(cnt1) +", \'O\': " + str(cnt4)+ ", \'B\': "+ str(cnt2)+ ", \'AB\': " +str(cnt3)+ "}")
>>>>>>> 1c8508b (commit3)
