#-*- coding: utf-8 -*-
# 함수 만들기

### 챕터 6 예외 처리 ###
## 06-1 : 구문 요류와 예외 ##

# 구문 오류 - SYntaxError -> 실행 전에 발생하는 오류
print("aaa)
# 구문오류는 오류난 부분을 확인해서 수정하면됩니다.

# 예외 - Exception or 런타임 오류 runtime error -> 실행 중에 발생하는 오류
print("프로그램 시작")
list_a[1]
# 예외는 구문오류와 같이 오류난 부분을 수정하고나, 해당 부분을 예외처리 하는 방법으로 해결함. -> 예외처리
# 예외처리 방법은
# 1. 조건문을 사용하는 방법 -> 우리가 앞서 계속 오류가 안나도록 해오던 방법, 간단한 상황에서 사용
# 2. try except 구문을 사용하는 방법

# 1. 조건문을 사용하는 방법 
# > 2주차 퀴즈 : 게임 종료에 대한 if문
# > 3주차 주차 : 숫자 입력에 대한 if문

# 2. try except 구문을 사용하는 방법
try:
    # 예외가 발생할 가능성이 있는 코드
    # 오류가 날것만 같은 코드들을 여기에 기입
except:
    # 예외가 발생했을 때 실행할 코드    
else:
    # 예외가 발생하지 않았을 때 실행할 코드
finally:
    # 무조건 실행할 코드
    # try에서 열었던 파일을 닫는다던가 등등

# 예제 try_except_else_finally.py

# 능한 조합
# try + except
# try + except + else
# try + except + finally
# try + except + else + finally
# try + finally

# 함수 작성 시 try문에 break, return 값을 넣을 경우 빠져나올때 finally를 실행함.



## 06-2 : 예외 고급 ##

# 예외 객체
# 예외가 발생했을 때 예외에 관련된 정보가 저장되는 객체 -> 예외 객체
# try except 구문을 사용할 때 예외를 구분하고 각 예외마다 다른 처리가 가능하다.
# 각 예외들에는 exception 객체를 사용하여 활용이 가능하다.
# except로 정의하지 못한 모든 예외를 처리하고 싶을 떄는 Exception을 넣어서 처리한다.
# except_all.py -> 1입력

# raise 구문
# 일부러 강제종료를 발생 시킬때 사용하는 구문
# 나중에 까먹을까봐 만들어 놓는 코드 
# NotImplementedError은 미리 구현된 클래스고 다른 예외를 만들고 싶다면 별도의 예외 클래스를 만들어야됨.


