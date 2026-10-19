#n-gram
def n_gram(input, n):
    return [input[i:i+n] for i in range(len(input)-n+1)] #リスト内包表記使用

def m_gram(input, m):
    for i in range(len(input)-m+1):
        yield input[i:i+m] #ジェネレータ使用

input = "I am an NLPer"
print(n_gram(input, 3))
print(n_gram(input.split(), 2))