data = [int(c) for c in input().split()]
# dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
# ここにプログラムを追記
for k in range(len(data)-1):
  if(data[k]==data[k+1]):
    print("YES")
    break
  elif k == len(data)-2:
    print("NO")