# 모각코 9회차
# 2022년 09월 04일 19:00~22:00
# 참가자: 김경미, 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 배열 회전시키기 1
def solution(numbers, direction):
    num = numbers.copy()
    if direction=='left':
        for i in range(len(numbers)-1):
            numbers[i] = num[i+1]
        numbers[-1] = num[0]
    else:
        for i in range(1, len(numbers)):
            numbers[i] = num[i-1]
        numbers[0] = num[-1]
    return numbers

# 배열 회전시키기 2
def solution(numbers, direction):
    from collections import deque
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1) # k만큼 오른쪽으로
    else:
        numbers.rotate(-1)
    return list(numbers)

# 7의 개수 1
def solution(array):
    ans=''
    for i in array:
        ans+=str(i)
    ans = list(ans)
    answer = 0
    for i in ans:
        if i=='7':
            answer+=1
    return answer