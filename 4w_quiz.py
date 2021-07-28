#-*- coding: utf-8 -*-

# 2주, 3주차에 만든 퀴즈문제를 활용(안만드셨으면 github에서 제꺼 그대로 떙겨오셔도 됩니다.)
# 메인코드 실행 -> 하고 싶은게임 입력 -> 해당 값에 따라 게임 함수를 불러오는 형태로 구성
# 메인코드에 실제 게임 관련 내용이 들어가면 안됨!
# 게임 실행에 대한 기본 값을 받는다.(입력이 없을경우 퀴즈게임이 실행 되도록)
# 추가사항(해보면 좋은 내용)
# - 2주차 퀴즈게임에 퀴즈답을 파일로 읽어서 사용하는 방법


# 모듈
import random

## 2주차 퀴즈게임
def quiz():
    
    ## 퀴즈를 맞춰서 점수를 매기는 게임
    ## 시작에 대한 여부 

    quiz_answer = [
        ["당신이 다니고 있는 회사의 이름은?","야놀자"],
        ["당신이 다니고 있는 회사의 영문 이름은?","yanolja"],
        ["현재 다니고 있는 회사에서 가장 가까운 역은?","삼성역"],        
        ["현재 공부하고 있는 수업의 언어는?","파이썬"]
    ]


    print("퀴즈게임에 온것을 환영합니다.")
    playing = input("퀴즈게임을 시작하시겠습니까? (시작하려면 yes) ")

    if playing.lower() != "yes":
        quit()

    print("좋아, 그럼 게임을 시작하지 :)")
    score = 0
    for i in range(len(quiz_answer)):    
        answer = input(quiz_answer[i][0])
        if answer == (quiz_answer[i][1]):
            print('정답!!!')
            score += 1
        else:
            print("땡!!!")
            
    print("당신은 " + str(score) + " 개의 문제를 맞추었습니다.")
    print("당신의 정답율은" + str((score / 4) * 100) + " % 입니다.")

## 3주차 숫자맞추기 게임
def number_guess():
    print("정해진 범위 내에서 숫자를 맞추는 게임입니다.")
    top_of_range = input("0보다 큰 숫자를 입력해주세요(범위설정) :  ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print('0보다 큰 숫자를 입력하지 않아 종료합니다.')
            quit()
    else:
        print('숫자를 입력하지 않아 종료합니다.')
        quit()
    ## 랜덤 숫자를 입력합니다.
    random_number = random.randint(0, top_of_range)
    guesses = 0
    print(f"정답은 0부터 {top_of_range} 까지의 숫자중 하나입니다.")
    while True:
        guesses += 1
        user_guess = input("숫자를 맞춰보세요: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print('숫자를 입력해주세요.')
            continue

        if user_guess == random_number:
            print("숫자를 맞췄습니다!!")
            break   

        elif user_guess > random_number:
            print("정답은 더 낮은 숫자입니다.")

        else:
            print("정답은 더 높은 숫자입니다.")

    print("당신은", guesses, "회 만에 맞췄습니다.")

## 메인 코드
def mainmenu(number=1):    
    print("지금부터 여러가지 게임을 시작하지.\n\n")
    print("1) 퀴즈게임\n")
    print("2) 숫자맞추기 게임\n")
    print("3) 게임을 종료\n")
    print("미입력시 퀴즈게임이 선택됩니다.\n")
    number_check = 0
    while number_check not in ['','1','2','3']:
        number_check = input("원하는 게임을 골라보게나) ")
    if number_check == '':
        number_check = int(number)
    number_check = int(number_check)
    if number_check == 1:
        quiz()
    elif number_check == 2:
        number_guess()
    else:
        print("게임이 종료되었습니다.")
        quit()

# 메인 코드 실행
mainmenu()
