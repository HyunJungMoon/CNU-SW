# 모각코 7회차
# 2022년 08월 21일 19:00~22:00
# 참가자: 김경미, 문현정, 서성민
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 문자 정렬하기 (1)
def solution(my_string):
    import re
    answer = re.findall(r'\d', my_string)
    ans = map(int, answer)
    ans.sort()
    return ans

# 문자 정렬하기 (2)
def solution(my_string):
    ans = list(my_string.lower()) # 소문자
    ans.sort()
    return ''.join(ans)

# 대문자와 소문자
def solution(my_string):
    ans = ''
    for i in range(len(my_string)):
        if my_string[i].isupper(): # 대문자 판별
            ans+=my_string[i].lower()
        else:
            ans+=my_string[i].upper()
    return ans