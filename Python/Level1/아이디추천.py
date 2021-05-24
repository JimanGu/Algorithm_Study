def solution(new_id):
    usable = "abcdefghijklmnopqrstuvwxyz.-_1234567890"
    answer = ''
    #1. 대문자를 소문자로 치환
    answer = new_id.lower()
    print(answer)
    #2. usable에 없는 문자 삭제
    answer = ''.join(x for x in answer if x in usable)
    print(answer)
    #3. 마침표 두개 이상 하나로 치환
    answer=list(answer)
    for i in range(len(answer)-1):
        if answer[i] == '.' and answer[i+1] == '.':
            answer[i] = ''
    
    answer = ''.join(answer)
    answer = list(answer)
    
    #4. 처음 끝 마침표 제거
    if answer[0] == '.':
        del answer[0]
    answer = ''.join(answer)
    
    if answer != '' and answer[-1] == '.':
        answer = answer[:-1]
    print(answer)
    
    #5. 빈 문자열, a 대입
    if answer == '':
        answer = 'a'
    print(answer)
    
    #6. 16자 이상이면 15자까지만 표기
    if len(answer) >= 16:
        answer = answer[:15]
    print(answer)
    
    #4. 처음 끝 마침표 제거
    if answer[0] == '.':
        del answer[0]
    answer = ''.join(answer)
    
    if answer != '' and answer[-1] == '.':
        answer = answer[:-1]
    print(answer)
    
    #7. 2자 이하면 마지막 문자를 3이상 될때까지
    if len(answer) == 1:
        answer = answer + answer[0] + answer[0]
    if len(answer) == 2:
        answer = answer + answer[1]
    print(answer)
    
    
    return answer
