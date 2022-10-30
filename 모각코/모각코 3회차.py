# 모각코 3회차
# 2022년 07월 24일 19:00~22:00
# 참가자: 김경미, 문현정, 서성민
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 1. 소수 만들기
from itertools import permutations
def solution(n):
    sum_list=list(permutations(n, 3))
    l = []
    for i in sum_list:
        l.append(sum(i))
    l = set(l)
    n = 0
    for a in list(l):
        b = int(a*0.5)+1
        for j in range(2, b+1):
            if a%j==0 and a!=j:
                n+=1
                break
    return len(l)-n

# 4. 숫자게임
def solution(A, B):
    A.sort()
    B.sort()
    ans = 0
    for i, j in zip(A,B):
        if i<j:
            ans+=1
    return ans

# 문자열 뒤집기 1 
def solution(my_string):
    ans = list(my_string)
    answer = []
    for i in range(1, len(ans)+1):
        answer.append(ans[len(ans)-i])
    ans = ''.join(answer)
    return ans