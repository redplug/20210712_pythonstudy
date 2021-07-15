#-*- coding: utf-8 -*-

## 2주차는 2~3장 ##
## 2장 자료형 ##
# 자료형 
# 1. 문자열(string) : 문자, 단어등으로 구성된 문자들의 집합
# 2. 숫자(number) : 숫자 형태의 자료형으로 정수, 실수, 8진수, 16진수
# 3. 불형(bool) : True, False 두가지 형태가 있고 첫글자는 항상 대문자를 사용(예약어) -> 얘는 3장에 나옴
# 4. 기타 : 리스트, 튜플, 딕셔너리 등등 -> 얘는 4장부터 나옴.

# 1. 문자열 자료형
# - "" 또는 ''로 감싸서 만들 수 있다.
# - 이스케이프 문자를 사용할 수 있다
# - 문자열 연산자 : 연결, 반복, 인덱싱, 슬라이싱, 길이구하기

# 2. 숫자
# - 종류 : 정수, 실수
# - 연산자 : 사칙, 정수나누기, 나머지, 제곱
# - 우선순위, 문자열 연산자도 우선순위가 있다 -> 구분할 수있게 괄호를 쳐주자

# 3. 변수와 입력
# - 변수란? 값을 저장하는 공간(박스)
# - 복합 대입 연산자 += -= *= /= %= **/
# - 사용자의 입력을 받는 input()
# - 문자열을 숫자로 바꾸기 int()
# - 숫자를 문자로 바꾸기 str()
# - 문자열의 format() 함수
# - 대문자 upper(), 소문자 lower()
# - 양옆 공백제거 strip() lstrip() rstrip()
# - 문자열 구성 파악 isXX()
# - 문자열 찾기 find() rfind()
# - 문자열 in 연산자
# - 문자열 자르기 split()

## 3장 조건문 ##
# - 조건문이란? 주어진 조건의 결과에 따라 프로그램을 수행하는 코드
# - 조건문에는 if-elseif, switch있는데 파이썬에는 switch문이 없음 only if문
# - 조건에 만족/불만족을 구분하기 위해서 불 자료형을 사용함.
# - 불 만드는 방법 : 비교 연산자 == != < > <= >=
# - 불 만드는 방법 : 논리 연산자 not and or
# - if문 사용 방법
# if 불 값이 나오는 표현식:
#     불 값이 참일 떄 실행할 문장
#     불 값이 참일 떄 실행할 문장
# elif 불 값이 나오는 표현식:
#     elif 불 값이 참일 떄 실행할 문장
#     elif 불 값이 참일 떄 실행할 문장
# elif 불 값이 나오는 표현식:
#     elif 불 값이 참일 떄 실행할 문장
#     elif 불 값이 참일 떄 실행할 문장
# else:
#     위에 모든 조건을 만족하지 않았을 경우에 실행할 문장
# - 오전 오후를 구분하는 프로그램 (if만 활용)
# - 계절을 구분하는 프로그램 (if만 활용)
# - 계절을 구분하는 프로그램 (elif 활용)

## 추가 ##
# quit() -> 프로그램을 종료하는 방법 추가 : exit(), sys.exit(), os.exit()
# for test in range(10):     
#     if test == 5: 
#         print(quit) 
#         quit()
#     print(test)


## 배운걸로 간단 게임을 만들어보자
# 1. 제목은 퀴즈게임
# 2. 총 5번의 입력을 받는다.(게임 할지 여부1, 문제 4개)
# 3. 퀴즈의 정답 여부를 표기한다.
# 4. 퀴즈가 완료 후 맞힌 갯수와 정답율을 표기한다.


# 자료형을 확인하는 방법은 type() 함수를 활용 하는 것. 

## 자료형 확인 방법
print("문자 자료형 : ", type("테에에엑스트"))
print("숫자 자료형 : ", type(12345))
print("불 자료형 : ", type(True))
print("불 자료형 : ", type(['1']))

## 문자열 자료형 부터
## 문자열 자료형을 만들때는 "" 혹은 ''로 만든다
print("밥은 먹고 다니니?")
print('그럼 잘 먹고 다니지')

