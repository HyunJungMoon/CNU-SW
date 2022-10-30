# 모각코 12회차
# 2022년 09월 24일 16:00~19:00
# 참가자: 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 짝수 홀수 개수
def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        if i%2==0:
            answer[0]+=1
        else:
            answer[1]+=1
    return answer

# 배열의 유사도 1
def solution(s1, s2):
    if s1>=s2:
        a = 0
        for i in s2:
            if i in s1:
                a+=1
            else:
                pass
    else:
        a = 0
        for i in s1:
            if i in s2:
                a+=1
            else:
                pass
    return a

# 배열의 유사도 2
def solution(s1, s2):
    n = set(s1)&set(s2)
    return len(n)