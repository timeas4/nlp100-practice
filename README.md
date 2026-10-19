# 言語処理100本ノック 2025 の解答と AtCoder の練習

大学院（電気通信大学 稲葉研究室）の勉強会で取り組んだ、[言語処理100本ノック 2025](https://nlp100.github.io/2025/ja/) の解答です。
あわせて、AtCoder の練習問題の解答を置いています。

## 内容

| フォルダ | 内容 | 主に使ったもの |
|---|---|---|
| chapter 1 | 準備運動（文字列の操作） | Python |
| chapter 2 | UNIX コマンド相当の処理 | Python |
| chapter 3 | 正規表現（Wikipedia の記事から情報を取り出す） | re, json |
| chapter 4 | 言語解析（品詞、係り受け） | spaCy |
| chapter 5 | 大規模言語モデル（プロンプト、評価） | Gemini API, Ollama |
| chapter 6 | 単語ベクトル（類推、クラスタリング、t-SNE） | gensim, scikit-learn |
| chapter 7 | 機械学習（SST-2 の評判分析） | scikit-learn |
| chapter 8 | ニューラルネット | PyTorch |
| chapter 9 | 事前学習済み言語モデル（BERT 型） | Transformers |
| chapter 10 | 事前学習済み言語モデル（GPT 型）。生成、評判分析、LoRA によるファインチューニング | Transformers, PEFT |
| chapter 11 | 機械翻訳。KFTT の日英対訳で Transformer をゼロから学習し、BLEU で評価 | PyTorch, SentencePiece, sacreBLEU |
| AtCoder | AtCoder の練習問題 | Python |

## 動かすときの注意

- データセット（Wikipedia の記事、SST-2、KFTT など）と学習済みモデルは容量が大きいため含めていません。各章の問題文にある配布元から入手してください。
- chapter 5 の Gemini API を使うコードは、環境変数 `GEMINI_API_KEY` にキーを設定してから実行します。
