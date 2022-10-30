# 모각코 14회차
# 2022년 10월 09일 13:00~15:00
# 참가자: 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 암호 해독 2
def solution(cipher, code):
    answer = cipher[code-1::code] # 건너뛰면서 슬라이싱
    return answer

# 7의 개수 2
def solution(array):
    n = map(str, array)
    return ''.join(n).count('7')

# 합성수 찾기
def solution(n):
    num=[]
    for i in range(4, n+1): 
        for j in range(2, n+1):  
                if i!=j and (i%j==0):  
                    num.append(i)
                    break
    return len(num)