#暗号文
def  cipher(text):
    result=""
    for s in text:
        if s.islower(): #islower()は文字が小文字かどうかを判定する関数
            code=219-ord(s) #ord()は文字を数値に変換する関数 ordinary
            result+=chr(code) #chr()は数値を文字に変換する関数 char
        else:
            result+=s
    return result

print(cipher("Hello, World!"))