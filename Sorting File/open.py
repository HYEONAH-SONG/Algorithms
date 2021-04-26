from django.shortcuts import render
from .models import UploadFileModel
from django.http import JsonResponse
import sys
import math
import json

cnt = 1
fileName_Num = 1
num_list = [1]
info_list = []
whole_fun_list = []
func_cnt = 0


# Create your views here.

# upload.html 출력
def upload(request):
    return render(request, 'upload.html')


# 파일 업로드하면 /media 폴더내에 파일 업로드
def upload_file(request):
    uploadfile = UploadFileModel()
    uploadfile.func_file = request.FILES['func_file']
    print(uploadfile)
    uploadfile.save()

    # web을 통해 받은 file 열기
    f = open("media/input.txt", 'r')
    lines = f.readlines()
    f.close()

    global fileName_Num
    global cnt
    global num_list
    global info_list
    global whole_fun_list
    global func_cnt

    word = 'func '
    for index, line in enumerate(lines):
        if index < len(lines) - 1:

            fileName = 'function' + str(fileName_Num) + '.txt'

            fw = open(fileName, "a")
            fw.write(line)
            fw.close()

            if word in lines[index + 1]:
                fileName_Num = fileName_Num + 1
                num_list.append(fileName_Num)
                cnt = 0
            cnt += 1

    for i in num_list:
        fileName = 'function' + str(i) + '.txt'
        func_cnt = func_cnt + 1
        fw = open(fileName, "r")
        print("function", i)
        fun_weight(fw)
        info_list.append(i)
        whole_fun_list.append(info_list)
        info_list = []
        fw.close()

    print(whole_fun_list)
    transaction_sorted = sorted(whole_fun_list, key=lambda x: (x[3], x[2], x[1], x[0]))

    print(transaction_sorted)

    # 토탈 코스트 : transaction_sorted[i][3]
    # 코드 라인 : transaction_sorted[i][0]
    # 반복문 수 : transaction_sorted[i][1]
    # 데이터 처리 비용: transaction_sorted[i][2]

    # 인덱스 파일 생성
    dict_index = {'cost': {'function': {'code_line_cost': '', 'control_statement_cost': '', 'data_process_cost': ''}}}
    code_line_cost = "code_line_cost"
    control_statement_cost = "control_statement_cost"
    data_process_cost = "data_process_cost"

    index_cost = {'function': {'code_line_cost': '', 'control_statement_cost': '',
                               'data_process_cost': ''}}  # cost 다를 때, 키 cost의 value값 초기화해주기 위해
    index_func = {'code_line_cost': '', 'control_statement_cost': '',
                  'data_process_cost': ''}  # cost같을 때, 키 func의 value값 초기화해주기 위해

    for i in range(1, func_cnt + 1):
        str_total_cost = str(transaction_sorted[i - 1][3])
        str_code_line = str(transaction_sorted[i - 1][0])
        str_iteration = str(transaction_sorted[i - 1][1])
        str_data = str(transaction_sorted[i - 1][2])
        str_function_cnt = str(i)

        chg_func_cnt = "function" + str_function_cnt  # 함수 이름
        chg_str_total_cost = "cost" + str_total_cost

        if (i == 1):

            chg_str_total_cost = "cost" + str_total_cost

            dict_index[chg_str_total_cost] = dict_index.pop('cost')
            dict_index[chg_str_total_cost][chg_func_cnt] = dict_index[chg_str_total_cost].pop('function')

            dict_index[chg_str_total_cost][chg_func_cnt][code_line_cost] = str_code_line
            dict_index[chg_str_total_cost][chg_func_cnt][control_statement_cost] = str_iteration
            dict_index[chg_str_total_cost][chg_func_cnt][data_process_cost] = str_data

        else:
            previous_total_cost = transaction_sorted[i - 2][3]  # 이전 cost와 비교하기 위해
            if transaction_sorted[i - 1][3] == previous_total_cost:  # 이전 cost와 같을 때

                chg_str_total_cost = "cost" + str_total_cost
                dict_index[chg_str_total_cost][chg_func_cnt] = index_func  # 새로운 func 키를 생성

                dict_index[chg_str_total_cost][chg_func_cnt][code_line_cost] = str_code_line
                dict_index[chg_str_total_cost][chg_func_cnt][control_statement_cost] = str_iteration
                dict_index[chg_str_total_cost][chg_func_cnt][data_process_cost] = str_data

            else:  # 이전 cost와 다를 때
                dict_index[chg_str_total_cost] = index_cost

                dict_index[chg_str_total_cost][chg_func_cnt] = dict_index[chg_str_total_cost].pop('function')
                dict_index[chg_str_total_cost][chg_func_cnt][code_line_cost] = str_code_line
                dict_index[chg_str_total_cost][chg_func_cnt][control_statement_cost] = str_iteration
                dict_index[chg_str_total_cost][chg_func_cnt][data_process_cost] = str_data

        print("i: ", i)
        print(dict_index)

    json_index = json.dumps(dict_index, indent=4)
    print(json_index)

    return 0
    # return JsonResponse({
    #                         json_index
    #                     }, safe=False)

    # return render(request, 'show.html',{'code_line1': whole_fun_list[0][0], 'iteration1':whole_fun_list[0][1] , 'data_cost1': whole_fun_list[0][2], 'total_cost1': whole_fun_list[0][3],'code_line2': whole_fun_list[1][0], 'iteration2':whole_fun_list[1][1] , 'data_cost2': whole_fun_list[1][2], 'total_cost2':whole_fun_list[1][3] ,'code_line3':whole_fun_list[2][0] , 'iteration3': whole_fun_list[2][1], 'data_cost3': whole_fun_list[2][2], 'total_cost3':whole_fun_list[2][3],'first_fun':transaction_sorted[0][4], 'second_fun':transaction_sorted[1][4], 'third_fun':transaction_sorted[2][4], 'sorted_first_line':transaction_sorted[2][0],'sorted_first_iteration':transaction_sorted[2][1],'sorted_first_data':transaction_sorted[2][2], 'sorted_first_total':transaction_sorted[2][3],'sorted_second_line':transaction_sorted[1][0],'sorted_second_iteration':transaction_sorted[1][1],'sorted_second_data':transaction_sorted[1][2], 'sorted_second_total':transaction_sorted[1][3],'sorted_third_line':transaction_sorted[0][0],'sorted_third_iteration':transaction_sorted[0][1],'sorted_third_data':transaction_sorted[0][2], 'sorted_third_total':transaction_sorted[0][3]})