## 작은 혹은 큰 따옴표를 넣고 싶을 때 
print("'작은 따옴표를 넣을 떄' 이렇게 하세요 ")
print('"큰 따옴표를 넣을 때 " 이렇게 하세요')

## 이스케이프 문자 사용방법
## 이스케이프는 특수한 문자를 사용할때 사용하는 문자 \
print('\"큰 따옴표를 넣을 때\" 이렇게 하세요')
print('줄바꿈\n줄바꿈\n탭탭탭\t 탭탭탭 \\ \\ \\ \\ \\')

## 여러줄을 한번에 넣을 때
print("""\
가나다라마바사
아자차카타파하
아하하하하하하\
""")

##문자열 연산자
print("박지환" + "입니다.")
print("박지환" * 3)

## 문자열 인덱싱 -> 글자 하나하나 마다 번호를 매겨놓은거라고 보면 됩니다.

## 인덱스의 시작은 0부터 시작합니다. (중요함)
print("박지환"[0]) 
print("박지환"[1])
print("박지환"[2])

## -는 거꾸로 시작
print("박지환"[-1]) 
print("박지환"[-2])
print("박지환"[-3])

## 문자열 슬라이싱
print("박지환입니다\."[0:3])
print("박지환입니다."[1:4])
#print("박지환입니다."[10])
print("박지환입니다."[1:10])

## 문자열 길이 구하기
print(len("박지환입니다요오오오오오"))
#print(len(1234567890))

## 연습문제 2-1 ##
print("# 연습 문제")
print("\\\\\\\\")
print("-" * 8)

print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
#print("안녕하세요"[5])

print("안녕하세요"[1:3])
print("안녕하세요"[2:4])
print("안녕하세요"[1:])
print("안녕하세요"[:3])

## 숫자 자료형 ##
print(123)
print(123.123123)

print(type(123)) ## 정수
print(type(123.123123)) ## 실수

