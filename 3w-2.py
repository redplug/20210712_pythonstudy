# 4-2 딕셔너리와 반복문
# 딕셔너리? {} 중괄호로 선언하며 키:값(key:value) KV라고도하며, 키 값을 기반으로 값을 저장하는것
dict_a = {
    "name" : "어벤져스 엔드게임",
    "type" : "히어로 무비",
    "ing" : ["망고", "설탕", "색소"],
}
# 값에 접근할 때는 dic['key'] 값의 형태를 사용
# print(dict_a)
# print(dict_a["name"])
# print(dict_a["type"])
# # 값에 리스트가 들어가 있을 경우 이 역시도 인덱스로 뽑아낼 수 있음.
# print(dict_a["ing"][1])

dict_a["price"] = 5000
print('price 추가후 :',dict_a)
dict_a["price"] = 4000
print('price 변경후 :',dict_a)

del dict_a["price"]
print('price 삭제후 :',dict_a)

# print('에러 :',dict_a["key"])

# 키가 존재하는지 확인 하고 값에 접근하기 
# in 키워드 key_in.py
# get() 함수 get01.py
# for 반복문: 딕셔너리와 함께 사용하기 for_dict.py


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
# while 반복문:상태를 기반으로 반복하기 while_with_condition.py
# while 반복문: 시간을 기반으로 반복하기 while_with_time.py
# while 반복문 : break 키워드/continue키워드 
# break : 반복문을 아예 빠져나올때 사용 break.py 
# continume : 현재 순번의 반복문을 빠져나올때 사용  break01.py


# 4-4 문자열, 리스트, 딧셔너리와 관련된 기본 함수

# 리스트에 적용할 수 있는 기본 함수 : min(), max(), sum()
numbers = [1, 2, 3, 4, 5]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# reversed() 함수로 리스트 뒤집기
numbers = [1, 2, 3, 4, 5]

print(reversed(numbers))
print(list(reversed(numbers))) # 메모리 문제, next()로 하나씩 꺼내쓸 수 있음.
# reversed의 결과는 제네레이터로 값을 사용 후에는 기억하지 않음(소비한다?)
# https://niceman.tistory.com/137

# 확장슬라이스로 뒤집기
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])


# enumerate()함수와 반복문 조합
# 리스트에 인덱스 값을 포함하는 객체를 리턴 해줌
# enumerate.py

# 딕셔너리의 items() 함수와 반복문 조합 items.py

# 리스트 내포
# 반복문을 사용한 리스트 생성 for_list01.py -> 요걸 좀 더 단순하게 사용하기 위해 리스트 내포를 사용
# 리스트 안에 for문 사용하기 list_in.py
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]
# 조건을 활용한 리스트 내포 array_comprehensions.py
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결 string02.py string03.py (join)

# 이터레이터
# 반복할 수 있는것 -> 이터러블
# next()함수를 적용해 하나하나 꺼낼수 있는 요소 -> 이터레이터 iterator01.py
# -> 메모리 효율성