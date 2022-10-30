# 모각코 4회차
# 2022년 07월 31일 19:00~22:00
# 참가자: 김경미, 문현정, 서성민
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 문자열 뒤집기 2
def solution(my_string):
    ans = list(my_string)
    ans.reverse()
    ans = ''.join(ans)
    return ans

# 각도기
def solution(angle):
    if 0<angle<90:
        return 1
    elif angle==90:
        return 2
    elif 90<angle<180:
        return 3
    else:
        return 4

# 중앙값 구하기
def solution(array):
    array.sort()
    n = int(len(array)/2)
    return array[n]