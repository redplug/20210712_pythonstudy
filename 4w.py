
#-*- coding: utf-8 -*-
# 숫자 맞추기 퀴즈 풀이

### 챕터 05 - 함수 ###
## 05-1 함수 만들기 ##
# 함수? 입력으로 어떤값(매개변수)를 넣으면 내부에서 처리하고 최종 결과값(리턴)을 출력하는 해주는 친구.
# 실제 사용(호출)할 때는 함수내부는 어떤구조로 되어있는지는 알 필요가 없음 -> 입력 값을 넣으면 '내가 원하는 값(리턴)'을 준다만 알면됨.

# 함수를 사용하는 방법 (2단계)
# 1. 함수를 선언(def)
# 2. 함수를 사용(호출) 

# 함수 사용방법 예시
# 1. '함수'를 선언한다
def 함수이름():
    #처리할 문장이 들어가야 함
    print("처음만들어보는 함수!!!")

# 2. 함수를 사용(호출)한다.
함수이름()

# 함수는 매개변수라는 걸 받을 수 있음 () 안에 들어가는건 모두 매개변수라고 보면 됨.
def 함수이름(매개변수1, 매개변수2, 매개변수3):
    print(매개변수1)
    print(매개변수2)
    print(매개변수3)

변수1 = "매개변수1를 넣어보자"
변수2 = "매개변수2를 넣어보자"
변수3 = "매개변수3를 넣어보자"
함수이름(변수1,변수2,변수3)

# 힘수는 입력 값(매개변수) 라는걸 받을 수가 있음
# 매개변수 종류 (4가지)

# - 일반 매개변수 : 변수로 입력 받은 값을 그대로 쓰는 케이스, 사용법 : 매개변수명
# def 함수명(매개변수명, 매개변수명, 매개변수명)

# - 가변 매개변수 : 길이가 제한이 없는 케이스, 사용법 : *매개변수명, 함수내에서 사용 시 리스트 형태로 사용
# def 함수명(*매개변수명)
# print("당신은", "우리와", "함께할 수", "없습니다.")


# - 기본 매개변수 : 함수 호출 시 매개변수를 안넣었을 때 기본으로 들어가는 값 말그대로 '기본 값', 사용법 : 매개변수명=기본값
# def 함수명(매개변수명=값)

# - 키워드 매개변수 : 사용(호출)시에 매개변수명을 직접 입력하여 사용하는 케이스
def 함수명(aaa, bbb, ccc):
  함수내부 블라블라~
# 함수명(bbb=2,aaa=1,ccc=3) // 함수 호출 시 매개변수명을 입력

# 리턴 설명
# 위에서 얘기한 함수 -> 입력으로 어떤값(매개변수)를 넣으면 내부 적으로 처리하고 최종 결과값(리턴)을 출력하는것
# 결과값을 출력 = 리턴(return) => 리턴을 만난다 = 함수를 종료한다

def 리턴함수(매개변수):
    매개변수 = 매개변수 + 1    
    return 매개변수

입력값 = 1
리턴값 = 리턴함수(입력값)
print(리턴값)

# 결과값을 받고 싶지 않다 => return
# 결과값을 받고 싶다 => return 리턴 할 값

# 문제풀이 : 05-1 2번 (p227)
# 문제 내용 : 입력받은 숫자를 모두 곱하는 함수를 만들고 곱한값을 리턴, 값을 출력해라
def mul(*values):
    ### 작성 코드(시작) ###
    sum = 1
    for value in values:
        sum *= value        
    return sum
    ### 작성 코드(끝) ###
print(mul(5,7,9,10))



## 05-2 함수의 활용 ##

# 재귀함수 : 자기 자신을 호출하는 함수(파이썬에서는 1000번까지 호출 가능), 상황에 따라 기하급수적으로 많이 반복한다는 문제가 있음
# 재귀 씀 -> 반복이 늘어남 -> 코드가 작동시간이 기하급수로 늘어남 -> 야근을 하게됨 -> 매우 기분 나빠짐. -> 자주쓰면 분노 함.
# 메모화 : 재귀함수를 해결하는 방법, 재귀함수로 호출했던 값을 딕셔너리에 저장해서 또 호출하지 않게함. -> 기억하고 있다가 재귀함수 쓸일이 있을 때 사용.

#### 재귀함수 뎁스 체크(시작) ####
# 1000줄에서 멈춤
aaa = 1
def factorial_test(count):
    if count == 0:
        return
    print("몇번째 재귀?", count)    
    count += 1
    factorial_test(count)
factorial_test(5)
#### 재귀함수 뎁스 체크(끝) ####

