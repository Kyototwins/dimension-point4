from flask import Flask, request, render_template, redirect, url_for
from user_management.user_management import get_user_data
import os
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firestoreクライアントの初期化
def initialize_firestore():
    # サービスアカウントキーファイルのパス 
    service_account_key_path = os.path.join(os.getcwd(), "serviceAccountKey2.json")
    # Firebase Admin SDKの初期化
    cred = credentials.Certificate(service_account_key_path)
    firebase_admin.initialize_app(cred)
    # Firestoreクライアントの初期化
    return firestore.client()

# Firestoreクライアントをグローバル変数として初期化
db = initialize_firestore()

# ユーザー情報を追加
def add_user_data(user_id, points):
    user_ref = db.collection('users').document(user_id)
    user_ref.set({
        'points': points
    })

# ログイン画面のルート
@app.route('/')
def login():
    return render_template('login.html')

# ログイン情報を受け取り、Firestoreで認証を行う
@app.route('/authenticate', methods=['POST'])
def authenticate():
    user_id = request.form['user_id']
    password = request.form['password']

    user_data = get_user_data(user_id)

    if user_data:
        add_user_data(user_id, user_data['points'])  # ログイン成功時にFirestoreにデータを追加
        return redirect(url_for('dashboard', user_id=user_id))
    else:
        return "Invalid credentials. Please try again."

# ポイント表示画面のルート
@app.route('/dashboard/<user_id>')
def dashboard(user_id):
    user_data = get_user_data(user_id)

    if user_data:
        points = user_data.get('points', 0)
        return render_template('dashboard.html', user_id=user_id, points=points)
    else:
        return "User not found."

if __name__ == '__main__':
    app.run(debug=True)
