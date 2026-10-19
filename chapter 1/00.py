#パタトクカシーー
s="パトカー"
m="タクシー"
t=""
for i in range(len(s)+len(m)):
    if i%2==0:
        t+=s[i//2]
    else:
        t+=m[i//2]
print(t)