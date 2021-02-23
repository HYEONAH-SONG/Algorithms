# 임의의 url 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로 구분하는 프로그램을 작성

url = input()
url_1 = url.split('://')[0]
url_2 = url.split('://')[1].split('/')[0]
url_3 = url.split('://')[1].split('/')[1]
print("protocol: "+url_1)
print("host: "+url_2)
print("others: "+url_3)