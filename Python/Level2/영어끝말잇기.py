def solution(n, words):
    answer = []
    index = 0
    person = 0
    count = 0
    for word in words:
        if index == 0:
            #첫 번째 단어면 그냥 넘어가기
            index+=1
            continue
        else:
            if word[0] == words[index-1][-1] and word not in words[0:index-1]:
                #전 단어랑 이어지고, 앞에서 말한 적 없는 단어인지
                index+=1
                continue
            else:
                #탈락한 사람 뽑아내기
                count = int((index)/n+1)
                person = (index+1)%n if person !=0 else n
                
    if index == len(words):
        answer = [0,0]
        #마지막까지 다 돌았으면? 탈락한 사람 없다
    else:
        answer = [person, count]
    return answer
