def string(n):
    global count
    if(n == 1):
       
        for i in range(0,count):
            print("____", end="")
        print("\"재귀함수가 뭔가요?\"")
        for i in range(0,count):
            print("____", end="")
        print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        for k in range(0,count):
            for i in range(0,count-k):
                print("____", end="")
            print("라고 답변하였지.")
        print("라고 답변하였지.")
        return 1;
    

    for i in range(0,count): print("____", end="")
    print("\"재귀함수가 뭔가요?\"")
    for i in range(0,count): print("____", end="")
    print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    for i in range(0,count): print("____", end="")
    print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    for i in range(0,count): print("____", end="")
    print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    
    count+=1
    return string(n - 1)
count=0   
a=int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
string(a+1)
# 개선 필수****
