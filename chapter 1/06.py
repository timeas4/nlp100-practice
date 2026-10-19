#集合
def n_gram(input,n):
    return set([input[i:i+n] for i in range(len(input)-n+1)]) #setを使用して重複を排除

X=n_gram("paraparaparadise", 2)
Y=n_gram("paragraph", 2)
print(X)
print(Y)
print(X | Y)    #和集合
print(X&Y)  #積集合
print(X-Y)  #差集合

w="se" #seがXとYのどちらに含まれているか
print(w in X)
print(w in Y)