# global 설명
# 변수는 전역변수와 지역변수로 나뉘어 짐.
# 전역변수 : 함수 밖에서 선언되는 변수로, 코드 전체에서 사용하는 변수, 함수 내 에서는 수정이 불가함-> 수정하려면 global 사용.
# 함수 내에서 전역변수와 동일한 변수명을 선언한 경우 전역변수 사용 불가, 선언하지 않으면 읽기전용(?)으로 사용 가능함.
# 지역변수 : 함수 안에서 선언되는 변수로, 함수 내에서만 사용하는 변수
# global 키워드 : 함수 내에서 전역변수를 수정하여 사용하기 위해서 사용하는 키워드. 사용법 : 함수 내에서 'global 사용하고자하는전역변수명'

# 조기 리턴 : 코드를 좀더 간결하게 사용하기 위해서 return값을 활용 하는 것, 필수X, 하면 좋음.

# 문제풀이 : 05-2 1번 (p243)
# 문제내용 : 리스트 평탄화, 중첩리스트를 풀어 1차 리스트를 만드는 것.

def flatten(data):
    ### 코드 작성(시작) ###    
    output = []    
    for data_list in data:
        if type(data_list) == list:
            output += flatten(data_list) # 리스트 끼리 더하면 하나의 리스트가 됨
        else:            
            output.append(data_list)
    return output
    ### 코드 작성(끝) ###
example = [[1,2,3],[4,[5,6]],7, [8,9]]
print("원본", example)
print("변환", flatten(example))

# 문제풀이 : 05-2 2번 (p244)
# 문제내용 : 패밀리 레스토랑 문제
# https://jooonho.com/algorithm/2020-03-08-makeGroup/

앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람의수 = 6
memo = {}

def 문제(남은사람수, 앉힌사람수):
    key = str([남은사람수, 앉힌사람수])
    # 종료 조건
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:        
        return 0 # 무효이므로 0을 리턴        
    if 남은사람수 == 0:
        return 1 # 유효하므로 수를 세기 위해 1을 리턴
    # 재귀 처리
    count = 0
    for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1):
        count +=  문제(남은사람수 - i, i)
    # 메모화 처리
    memo[key] = count
    # 종료
    return count

print(문제(전체사람의수, 앉힐수있는최소사람수))
   


## 05-3 함수 고급 ##

# 튜플?
# 리스트와 비슷, 한번 결정된 요소는 바꿀 수 없다
# 요소를 하나만 가지는 튜플은 ','를 넣어줘야 한다.
# 튜플은 리스트와 달리 괄호가 없이도 사용이 가능하다.
# 함수에서 여러개의 값을 리턴할때 튜플을 사용한다.


# 람다?
# 함수를 간단하고 쉽게 선언하는 방법 (따로적기 귀찮으니까...)
# 람다는 익명함수(이름없는) 함수라고도 합니다.(쓰고 버림)
# 쓰는이유? 코드 간결(리턴 안씀, 한줄) + 메모리 절약(쓰고버림)
# 사용법 : lambda 매개변수: 리턴값

# 기존 함수 선언
def power(item):
    return item * item
print(power(3))

# 람다 3줄 -> 1줄로 끝! / 정의와 바로 사용할 수 도 있음.
print((lambda x: x * x)(3))



# 파일처리 : 파일 관련된 처리를 하는 표준 함수

# 파일 열기 및 닫기 
# 사용법 : 
# 파일객체 = open("파일경로", "모드")
# 파일객체.close

# 쓰기모드 'w'
file = open("textfile.txt","w")
file.write("Hello Python Programing...!")
file.close()

# 읽기모드 'r'
file = open("textfile.txt","r")
contents = file.read()
file.close()
print(contents)

# 파일을 open하면 꼭 close를 해줄 것. -> with 키워드

# with 키워드 : 파일을 닫을 때 사용하는 키워드, with 내 구문이 끝나면 자동으로 파일이 닫힘.
# 사용법 : 
with open("textfile.txt", "w") as file:
    file.write("Hello Python Program!!")
print(aaaa)

## with구문이 끝나면 열었던 파일이 닫힘.


# 파일을 읽을 때 한줄씩 읽어드리는 방법은 for 반복문을 사용한다

# 파일을 기록
with open("textfile.txt", "w") as file:
    file.write("Hello Python Program 11\n")
    file.write("Hello Python Program 22")

# 파일을 읽고 한줄씩 읽어드린다.
file = open("textfile.txt","r")
for line in file:    
    print(a)
file.close()

a= "야이노무아야아야앙"
print(a[0])

# 제네레이터?
# 파이썬의 특수한 문법구조로 이터레이터를 직접 만들때 사용하는 코드
# 이터레이터? 리스트, 딕셔너리,튜플과 같이 하나씩 꺼내서 처리가 가능한 객체들
# 제네네이터는 함수를 조금씩 실행할때 사용, 필요할때만 꺼내쓸수 있음.

# 사용법 : 
# 함수안에 yield 키워들 사용 -> 리턴값이라고 보면 됨.

def number_generator():
    x = 1
    yield x   # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    x += 1
    yield x   # 1을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    y = 1    
    yield y    # 2를 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
 
g = number_generator()
 
a = next(g)    # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나옴
print(a)       # 0
 
b = next(g)
print(b)       # 1
 
c = next(g)
print(c)       # 2