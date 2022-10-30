# 모각코 10회차
# 2022년 09월 07일 14:00~17:00
# 참가자: 김경미, 문현정
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 중복된 문자 제거
def solution(my_string):
    m = list(dict.fromkeys(my_string)) # 순서 유지 & 중복 값을 삭제
    return ''.join(m)

# 2차원으로 만들기
def solution(num_list, n):
    import numpy as np
    a = len(num_list)//n
    m = np.array(num_list).reshape((a, n))
    m = m.tolist()
    return m

# 모스부호 (1)
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    ans = ''
    s = list(letter.split(' ')) 
    for i in s:
        ans+=morse[i]
    return ans