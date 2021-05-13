def solution(nums):
    answer = 0
    total = len(nums)
    pocketmon = {} #create an empty dictionary
    for i in nums:
        if i in pocketmon:
            pocketmon[i] +=1
        else:
            pocketmon[i] = 1 #포켓몬 새로 등록
    kind = len(pocketmon)
    if kind > total/2:
        answer = total/2
    else:
        answer = kind
    return answer
