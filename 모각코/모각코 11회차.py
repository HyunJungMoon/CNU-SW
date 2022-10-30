# 모각코 11회차
# 2022년 09월 18일 19:00~22:00
# 참가자: 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 삼각형의 완성조건 (1)
def solution(sides):
    sides.sort()
    if sides[0]+sides[1]>sides[2]:
        return 1
    else:
        return 2

# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 짝수의 합
def solution(n):
    ans = 0
    if n%2==0:
        for i in range(n, 0, -2):
            ans+=i
        return ans
    else: 
        for i in range(n-1, 0, -2):
            ans+=i
        return ans