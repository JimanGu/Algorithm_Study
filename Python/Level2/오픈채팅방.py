def solution(record):
    answer = []
    realanswer = []
    #key = userid, value = nickname 으로 구성된 딕셔너리 하나 생성
    userlist={}
    
    for user in record:
        situation = user.split()
        action = situation[0]
        userid = situation[1]
        
        if action == "Leave":
            answer.append("{0}님이 나갔습니다.".format(userid))
            continue #나갈 때는 인자로 닉네임이 들어오지 않음
        elif action == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(userid))
        userlist[userid] = situation[2]
        #닉네임 바꾸는 건 알림이 필요하지 않고, enter와 함께 닉네임만 딕셔너리에 추가
        
    #?분명 '님'전까지 자르는 방법이 있을텐데, 일단 몰라서 반복문으로 구현함
    for result in answer:
        userid=''
        for word in result:
            #'님'이 나오기 전까지를 userid로 본다
            if word != '님':
                userid+=word
            else:
                break
        
        result = result.replace(userid,userlist[userid])
        #?그냥 result를 바꾸니까 전체 answer에는 반영이 안됨
        realanswer.append(result)
    
    return realanswer
