#多肢選択問題の正解率
import csv
import re
import urllib.request
import ollama

MODEL = "qwen2.5"   # ローカルモデル。回数制限なし

# --- 1. 科目のCSVをダウンロード（日本史） ---
SUBJECT = "japanese_history"
url = f"https://raw.githubusercontent.com/nlp-waseda/JMMLU/main/JMMLU/{SUBJECT}.csv"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    content = resp.read().decode("utf-8")
with open(f"{SUBJECT}.csv", "w", encoding="utf-8") as f:
    f.write(content)

# --- 2. 読み込み ---
rows = []
with open(f"{SUBJECT}.csv", encoding="utf-8") as f:
    for row in csv.reader(f):
        if len(row) == 6:          # 問題,A,B,C,D,正解 の6列のみ採用
            rows.append(row)

# 全問解く場合は下行をコメントアウト。まず数問で動作確認を推奨
# rows = rows[:5]

# --- 3〜4. 1問ずつ質問して正解と照合 ---
correct = 0
for i, (q, a, b, c, d, answer) in enumerate(rows):
    prompt = f"""次の問題の正解を一つ選び、記号（A, B, C, D）のみを出力してください。

{q}
A. {a}
B. {b}
C. {c}
D. {d}

正解:"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    text = response["message"]["content"]
    # モデルの出力から最初の A/B/C/D を取り出す
    m = re.search(r"[ABCD]", text.upper())
    pred = m.group() if m else "?"

    if pred == answer.strip().upper():
        correct += 1
    print(f"{i+1}: 予測={pred} 正解={answer.strip()}")

# --- 5. 正解率 ---
print(f"\n正解率: {correct}/{len(rows)} = {correct/len(rows):.1%}")

'''
1: 予測=B 正解=B
2: 予測=B 正解=B
3: 予測=C 正解=D
4: 予測=A 正解=D
5: 予測=A 正解=A
6: 予測=A 正解=A
7: 予測=C 正解=D
8: 予測=A 正解=A
9: 予測=A 正解=C
10: 予測=B 正解=D
11: 予測=B 正解=A
12: 予測=A 正解=A
13: 予測=B 正解=C
14: 予測=C 正解=C
15: 予測=C 正解=A
16: 予測=B 正解=D
17: 予測=C 正解=A
18: 予測=A 正解=C
19: 予測=B 正解=A
20: 予測=B 正解=D
21: 予測=B 正解=A
22: 予測=C 正解=D
23: 予測=A 正解=C
24: 予測=B 正解=B
25: 予測=D 正解=C
26: 予測=B 正解=A
27: 予測=A 正解=A
28: 予測=A 正解=D
29: 予測=A 正解=A
30: 予測=A 正解=D
31: 予測=C 正解=C
32: 予測=A 正解=A
33: 予測=C 正解=D
34: 予測=C 正解=C
35: 予測=C 正解=C
36: 予測=A 正解=D
37: 予測=D 正解=C
38: 予測=A 正解=C
39: 予測=C 正解=D
40: 予測=B 正解=D
41: 予測=A 正解=A
42: 予測=B 正解=C
43: 予測=C 正解=D
44: 予測=D 正解=B
45: 予測=C 正解=C
46: 予測=A 正解=C
47: 予測=B 正解=B
48: 予測=C 正解=C
49: 予測=C 正解=D
50: 予測=A 正解=C
51: 予測=A 正解=D
52: 予測=B 正解=D
53: 予測=A 正解=A
54: 予測=C 正解=C
55: 予測=C 正解=D
56: 予測=B 正解=A
57: 予測=D 正解=D
58: 予測=B 正解=A
59: 予測=D 正解=B
60: 予測=B 正解=D
61: 予測=D 正解=B
62: 予測=B 正解=A
63: 予測=C 正解=C
64: 予測=C 正解=B
65: 予測=D 正解=D
66: 予測=A 正解=B
67: 予測=B 正解=B
68: 予測=B 正解=B
69: 予測=A 正解=A
70: 予測=D 正解=C
71: 予測=D 正解=D
72: 予測=B 正解=B
73: 予測=A 正解=A
74: 予測=A 正解=D
75: 予測=C 正解=C
76: 予測=A 正解=C
77: 予測=A 正解=D
78: 予測=B 正解=D
79: 予測=C 正解=C
80: 予測=C 正解=C
81: 予測=B 正解=A
82: 予測=A 正解=D
83: 予測=D 正解=D
84: 予測=C 正解=A
85: 予測=A 正解=D
86: 予測=D 正解=D
87: 予測=D 正解=A
88: 予測=A 正解=C
89: 予測=A 正解=A
90: 予測=C 正解=C
91: 予測=C 正解=A
92: 予測=C 正解=D
93: 予測=B 正解=B
94: 予測=A 正解=B
95: 予測=A 正解=A
96: 予測=D 正解=C
97: 予測=A 正解=C
98: 予測=C 正解=D
99: 予測=B 正解=A
100: 予測=D 正解=B
101: 予測=D 正解=D
102: 予測=A 正解=D
103: 予測=D 正解=D
104: 予測=B 正解=C
105: 予測=A 正解=A
106: 予測=A 正解=A
107: 予測=A 正解=A
108: 予測=C 正解=D
109: 予測=B 正解=B
110: 予測=B 正解=D
111: 予測=B 正解=B
112: 予測=C 正解=A
113: 予測=C 正解=D
114: 予測=A 正解=D
115: 予測=B 正解=B
116: 予測=C 正解=C
117: 予測=D 正解=D
118: 予測=D 正解=A
119: 予測=D 正解=D
120: 予測=D 正解=B
121: 予測=A 正解=B
122: 予測=C 正解=C
123: 予測=D 正解=D
124: 予測=B 正解=A
125: 予測=B 正解=B
126: 予測=D 正解=D
127: 予測=B 正解=C
128: 予測=A 正解=D
129: 予測=A 正解=D
130: 予測=B 正解=C
131: 予測=B 正解=B
132: 予測=B 正解=D
133: 予測=B 正解=B
134: 予測=D 正解=C
135: 予測=B 正解=B
136: 予測=A 正解=D
137: 予測=C 正解=B
138: 予測=A 正解=A
139: 予測=A 正解=B
140: 予測=B 正解=D
141: 予測=A 正解=A
142: 予測=B 正解=C
143: 予測=B 正解=D
144: 予測=C 正解=A
145: 予測=B 正解=B
146: 予測=D 正解=D
147: 予測=D 正解=A
148: 予測=D 正解=D
149: 予測=D 正解=D
150: 予測=B 正解=B

正解率: 63/150 = 42.0%
'''