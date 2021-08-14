
## K번째수
def solution(array, commands):    
    counts = len(commands)
    answer = []
    for count in range(0, counts):
      first = commands[count][0]      
      end = commands[count][1]
      select = commands[count][2]
      # print(commands[count][2])      
      sort2 = (sorted((array[first-1:end])))
      result = sort2[select-1]
      answer.append(result)
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
