# 4-3 반복문과 while 반복문

# 범위 range

a = range(5)
print(a)
print(list(range(10))) # 0에서 10-1까지
print(list(range(5,10))) # 5에서 10-1까지
print(list(range(0,10,2))) # 0에서 2씩 증가해서 10-1까지

# for반목문을 활용하는 range for_range.py
# 리스트와 범위를 조합해서 사용하기 list_range01.py
# for 반복문 : 반대로 반복하기 reversed_for1.py reversed_for2.py

# while 반복문 : 무한히 반복할때 주로 사용함, while문의 조건이 false가 될때까지 실행함.
# while 불 표현식:
#     문장
# infinite_loop.py 
# while 반복문을 for 반복문처럼 사용하기 while_as_for.py
# while는 무한히 반복이 가능하나 for문은 불가능함.