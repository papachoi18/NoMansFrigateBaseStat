import time

arr = [4, 8, 15, 25, 30, 35, 40, 45, 50, 55]
while True:
    count = int(input("원정 횟수를 적어주세요:"))
    print()
    
    totStat = 0
    totStat += int(input("전투 스탯을 적어주세요:"))
    totStat += int(input("탐험 스탯을 적어주세요:"))
    totStat += int(input("산업 스탯을 적어주세요:"))
    totStat += int(input("무역 스탯을 적어주세요:"))
    print()
    
    for i in range(10):
        if count < arr[i]:
            break
        else:
            totStat -= 6
    
    P = int(input("긍정 특성 개수를 적어주세요(주스탯15 미포함):"))
    print()
    if P != 0:
        print(P, "개의 특성 스탯 수치를 하나씩 입력해주세요:")
        for i in range(P):
            totStat -= int(input())
    print()
    
    N = int(input("부정 특성 개수를 적어주세요:"))
    print()
    if N != 0:
        print(N, "개의 특성 스탯 수치를 하나씩 입력해주세요:(-기호 생략)")
        for i in range(N):
            totStat += int(input())
    print()
    print("해당 호위함 기본 스탯은", totStat, "입니다.")
    time.sleep(1)
    print("\n=============================초기화=============================")
    
