def printc(text):
    print("\033[33m" + text + "\033[0m")

# 3주차 파이썬

# 0-1 quit 풀이시간
# 0-2 실수와 정수를 구분하는 이유
# print(0.1 + 0.1 + 0.1 == 0.3)
# print(0.1 + 0.1 + 0.1)
# print(0.3)
# print(0.1)
# print('%0.400f' % 0.1)
# print("")
# print("")
# print("")
# print("")

# 컴퓨터는 2진수를 사용 -> 0.1과 같은 소수점을 이진수로 표현할 경우 무한히 반복되는 실수가 됨.
# 0.1=0.00011001100110011001100110011001100110011001100110011001100110011⋯(2)
# 메모리가 크기가 제한되나 저걸 전체를 표현할 수 없으니 특정소수점 이하는 생략하고 가장 비슷한 숫자로 저장됨.

# 0.1≈0.1000000000000000055511151231257827021181583404541015625
# 따라서 실수를 비교할 경우에는 round를 써서 소수점 자리수를 제한한 후에 반올림 하여 계산
# print(round(0.1 + 0.1 + 0.1, 5) == round(0.3, 5))
# 
# import math, sys
# x = 0.1 + 0.1 + 0.1
# print(math.fabs(x - 0.3) <= sys.float_info.epsilon) ## 오차 범위를 계산하여 epsion보다 작을 경우 True

# 3.5 이상부터는 isclose를 사용
# import math
# print(math.isclose(0.1 + 0.1 + 0.1, 0.3))



# https://datascienceschool.net/01%20python/02.02%20%EB%B6%80%EB%8F%99%EC%86%8C%EC%88%98%EC%A0%90%20%EC%8B%A4%EC%88%98%20%EC%9E%90%EB%A3%8C%ED%98%95.html
# https://dojang.io/mod/page/view.php?id=2466

# 3주차는 Chapter_4 반복문 #
# - 반복문이란? 반복해서 코드를 수행할때 사용하는 명령어를 반복문이라고 한다.
# - 반복문에는 for, while 두가지가 있음.
# - break문과 continue문을 통하여 반복분을 보다 세밀하게 설정할 수 있음.

printc("4-1 리스트와 반복문")

print("")

printc("# 리스트란? 여러가지 자료를 저장할 수 있는 자료형")
printc("# 리스트는 대괄호 [] 안에 여러가지 데이터를 넣고 ,(콤마) 로 자료들을 구분한다.")
printc("# 리스트는 여러가지 자료형을 가지고 구성할 수 있다.")
list = [1,2,3,4,5, "문자열", True, False]
print('list = [1,2,3,4,5, "문자열", True, False] : ', list)

print("")

printc("# 리스트 안에 넣은 자료들은 인덱스를 활용해서 사용할 수 있다. (문자열 인덱스와 비슷함.)")
list = [1,2,3,4,5, "문자열", True, False]
print('list = [1,2,3,4,5, "문자열", True, False] : ', list)
print('list[0] : ',list[0])
print('list[1] : ',list[1])
print('list[2] : ',list[2])
print('list[3] : ',list[3])
print('list[4] : ',list[4])
print('list[5] : ',list[5])

print("")

printc("# 문자열 인덱스와 마찬가지로 범위와 마이너스를 선택할 수 있다.")
list = [1,2,3,4,5, "문자열", True, False]
print('list = [1,2,3,4,5, "문자열", True, False] : ', list)
print('list[1:3] : ',list[1:3])
print('list[2:4] : ',list[2:4])
print('list[-1] : ',list[-1])
print('list[-3] : ',list[-3])

print("")

printc("# 인덱스는 이중으로 사용 가능함.")
list = [1,2,3,4,5, "문자열", True, False]
print('list = [1,2,3,4,5, "문자열", True, False] : ', list)
print('list[5][0] : ',list[5][0])
print('list[5][1] : ',list[5][1])
print('list[5][2] : ',list[5][2])

print("")

printc("# 리스트 안에 리스트 사용 가능")
list= [[1,2,3], [4,5,6], [7,8,9]]
print('list= [[1,2,3], [4,5,6], [7,8,9]] : ',list)
print('list[0][2] : ',list[0][2])
print('list[1][1] : ',list[1][1])
print('list[2][0] : ',list[2][0])

print("")

printc("# 아래는 구성이 가능할까?")
print('list = [[1,2,3], [4,5,6], [7,8,9], 10, 11, "문자열"]')
list = [[1,2,3], [4,5,6], [7,8,9], 10, 11, "문자열"]
input()
print('가능!! :  ',list)

print("")

printc("# 문자열 인덱스 처럼 IndexError도 동일하게 나옴")
list = [1,2,3]
print('list = [1,2,3]')
print('list[10]')
runnum = input("패스는1")
print('runnum : ', runnum)
if runnum == "1":
    print(list[10])

