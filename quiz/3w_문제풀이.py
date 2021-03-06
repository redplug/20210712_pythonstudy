# 04-1 3-1문제

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 1:
        print(number,"는 홀수 입니다.")
    else:
        print(number,"는 짝수 입니다.")

# 04-1 3-2번
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    count = len(str(number))
    print(number,"는",count,"자리수입니다")

# 04-1 4번
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9],
]

for numbers in list_of_list:
    for number in numbers:
        print(number)

# 04-1 5번
numbers = [1,2,3,4,5,6,7,8,9]
output=[[],[],[]]

for number in numbers:
    output[number % 3 -1].append(number)

print(output)


#04-2 2번문제
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1},
]

print("# 우리 동네 애완 동물들")
for pet in pets:    
    print(pet["name"], str(pet["age"])+"살")

#04-2 3번문제
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:    
    if number not in counter:
        counter[number] = 1
    else:
        counter[number] += 1
print(counter)

#04-2 4번문제
character = {
    "name" : "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의검",
        "armor": "풀플레이트"
        },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }

for key in character:    
    if type(character[key]) is dict:        
        for i in character[key]:            
            print(i + " :",character[key][i])            
    elif type(character[key]) is list:
        for i in character[key]:
            print(key + " :", i)
    else:
        pass
        print(key + " :", character[key])

# 4-3 2
key_list = ["name","hp","mp","level"]
value_list = ["기사",200,30,5]
character = {}
for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]
print(character)

# 4-3 3
limit = 10000
i = 1
sum_value = 0
while sum_value < limit:    
    sum_value += i    
    i += 1
print(f"{i-1}를 더할 때 {limit}을 넘으며 그때의 값은 {sum_value}입니다.")

# 4-3 4
max_value = 0
a = 0
b = 0
for i in range(1, 100):    
    j = 100 - i
    if max_value < j * i:        
        a = i
        b = j
        max_value = j * i

print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))

# 4-4 2
output = [ i for i in range(1,100+1) if "{:b}".format(i).count("0") == 1 ]
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))