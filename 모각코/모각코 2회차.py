# 모각코 2회차
# 2022년 07월 17일 19:00~22:00
# 참가자: 김경미, 문현정, 서성민
# 1) 수업 내용 복습
# 2) 실습 문제 및 프로그래머스 문제 풀이

# 숫자 문자열과 영단어
def solution(s):
    l = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 
         'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for i in list(l.keys()):
        s = s.replace(i, str(l[i]))
    return int(s)

# 키패드 누르기
def solution(numbers, hand):
    num = {1:(0,0),2:(0,1),3:(0,2),
           4:(1,0),5:(1,1),6:(1,2),
           7:(2,0),8:(2,1),9:(2,2),
           '*':(3,0),0:(3,1),'#':(3,2)}
    L, R = [1,4,7], [3,6,9]
    L0, R0 = (3,0), (3,2)
    ans = ''
    for i in numbers:
        if i in L:
            ans+='L'
            L0 = num[i]
        elif i in R:
            ans+='R'
            R0 = num[i]
        else:
            DL = abs(num[i][0]-L0[0]) + abs(num[i][1]-L0[1])
            DR = abs(num[i][0]-R0[0]) + abs(num[i][1]-R0[1])

            if DL < DR:
                ans += 'L'
                L0 = num[i]
            elif DL > DR:
                ans += 'R'
                R0 = num[i]
            else:
                if hand == 'left':
                    ans += 'L'
                    L0 = num[i]
                else:
                    ans += 'R'
                    R0 = num[i]
    return ans