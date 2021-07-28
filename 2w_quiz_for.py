## 퀴즈를 맞춰서 점수를 매기는 게임
## 시작에 대한 여부 

quiz_answer = [
    ["당신이 다니고 있는 회사의 이름은?","야놀자"],
    ["당신이 다니고 있는 회사의 영문 이름은?","yanolja"],
    ["현재 다니고 있는 회사에서 가장 가까운 역은?","삼성역"],
    ["현재 공부하고 있는 수업의 언어는?","파이썬"],
    ["현재 공부하고 있는 수업의 언어는?","파이썬"],
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