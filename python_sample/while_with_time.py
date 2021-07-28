# 시간과 관련된 기능을 가져옵니다.
import time
import datetime
# 변수를 선언합니다.
number = 0
# print(time.time())
# epoch time: UTC(GMT+0) 기준으로 1970년 1월 1일 0시 0분 0초부터 경과시간(초)을 나타냄.
# print(datetime.datetime.today())

# 5초 동안 반복합니다.
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
    #print(number)

# 출력합니다.
print("5초 동안 {}번 반복했습니다.".format(number)) 
