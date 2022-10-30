# 모각코 13회차
# 2022년 10월 02일 19:00~21:00
# 참가자: 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 숫자 찾기 1
def solution(num, k):
    num = list(str(num))
    n = 0
    if str(k) in num:
        for i in num:
            if str(k)==i:
                n+=1
                break
            else:
                n+=1
    else:
        n=-1
    return n

# 숫자 찾기 2
def solution(num, k):
    num = str(num).find(str(k))
    if num!=-1:
        num+=1
    return num

# 암호 해독 1
def solution(cipher, code):
    answer = ''
    cip = list(cipher)
    for i in range(1, len(cip)+1):
        if i%(code)==0:
            answer+=cip[i-1]
    return answer