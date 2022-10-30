# 모각코 5회차
# 2022년 08월 07일 19:00~22:00
# 참가자: 김경미, 문현정, 서성민
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# A로 B 만들기
def solution(before, after):
    be = list(before)
    be.sort()
    af = list(after)
    af.sort()
    if be==af:
        return 1
    else:
        return 0

# n의 배수 고르기
def solution(n, numlist):
    ans=[]
    for i in numlist:
        if i%n==0:
            ans.append(i)
    return ans

# 모음 제거
def solution(my_string):
    ans = ''
    a = ['a', 'i', 'u', 'o', 'e']
    for i in range(len(my_string)):
        if my_string[i] in a:
            pass
        else: 
            ans+=my_string[i]
    return ans