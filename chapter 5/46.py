#川柳の生成
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash"

# お題は自由に設定
theme = "在宅勤務"

prompt = f"""「{theme}」をお題にして、川柳を10個作成してください。
川柳は五・七・五（合計17音）の形式で、口語的でユーモアや世相を込めたものにしてください。
番号をつけて10個出力してください。"""

response = client.models.generate_content(
    model=MODEL,
    contents=prompt,
)
print(response.text)

'''
はい、承知いたしました。「在宅勤務」をお題に、五・七・五の川柳を10個作成します。

---

1.  着替えるか 悩む午前中 パジャマのまま
2.  会議中 映る子の顔 パパは営業
3.  冷蔵庫 仕事の合間の 誘惑が
4.  通勤路 今はリビング 天国か
5.  カメラオフ 誰が映ってる 背景だけ
6.  座りすぎ 腰がミシミシ 伸びしたい
7.  仕事終え 気がつけばまた パソコン前
8.  ランチ代 浮いたはずなのに 宅食頼む
9.  猫が鳴く 会議に響く 癒やし声
10. 書斎無し 寝室の隅で 仕事する
'''