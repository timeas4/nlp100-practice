S = input()
# ここにプログラムを追記
L = list(S)
a = int(L[0])
i = 0
while i < len(L)-2:
  if L[i+1] == "+":
    a+=int(L[i+2])
  elif L[i+1] == "-":
    a-=int(L[i+2])
  i+=2
print(a)