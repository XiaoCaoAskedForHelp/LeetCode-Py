from math import inf
import heapq

n,m = map(int,input().split())

shops = [[] for _ in range(m)]
for i in range(m):
    s,t,p,c = map(int,input().split())
    objs = []
    for j in range(c):
        a,b = map(int,input().split())
        objs.append((a,b))
    shops[i] = [s,t,p,objs]

price = [-1] * (n + 1)
items = [[] for _ in range(n + 1)]   # 因为优惠区间可能有多个，所以需要都记录下来
# 找到每个商品的最小值
for s,t,p,objs in shops:
    for a,b in objs:
        heapq.heappush(items[a],(b,b,m))
        if price[a] == -1:
            price[a] = b
        elif price[a] > b:
            price[a] = b

# 每一个时刻商品的最小值，总的最小值总是在折扣的起始时间出现
shops.sort(key=lambda x:x[0])
time = []  # 记录什么时间需要让价格恢复原价
res = inf
for s,t,p,objs in shops:
    # 先将需要恢复原价的商品恢复
    while time and time[0][0] < s:
        end,org,index = heapq.heappop(time)
        price[index] = org
        
    heapq.heappush(time,(b * p // 100,b,))   # 记录结束时间和原价和商品编号
    for a,b in objs:
        dis = b * p // 100
        if dis < price[a]:
            price[a] = dis
            
    # 计算现在的总价
    total = sum(price[1:])
    res = min(total,res)
print(res)
    


    


        
