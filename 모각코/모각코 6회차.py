# 모각코 6회차
# 2022년 08월 14일 19:00~22:00
# 참가자: 김경미, 문현정, 서성민
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 문자열안에 문자열
def solution(str1, str2):
    if str1.find(str2)==-1:
        return 2
    else:
        return 1

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    import re
    answer = re.findall(r'\d', my_string)
    ans = map(int, answer)
    return sum(ans)
    '''
    re.findall(pattern,string): 문자열의 패턴에 해당하는 모든 문자를 찾아 리스트로 반환
    r'\d': 숫자 하나
    r'\d+': 연속된 숫자
     '''

# 특정 문자 제거하기
def solution(my_string, letter):
    m = list(my_string)
    while True:
        if letter in m:
            m.remove(letter)
        else:
            break
    return (''.join(m))