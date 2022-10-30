# 모각코 15회차
# 2022년 10월 16일 14:00~16:00
# 참가자: 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# k의 개수 1
def solution(i, j, k):
    ans=''
    for i in range(i, j+1):
        ans+=str(i)
    ans = list(ans)
    answer = 0
    for i in ans:
        if i==str(k):
            answer+=1
    return answer

# k의 개수 2
def solution(i, j, k):
    from collections import Counter
    ans = 0
    for i in range(i,j+1):
        ans += Counter(str(i))[str(k)]
    return ans