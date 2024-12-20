# feat: 크리스마스 선물 BOJ_14235.py

# 입력
# 첫 번째 줄에서는 아이들과 거점지를 방문한 횟수 n이 주어진다.(1≤n≤5,000)
import sys
import heapq

n = int(sys.stdin.readline())
gift_in_order = []

for _ in range(n):
    gift_point = list(map(int, sys.stdin.readline().split()))
    
    # 뭔가 숫자가 있을 경우: 일단 우선순위 큐 gift_in_order에 넣기
    if gift_point[0] != 0:
        for i in range(1, len(gift_point)):
            heapq.heappush(gift_in_order, (-(gift_point[i]), gift_point[i]))
            
    # 0이 들어올 경우 : 뭔가 있으면 가장 높은 우선순위 출력, 아무것도 없으면 -1 출력
    else:
        if gift_in_order:
            print(heapq.heappop(gift_in_order)[1])
        else:
            print(-1)
        
# 다음 n줄에는 a가 들어오고, 그 다음 a개의 숫자가 들어온다. 
# 이는 거점지에서 a개의 선물을 충전하는 것이고, 그 숫자들이 선물의 가치이다.
#  만약 a가 0이라면 거점지가 아닌 아이들을 만난 것이다. 
# 선물의 가치는 100,000보다 작은 양의 정수이다.(1≤a≤100)

# 출력
# a가 0일 때마다, 아이들에게 준 선물의 가치를 출력하시오.
#  만약 줄 선물이 없다면 -1을 출력하라. 적어도 하나의 출력이 있음을 보장한다.

