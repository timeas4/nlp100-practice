#対話
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MODEL = "gemini-2.5-flash"

question = """つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。"""

response = client.models.generate_content(
    model=MODEL,
    contents=question,
)
print(response.text)

'''
つばめちゃんの目的地の駅は**緑が丘（みどりがおか）**です。

1.  自由が丘から東急大井町線大井町方面の急行に乗車した場合、次の停車駅は**大岡山**です。
2.  つばめちゃんは大岡山で降車し、反対方向（二子玉川方面）の電車に乗り換えました。
3.  大岡山から一駅戻ると、**緑が丘**駅になります。
'''