def fun_weight(code):
    # initialized variables
    total, weight = 0, 0
    count_line = 0
    if_count, for_count, while_count, switch_count = 0, 0, 0, 0
    G, P, M, U = 0, 0, 0, 0

    code_list = list(enumerate(code))
    count_line = code_list[-1][0] + 1
    print('코드의 라인 수 :', count_line)
    word1, word2, word3, word4 = 'if', 'for', 'while', 'switch'
    data1, data2, data3, data4 = 'GetState', 'PutState', 'Marshal', 'Unmarshal'

    # count variable cost
    for i in code_list:
        if word1 in i[1]:
            if_count += 1
        elif word2 in i[1]:
            for_count += 1
        elif word3 in i[1]:
            while_count += 1
        elif word4 in i[1]:
            switch_count += 1
        elif data1 in i[1]:
            G += 1
        elif data2 in i[1]:
            P += 1
        elif data3 in i[1]:
            M += 1
        elif data4 in i[1]:
            U += 1

    code_line_cost = math.ceil(count_line / 50)
    iteration_cost = if_count + for_count + switch_count + while_count
    data_cost = G + P + M + U
    total = code_line_cost + iteration_cost + data_cost
    # weight = code_line_cost + iteration_cost*2 + data_cost*3

    # output printing
    print('if문의 수 :', if_count)
    print('for문의 수 :', for_count)
    print('while문의 수 :', while_count)
    print('switch문의 수 :', switch_count)
    print('GetState:', G)
    print('PutState:', P)
    print('Marshal:', M)
    print('Unmarshal:', U)
    print('Total Execution Cost :', total)
    print('—————————————————————————')

    info_list.append(code_line_cost)
    info_list.append(iteration_cost)
    info_list.append(data_cost)
    info_list.append(total)

    return total