## 숫자 연산자
print("5 + 7 =", 5 + 7)
print("5 - 7 =", 5 - 7)
print("5 * 7 =", 5 * 7)
print("10 / 7 =", 5 / 7)
print("10 // 7 =", 10 // 7)
print("2 ** 1 =", 2 ** 1)
print("2 ** 2 =", 2 ** 2)
print("2 ** 3 =", 2 ** 3)
print("2 ** 4 =", 2 ** 4)

## 연산자 우선순위
print("(5 + 3) * 2 =", (5 + 3) * 2)
print("5 + (3 * 2) =", 5 + (3 * 2))

string = "문자열"
number = 273
#print(str + number)

## 연습문제 2-2 ##
print(" # 기본적인 연산")
print(15, "+", 4, "=", 15 + 4)
print(15, "-", 4, "=", 15 - 4)
print(15, "*", 4, "=", 15 * 4)
print(15, "/", 4, "=", 15 / 4)

print("3462를 17로 나뉘었을 떄의")
print("- 몫 :",3462 // 17)
print("- 나머지 :",3462 % 17)

print(2 + 2 - 2 * 2 / 2 * 2)
print(2 - 2 + 2 / 2 * 2 + 2)

## 변수와 입력
## 변수란? 값을 넣는 박스, 변수> 변하는 값
## 사용볍 : 변수를 선언 > 값을 넣고 > 참조
pi = 3.1459265
print(pi)

## 복합 대입 연산자
number = 100
print("number ", number)
number += 10
print("number ", number)
## number += 10 > number = number + 10 과 같다.

## 문자열도 동일하게 사용 가능함.
string = "안녕하세요"
print("string ", string)
string += "!!!"
print("string ", string)
## 반대로 쓰면???
# string =+ "!!!"
# print("string ", string)

## 사용자 입력받기 input
string = input("인사말을 입력하세요>")
print(string)
print(type(string))


## 문자열을 숫자로 int
string_a = input("입력A> ")
int_a = int(string_a)
print("string_a 타입 : ",type(string_a))
print("int_a 타입 : ",type(int_a))

output_a = int("52")
output_b = float("52.333")
print("output_a 타입", type(output_a))
print("output_b 타입", type(output_b))

## int인데 점을 붙이면?? Value Error
# output_a = int("52.1")

## 숫자를 문자열로
output_a = str(52)
output_b = str(52.333)

print(type(output_a), output_a)
print(type(output_b), output_b)

## 연습문제 2-3
str_input = input("<숫자입력> ")
num_input = float(str_input)
print()
print(num_input, "inch")
print((num_input * 2.54), "cm")

str_input = input("원의 반지름 입력> ")
num_input = float(str_input)
print()
print("반지름 : ", num_input)
print("둘레 : ", 2 * 3.14 * num_input) ## 둘레 : 반지름 * 2 * 3.14
print("넓이 : ", 3.14 * num_input ** 2) ## 넓이 : 반지름 * 반지름 * 3.14

a = input("문자열 입력> ")
b = input("문자열 입력> ")
## 안녕하세요 아침입니다.
print(a, b)
c = a
a = b
b = c
## 아침입니다 안녕하세요
print(a, b)

## 숫자와 문자열의 다양한 기능

## 문자열의 format() 함수
## 앞에 있는 중괄호 {}를 format함수의 매개변수로 교체 해주는 함수
## 중괄호와 매개변수의 갯수가 같거나 매개변수가 많아야함 중괄호가 많으면 에러.

string_a = "{}".format(10)
print(string_a)
string_a = "텍스트입니다. {} {}".format(10, 20)
print(string_a)
string_a = "텍스트 이지롱  {} {} {}".format(10, 20, 100)
print(string_a)
string_b = "{}".format(10)
print(string_b)
print(type(string_b))

## format 매개변수에 변수값을 집어넣어서 사용
a = "월급"
b = 500
string_a = "나는 {}을 {}만원 받고 싶습니다.".format(a, b)
print(string_a)

## But 3.6 버젼부터는 f-string라는 기능을 사용합니다. 전 이게 편해서 요 기능으로 씁니다~
a = "월급"
b = 1000
string_a = f"나는 {a}을 {b}만원 받고 싶습니다."
print(string_a)

##format02.py
# 정수
output_a="{:d}".format(52)

# 특정 칸에 출력하기
output_b="{:5d}".format(52)     # 5칸
output_c="{:10d}".format(52)    # 10칸

# 빈칸을 0으로 채우기
output_d="{:05d}".format(52)    # 양수
output_e="{:05d}".format(-52)   # 음수

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈 칸을 0으로 채우기")
print(output_d)
print(output_e)

## format03.py
# 기호와 함께 출력하기
output_f="{:+d}".format(52)     # 양수
output_g="{:+d}".format(-52)    # 음수
output_h="{: d}".format(52)     # 양수: 기호 부분 공백
output_i="{: d}".format(-52)    # 음수: 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

## format04.py 조합해 보기
# 조합하기
output_h="{:+5d}".format(52)     # 기호를 뒤로 밀기: 양수
output_i="{:+5d}".format(-52)    # 기호를 뒤로 밀기: 음수
output_j="{:=+5d}".format(52)    # 기호를 앞으로 밀기: 양수
output_k="{:=+5d}".format(-52)   # 기호를 앞으로 밀기: 음수
output_l="{:+05d}".format(52)    # 0으로 채우기: 양수
output_m="{:+05d}".format(-52)   # 0으로 채우기: 음수

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

## format05.py Float 자료형 기본
# 조합하기
output_a="{:f}".format(52.273)     
output_b="{:15f}".format(52.273)    # 15칸 만들기
output_c="{:+15f}".format(52.273)   # 15칸에 부호 추가하기
output_d="{:+015f}".format(52.273)  # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)

## format06.py 소수점 아래 자릿수 지정하기
output_a="{:15.3f}".format(52.273)     
output_b="{:15.2f}".format(52.273)    
output_c="{:15.1f}".format(52.273)   

print(output_a)
print(output_b)
print(output_c)

## format07.py 의미없는 소수점 제거하기
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)

## upper() lower() 대문자 소문자로 만드는 함수
a = "Hello World Python Programming!!"
print(a)
print(a.upper())
print(a.lower())

## 양 옆 공백 제거하는 함수 strip()
## 왼쪽 공백 제거 lstrip()
## 오른쪽 공백 제거 rstrip()
a = "    Hello World    "
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

## 문자열의 구성 파악 하기 : isOO()
## 요건 저도 처음 보네요!!
a = "hellworld"
print("알파벳 or 숫자 : ", a.isalnum())      ## 알파벳 또는 숫자
print("알파벳으로만   : ",a.isalpha())      ## 알파벳으로만
print("식별자        : ",a.isidentifier()) ## 식별자
print("문자열이 정수인지",a.isdecimal())    ## 문자열이 정수형태인지
print("문자열이 숫자로 인식되는지 : ",a.isdigit())      ## 문자열이 숫자로 인식될 수 있는지
print("공백만으로 구성되있는지 : ",a.isspace())      ## 공백으로만 구성되어있는지
print("소문자만 있는지 : ",a.islower())      ## 소문자만인지
print("대문자만 있는지 ",a.isupper())      ## 대문자만인지
## 각각 True 값을 가져올 수 있는 a값은?

## 왼쪽부터 처음 등장하는 위치 find()
## 오른쪽부터 처음 등장하는 위치 rfind()
a = "안녕안녕하세요".find("안녕")
print(a)

a = "안녕안녕하세요".rfind("안녕")
print(a)

## 문자열과 in 연산자
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

## 문자열 자르기 split() (리스트) 
a = "10 20 30 40 50".split(" ")
print(a)
print(a[0])

print("{}".format(52,273))



##### 3장 조건문 #####
## 불 자료형과 if 조건 문
## 불 자료형?? true false만 가지는 자료형
print(10 == 100)
print(10 == 10)
## = 와 == 는 다릅니다. = 는 변수에 값을 넣는 행위 == 는 앞뒤에 값이 같은지 확인하는 비교 연산자
## 비교 연산자를 통해서 불 자료형을 나타낼 수 있음.
## 논리 연산자 not(반대로) and(두개가 모두 참일 경우 true)  or (둘중에 하나만 참이라도 true)
a = 10
b = 20
print(a == 10 and b == 10)
print(a == 10 or b == 10)
print(not a == 10)

## if 조건문
## 조건에 따라 코드를 실행
## if문의 구성은 if, elif, else 3가지만 기억
a = 30
if a == 10:
    print("True입니다.")
elif a == 20:
    print("elif True 입니다.")
elif a == 30:
    print("elif True2 입니다.")
else:
    print("else 입니다.")
## 이어지는 구문은 띄어쓰기(4칸)으로 구분합니다.

## date02.py
# 날짜/시간과 관련된 기능을 가져옵니다.
# 모듈을 임포트 -> datetime 이라는 파일에 사전에 작성된 코드가 있고 그걸 가져다 쓰는 것.
import datetime

# 현재 날짜/시간을 구합니다.
# now 변수에 datetime이라는 모듈 -> datetime이라는 클래스 -> now()라는 매써드를 이용해서 현재 시간을 구해온다.
now = datetime.datetime.now()
print(now)
print(type(now))
print(now.hour)
# 오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

# 오후 구분
if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

## date03.py
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()
print(now)
print(now.hour)

# 봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

# 여름 구분
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

# 가을 구분
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

# 겨울 구분
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))


## condition05.py
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구하고
# 쉽게 사용할 수 있게 월을 변수에 저장합니다.
now = datetime.datetime.now()
month = now.month

# 조건문으로 계절을 확인합니다.
if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")



## 불 값은 True, False외에 다른값도 넣을 수 있으며, False로 변환되는 값 0, 0.0, 빈값, 그 외에는 True로 변환

## Pass = 아무것도 안하고 넘김, 나중에 짤때 씀

## raise NotImplementError : 미구현을 오류로 발생 시킴
number = 10
if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError
print("테에에스트")

## Speed Test: Switch vs If-Else-If http://www.blackwasp.co.uk/speedtestifelseswitch.aspx

## 연습문제 답은 뭘까요?#
x = 10
y = 2
if x > 4:
    if y > 2:
        print(x * y)    
else:
    print(x + y)

x = 11
if 10 < x < 20:
    print("조간이 맞습니다.")