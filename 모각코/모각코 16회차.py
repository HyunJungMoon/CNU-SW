# 모각코 16회차
# 2022년 10월 23일 19:00~21:00
# 참가자: 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    import re
    answer = re.findall(r'\d+', my_string)
    ans = map(int, answer)
    return sum(ans)
'''
    re.findall(pattern,string): 문자열의 패턴에 해당하는 모든 문자를 찾아 리스트로 반환
    r'\d': 숫자 하나
    r'\d+': 연속된 숫자
'''

# 이진수 더하기
def solution(bin1, bin2):
    ans = int(bin1, 2)+int(bin2, 2)
    return bin(ans)[2:]