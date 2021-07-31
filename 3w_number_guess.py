import random

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
# 랜덤 숫자를 입력합니다.
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