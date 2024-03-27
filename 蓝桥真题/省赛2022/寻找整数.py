# 不能直接遍历10**17次方，得把步长加大
# 先找出两个整数，这两个整数相减就是区间
# L=[]
# for i in range(187,10**12,187):
#     if i%44==33 and i%45==29 and i%46==15 and i%47==5 and i%48==41 and i%49==46:
#     #else:
#         L.append(i)
#     if len(L)>=2:
#         break
# 用上面求出的正数区间去遍历
# L=[5458460249, 12590206409]
# step=L[1]-L[0]
# flag=0
# for i in range(L[0],10**17,step):
#     if i%20==9 and i%25==9 and i%26==23 and i%27==20 and i%28==25 and i%29==16 and i%30==29 and i%31==27 and i%32==25 and i%33==11 and i%34==17 and i%35==4 and i%36==29 and i%37==22 and i%38==37 and i%39==23 and i%40==9 and i%41==1 and i%42==11 and i%43==11 :
#         print(i)
#         break

# 剩余定理
ps = {
    2: 1,
    3: 2,
    5: 4,
    7: 4,
    11: 0,
    13: 10,
    17: 0,
    19: 18,
    23: 15,
    29: 16,
    31: 27,
    37: 22,
    41: 1,
    43: 11,
    47: 5
}


# 求 x,y 使得 ax + by = gcd(a,b)
# gcd(a,b) = 1 <=> ax + by = 1
# (a,b) = (b,a%b) 辗转相除
def exgcd(a, b):
    if b == 0: return 1, 0
    y, x = exgcd(b, a % b)
    return x, y - a // b * x


M = 1
ans = 0
for k in ps:
    M *= k  # 所有质数的乘积
for m, a in ps.items():
    Mi = M // m
    t, _ = exgcd(Mi, m)
    ans += a * Mi * t
print(ans % M)
