# 4-2 딕셔너리와 반복문
# 딕셔너리? {} 중괄호로 선언하며 키:값(key:value) KV라고도하며, 키 값을 기반으로 값을 저장하는것
dict_a = {
    "name" : "어벤져스 엔드게임",
    "type" : "히어로 무비",
    "ing" : ["망고", "설탕", "색소"],
}
# 값에 접근할 때는 dic['key'] 값의 형태를 사용
print(dict_a)
print(dict_a["name"])
print(dict_a["type"])
# 값에 리스트가 들어가 있을 경우 이 역시도 인덱스로 뽑아낼 수 있음.
print(dict_a["ing"][1])

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