print("")

printc("# 리스트 연산자 연결(+), 반복(*), len()")
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print('list_a = [1, 2, 3] : ',list_a)
print('list_b = [4, 5, 6] : ',list_b)
print('list_a + list_b : ',list_a + list_b) # 리스트끼리 더한다.
print('list_a * 3 : ',list_a * 3) # 리스트를 반복한다
print('len(list_a) : ',len(list_a)) # 리스트의 길이를 구한다.
print("")

printc("# 리스트 안에 리스트를 넣었을때 len 함수는 먹힐까? 먹힌다면 길이는 몇?")
list_a = [[1, 2, 3], [2, 3, 4], 3, 4, 5]
print('list_a = [[1, 2, 3], [2, 3, 4], 3, 4, 5] : ',list_a)
input()
print('len(list_a) : ', len(list_a))
print("")

printc("# 리스트 안에 리스트의 길이를 구하고 싶을 때는?")
list_a = [[1,2,3],[2,3,4],3]
input()
print('len(list_a[0]) : ', len(list_a[0]))
input()
print("")

printc("# 리스트에 요소 추가하기 append, insert, extend")
printc("# append : 리스트의 맨 끝에 추가 append(요소), extend(요소, 요소, 요소)")
printc("# insert : 위치를 정하고 추가    insert(위치, 요소)")
list_a = [1,2,3]
print('list_a = [1,2,3] : ',list_a)
list_a.append(4)
print('append(4) : ', list_a)

list_a.append(5)
print('append(5) : ', list_a)

list_a.insert(0,10)
print('insert(0,10) : ', list_a)

print("")
printc("# 인덱스가 넘는 위치에 추가를 한다면?")
input()
list_a.insert(100,20)
print('insert(100,20) : ', list_a)
input()

list_a.extend([11,12,13])
print('extend([11,12,13] : ', list_a)
print("")

printc("# 리스트에 요소 삭제하기 del, pop, remove, clear")
printc("# del : 리스트의 특정 인덱스 요소를 제거 / del 리스트명[인덱스]")
printc("# pop : 리스트의 특정 인덱스 요소를 제거 매개변수가 없으면 마지막 요소 제거/ 리스트명.pop(인덱스)")
printc("# remove : 값을 기준으로 제거 / 리스트.remove(값)")
printc("# clear : 모두 제거 / 리스트.clear()")

list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('list_a           : ', list_a)

del list_a[1]
print('del list_a[1]    : ', list_a)

del list_a[8:9]
print('list_a[8:9]      : ', list_a)

del list_a[6:]
print('list_a[6:]       : ', list_a)

list_a.pop(2)
print('list_a.pop(2)    : ', list_a)

list_a.pop()
print('list_a.pop()     : ', list_a)

list_b = [1,2,3,3,3,4,5,6]
print('list_b           : ', list_b)

list_b.remove(3)
print('list_b.remove(3) : ', list_b)

list_b.clear()
print('list_b.clear()   : ', list_b)

print("")

printc("# 리스트 내부에 있는지 확인하기 in / not in 연산자, 값 in 리스트")
list_a = [1, 2, 3, 4, 5]
print("list_a :",list_a)
print("1 in list_a : ",1 in list_a)
print("6 in list_a : ",6 in list_a)
print("3 in list_a : ",3 in list_a)
print("6 not in list_a : ",6 not in list_a)

print("")

printc("# for 반복문")
printc("# - 반복문이란? 반복해서 코드를 수행할때 사용하는 명령어를 반복문이라고 한다.")
printc("# - 반복문에는 for, while 두가지가 있음.")
printc("# - 반복문에는 for, while 두가지가 있음.")
printc("# - break문과 continue문을 통하여 반복분을 보다 세밀하게 설정할 수 있음.")

printc("출력을 10번 출력 하려면?")
input()
print("print('출력')")
print("print('출력')")
print("print('출력')")
print("print('출력')")
print("print('출력')")
print("print('출력')")
print("print('출력')")
print("print('출력')")
print("print('출력')")
input()

print('for i in range(10):')
print('    print("출력")')

printc("# 반복문은 앞에서 배운 리스트를 가지고 반복문을 만들수도 있는데")
printc("# for 반복자 in 반복할수있는것:")
printc("#     코드")

array = [1, 2, 3, 4, 5]
print("array : ",array)
print("for element in array:")
print("    print(element)")
for element in array:
    print(element)

printc("# 문자열도 동일하게 사용이 가능함")
print("for element in 안녕하세요:")
print("    print(element)")
for element in "안녕하세요":
    print(element)


printc("# 문제풀이 3번 4번문제")






