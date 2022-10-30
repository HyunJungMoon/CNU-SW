# 모각코 8회차
# 2022년 08월 28일 19:00~22:00
# 참가자: 김경미, 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 인덱스 바꾸기
def solution(my_string, num1, num2):
    m = list(my_string)
    m[num1], m[num2] = m[num2], m[num1]
    return ''.join(m)

# 외계행성의 나이
def solution(age):
    key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    val = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    ans = ''
    for i in list(str(age)):
        n = key.index(i)
        ans += val[n]
    return ans

# 최댓값 만들기 (2)
def solution(numbers):
    from itertools import combinations # 조합
    n = list(combinations(numbers, 2))
    m = []
    for i in range(len(n)):
        m.append(n[i][0]*n[i][1])
    return max(m)