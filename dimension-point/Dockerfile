# ベースイメージの指定
FROM python:3.9-slim

# ワークディレクトリの設定
WORKDIR /app

# アプリケーションの依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードを追加
COPY . .

# Flaskアプリの起動
CMD ["python", "app.py"]
