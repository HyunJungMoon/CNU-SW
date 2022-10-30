# 모각코 1회차
# 2022년 07월 10일 19:00~22:00
# 참가자: 김경미, 문현정, 서성민
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 기본 2.
import numpy as np
def solution(x, w, b):
    ans = np.dot(x, w) + b
    return ans

# 기본 3.
def solution(n):
    ans = []
    for i in range(len(n[0])):
        if 150>n[0][i] or 195<i[0][i] or i[1][i]>=140:
            ans.append(i)
    return ans

# 옹알이(1)
def solution(babbling):
    ans = 0
    n = ["aya", "ye", "woo", "ma"]
    for i in range(4):
        for j in range(4):
            n.append(n[i]+n[j])
            for k in range(4):
                n.append(n[i]+n[j]+n[k])
                for l in range(4):
                    n.append(n[i]+n[j]+n[k]+n[l])
    for i in babbling:
        if i in list(set(n)):
            ans+=1
    return ans